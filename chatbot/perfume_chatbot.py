import json
import re
import random

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from chatbot.chatbot_base import ChatbotBase
from chatbot.intent_chatbot import IntentChatbot


class PerfumeChatbot(ChatbotBase):
    """
    A hybrid chatbot combining custom scent-based perfume recommendations with general intent handling using IntentChatbot.
    """

    def __init__(self, name: str = "Perfumer", dataset: pd.DataFrame = None) -> None:
        """
        Initialize chatbot with a dataset and prepare TF-IDF for perfume matching.
        """

        self.name = name
        self.conversation_is_active = True
        self.intent_chatbot = IntentChatbot(name=name)
        self.dataset = dataset
        with open("data\\scent_keywords.json", "r", encoding="utf-8") as f:
            self.scent_keywords = json.load(f)

        # Ensure required columns ('Name', 'Notes') exist
        if self.dataset is not None and 'Name' in self.dataset and 'Notes' in self.dataset:
            self.dataset['Name'] = self.dataset['Name'].fillna('')
            self.dataset['Notes'] = self.dataset['Notes'].fillna('')
            self.dataset['full_description'] = self.dataset['Name'] + " " + self.dataset['Notes']
            self.tfidf_vectorizer = TfidfVectorizer()
            self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.dataset['full_description'])
        else:
            self.tfidf_matrix = None

    def extract_keywords(self, text: str) -> list[str]:
        pattern = r'\b[a-zA-Z]+\b'
        words = re.findall(pattern, text)
        stop_words = {'a', 'an', 'the', 'and', 'in', 'of', 'on', 'for', 'to', 'with', 'by', 'it', 'is', 'are', 'this'}
        filtered_words = [word for word in words if word not in stop_words]
        return filtered_words

    def greeting(self) -> None:
        print(f"Hello, I am {self.name}, your personal perfume consultant. Let's start this wonderful journey of smell together!\n"
            f"My functions are as follows:\n"
            f"[1] I can recommend perfumes for you, just need to tell me what [scents] you like or your [zodiac sign].\n"
            f"[2] I can also share perfume-related jokes, or tell you about some perfume brands or their history.\n"
            f"[3] Of course, I can also get time; help you relieve your emotions; introduce myself, etc.")

    def farewell(self) -> None:
        print("Thank you for using customised perfume Journeys. We wish you a wonderful day in beautiful fragrances. Remember to give me a good review!")

    def receive_input(self) -> str:
        return input("You: ")

    def recommend_perfume(self, user_input: str, scent_category: str) -> str:
        """
        Recommend a perfume based on user input and scent category.
        Extracts keywords from the input, filters the dataset by category, and selects the best-matching perfume using a simple scoring system.
        """    
        self.dataset['Notes'] = self.dataset['Notes'].fillna('').astype(str)
        keywords = self.extract_keywords(user_input)
        scent_filtered_data = self._filter_by_scent_category(scent_category)
        perfume_scores = self._calculate_scores(scent_filtered_data, keywords)

        if perfume_scores:
            recommended_perfume = self._select_best_perfume(scent_filtered_data, perfume_scores)
            return self._compose_recommendation_response(recommended_perfume)
        else:
            return "I'm really sorry that I couldn't find the suitable perfume, can you change your favourite scent? (e.g. rose, violet, lime, grapefruit)"


    def _filter_by_scent_category(self, scent_category: str) -> pd.DataFrame:
        if scent_category:
            return self.dataset[self.dataset['Notes'].str.contains(scent_category, case=False, na=False)]
        return self.dataset


    def _calculate_scores(self, data: pd.DataFrame, keywords: list[str]) -> list[int]:
        scores = []
        for _, perfume in data.iterrows():
            perfume_notes = perfume['Notes']
            score = sum(1 for keyword in keywords if keyword in perfume_notes)
            scores.append(score)
        return scores


    def _select_best_perfume(self, data: pd.DataFrame, scores: list[int]) -> pd.Series:
        most_similar_index = scores.index(max(scores))
        return data.iloc[most_similar_index]


    def _compose_recommendation_response(self, perfume: pd.Series) -> str:
        """
        Generate a user-facing recommendation string from the selected perfume.
        """
        perfume_name = perfume['Name']
        perfume_brand = perfume['Brand']
        perfume_notes = perfume['Notes']

        responses = [
            f"You're in for a treat! How about the delightful [{perfume_name}] from [{perfume_brand}]? It has a wonderful blend of notes like [{perfume_notes}], perfect for your next perfume adventure. \nDo you have any other favourite flavours? I can continue to recommend them for you.",
            f"How about [{perfume_name}] from [{perfume_brand}]? Its [{perfume_notes}] will make you feel like you're wearing a little slice of luxury every day. \nDo you have any other favourite flavours? I can continue to recommend them for you.",
            f"Here's a thought: why not try [{perfume_name}] from [{perfume_brand}]? The [{perfume_notes}] are fresh and lively, just the kind of scent that might brighten your day. \nDo you have any other favourite flavours? I can continue to recommend them for you.",
        ]
        return random.choice(responses)

    def process_input(self, user_input: str) -> str:
        # Identify if user input is related to perfume scents
        for category, keywords in self.scent_keywords.items():
            if any(keyword in user_input.lower() for keyword in keywords):
                return self.recommend_perfume(user_input, category)

        # Delegate to intent-based response if no perfume scent is detected
        return self.intent_chatbot.generate_response(user_input)

    def respond(self) -> None:
        self.greeting()
        while self.conversation_is_active:
            received_input = input("\nYou: ").strip().lower()
            if received_input in ["exit", "quit", "bye", "goodbye"]:
                self.farewell()
                self.conversation_is_active = False
                break
            processed_input = self.process_input(received_input)
            print(f"Bot: {processed_input}")