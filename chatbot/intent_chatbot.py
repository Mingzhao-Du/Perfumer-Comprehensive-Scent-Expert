import re
import random
import nltk
from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize sentiment lexicon used for sentiment scoring
nltk.download('vader_lexicon')


class IntentChatbot:
    """
    A rule-based chatbot using sentiment analysis and keyword matching.
    Provides responses based on user emotions, perfume brand knowledge, zodiac-based suggestions, and general small talk.
    """

    def __init__(self, name: str = "Chatbot") -> None:
        """Initialize chatbot with name and sentiment analyzer."""
        self.name = name
        self.conversation_is_active = True
        self.analyzer = SentimentIntensityAnalyzer()

        # Mapping zodiac signs to personalized scent styles
        self.zodiac_perfume_map = {
            "aries": "Spicy and bold perfumes with hints of cinnamon or pepper",
            "taurus": "Floral and earthy perfumes with lavender and patchouli",
            "gemini": "Citrus and fresh perfumes, light and airy",
            "cancer": "Soft and comforting, with notes of vanilla and coconut",
            "leo": "Warm and luxurious perfumes with amber and musk",
            "virgo": "Fresh, clean scents with notes of lemon and green tea",
            "libra": "Balanced perfumes, with a touch of rose and jasmine",
            "scorpio": "Mysterious and deep, with scents of leather and oud",
            "sagittarius": "Woody and adventurous scents with sandalwood and cedar",
            "capricorn": "Earthy and grounding perfumes, with vetiver and moss",
            "aquarius": "Unique and unconventional, with aquatic and metallic notes",
            "pisces": "Dreamy and floral perfumes, with hints of lily and jasmine"
        }

    def respond_happy_confirmation(self) -> str:
        return random.choice([
            "It makes me happy to see you happy. Ongoing you continue to serve.",
            "Since you are so happy, remember to give me a good review.",
            "Remember to be so happy every day. Continuing you continue to serve.",
            "Since you are in such a good mood today, why don't you try letting me recommend a perfume for you?"
        ])

    def respond_upset_confirmation(self) -> str:
        return random.choice([
            "Don't be sad about the little things. Do you want me to tell you a joke?",
            "Life is full of setbacks, may you get out of it soon. Shall I tell you a joke to cheer you up?",
            "Please stop being frustrated! I can recommend a perfume for you, it might bring you joy."
        ])

    def respond_angry_confirmation(self) -> str:
        return random.choice([
            "Please turn your grief into strength. Shall I tell you a joke to cheer you up?",
            "Anger harms the body. Why don't you let me tell you a joke?",
            "If venting your anger at me makes you feel better, then go ahead."
        ])

    def respond_small_talk(self) -> str:
        return (
            "Hello, all the best!\n"
            "My functions are as follows:\n"
            "[1] I can recommend perfumes for you, just need to tell me what [scents] you like or your [zodiac sign].\n"
            "[2] I can also share perfume-related jokes, or tell you about some perfume brands or their history.\n"
            "[3] Of course, I can also get time; help you relieve your emotions; introduce myself, etc."
        )

    def get_time(self) -> str:
        now = datetime.now()
        return f"The time is {now.strftime('%H:%M:%S')}. \nDo you have any other questions? Continuing to serve you."

    def help(self) -> str:
        return random.choice([
            "I'm here to help with anything you need! Whether it's jokes, advice, or a friendly chat, just ask!",
            "Need assistance or a good laugh? I’m here for both! Ask me anything!",
            "I’m your friendly chatbot, ready to help, share a joke, or just have a conversation. What’s on your mind?",
            "Looking for answers, jokes, or just someone to talk to? I’ve got you covered. Ask away!",
            "I’m always ready to chat, tell a joke, or help you out! What can I do for you today?",
            "Want a fun chat or a good laugh? Or maybe some help? Just ask me anything!"
        ])

    def get_joke(self) -> str:
        return random.choice([
            "My friend opened a perfume shop specializing in failed scent combinations. He says every time someone leaves, it's a huge relief.",
            "Why are perfume bottles always so nervous? Because they might get sprayed.",
            "Why can’t perfume keep a secret? Because it always gets out.",
            "I created a coffee-scented perfume. When I wore it, I felt so energized—everyone else thought I got a job at a café.",
            "Someone said my perfume was too expensive. I replied, 'Can’t you smell the confidence?'",
            "One perfume bottle asked another, 'Why are you so quiet?' It replied, 'I’m just bottling it up.'",
            "I once bought a perfume designed to cover bad smells. Everyone kept asking, 'What’s that scent?' I said, 'It’s called ‘Trying My Best.’'"
        ])

    def ask_follow_up_question(self) -> str:
        """Encourage user to continue the conversation."""
        return self.respond_small_talk()

    def get_perfume_history(self) -> str:
        return random.choice([
            "Perfume dates back to ancient Egypt, where it was used in religious rituals and for personal adornment.",
            "The word 'perfume' comes from the Latin word perfumare, meaning 'to smoke through,' as incense was often used in early fragrance-making.",
            "The first modern perfume factory was established in the 16th century in Italy, making it more accessible to the elite.",
            "In the 17th century, perfume became a symbol of wealth and sophistication in Europe, especially among French royalty.",
            "The development of alcohol-based perfumes in the 18th century made fragrances more wearable and longer-lasting.",
            "Perfume became a significant part of the fashion world in the 19th century, with famous houses like Guerlain and Chanel emerging.",
            "In the 20th century, synthetic fragrances were introduced, revolutionizing the perfume industry by expanding scent possibilities."
        ])

    def get_perfume_brand_info(self) -> str:
        return random.choice([
            "Chanel: Classic elegance and timeless luxury. Chanel No. 5, launched in 1921, is one of the best-selling perfumes in history, known for its floral aldehyde scent.",
            "Dior: Bold and elegant fragrances that reflect French refinement. Dior perfumes are often known for their rich, complex compositions.",
            "Guerlain: Being one of the oldest perfume houses (established in 1828). Guerlain is known for creating rich, opulent scents with a focus on floral, oriental, and powdery notes.",
            "Tom Ford: Bold, sensual, and modern scents with a touch of luxury. Tom Ford’s fragrances often feature warm, spicy, and woody notes.",
            "Creed: High-quality, luxurious fragrances with a long-lasting, unique scent profile. Aventus, launched in 2010, is famous for its smoky and fruity blend.",
            "Jo Malone: Simple, fresh, and elegant fragrances with a focus on natural ingredients. Jo Malone is known for its ability to blend scents to create subtle yet distinctive perfumes.",
            "Yves Saint Laurent: Sensual and bold fragrances, often with spicy, oriental, or floral notes. Opium, launched in 1977, became an iconic, controversial fragrance with its exotic and spicy scent.",
            "Hermès: Elegant, minimalist, and high-end fragrances that often feature earthy and woody notes. Hermès is known for creating sophisticated yet subtle perfumes.",
            "Chloé: Light, floral, and feminine scents that evoke elegance and romance. Chloé’s fragrances often feature a soft, powdery quality.",
            "Acqua di Parma: High-quality, refreshing, and sophisticated citrus-based scents. Acqua di Parma is known for its luxurious, Italian-made fragrances."
        ])

    def get_chatbot_info(self) -> str:
        return random.choice([
            "Regarding why I'm called ‘perfumer’, it's because I know a lot about perfume and I'd love to share that knowledge with you! \nPlease go ahead and ask me questions.",
            "I am ‘perfumer’, besides perfume, I have many other functions, such as checking the time, telling jokes, comforting your mood and so on. \nPlease go ahead and ask me questions.",
            "I'm ‘perfumer’, you can just call me by my first name, and I'm happy to bring you perfume knowledge and emotional value. \nPlease go ahead and ask me questions."
        ])

    def user_is_happy(self, input_str: str) -> bool:
        """Detect whether the user is expressing happiness."""
        score = self.analyzer.polarity_scores(input_str)['compound']
        return score > 0.5 or any(k in input_str.lower() for k in ["happy", "joyful", "excited", "pleased", "cheerful", "delighted", "elated"])

    def user_is_upset(self, input_str: str) -> bool:
        """Detect whether the user is expressing frustration or sadness."""
        score = self.analyzer.polarity_scores(input_str)['compound']
        return score < -0.3 or any(k in input_str.lower() for k in ["Irritated", "Frustrated", "Agitated", "Upset", "Displeased", "Infuriated"])

    def user_is_angry(self, input_str: str) -> bool:
        """Detect whether the user is expressing anger."""
        score = self.analyzer.polarity_scores(input_str)['compound']
        return score < -0.5 or any(k in input_str.lower() for k in ["angry", "mad", "furious", "annoyed", "fuck", "pissed", "shit"])

    def recommend_perfume_based_on_zodiac(self, zodiac_sign: str) -> str:
        return self.zodiac_perfume_map.get(zodiac_sign.lower(), "Sorry, I don't have a perfume suggestion for that sign.")

    def default_response(self) -> str:
        return random.choice([
            "Sorry, I didn't quite catch that.", 
            "Hmm, I didn’t understand that.", 
            "Oops, I didn’t quite catch that.", 
            "I’m not sure I understood.", 
            "Sorry, I didn’t quite get that."
        ])

    def with_guidance(self) -> str:
        return (
            "You can ask me some questions again. I'd be happy to help！\n"
            "My functions are as follows:\n"
            "[1] I can recommend perfumes for you, just need to tell me what [scents] you like or your [zodiac sign].\n"
            "[2] I can also share perfume-related jokes, or tell you about some perfume brands or their history.\n"
            "[3] Of course, I can also get time; help you relieve your emotions; introduce myself, etc."
            )

    def generate_response(self, user_input: str) -> str:
        """Main routing logic that analyzes input and returns a response."""
        user_input = user_input.lower()

        if any(k in user_input for k in ["perfume history", "history of perfume", "origin of perfume", "history"]):
            return self.get_perfume_history()
        
        if any(k in user_input for k in ["perfume brands", "brand information", "perfume brand information", "brand"]):
            return self.get_perfume_brand_info()
        
        if any(k in user_input for k in ["who are you", "what do you do", "introduce yourself"]):
            return self.get_chatbot_info()
        
        if any(k in user_input for k in ["hello", "hi", "bro", "small talk", "good morning", "good afternoon", "good evening"]):
            return self.respond_small_talk()
        
        if any(k in user_input for k in ["joke", "make fun"]):
            return self.get_joke()
        
        if any(k in user_input for k in ["help", "assist", "aid"]):
            return self.help()
        
        if any(k in user_input for k in ["what time is it", "current time", "time", "when"]):
            return self.get_time()
        
        if any(k in user_input for k in ["next", "other"]):
            return self.ask_follow_up_question()
        
        if self.user_is_happy(user_input):
            return self.respond_happy_confirmation()
        
        if self.user_is_upset(user_input):
            return self.respond_upset_confirmation()
        
        if self.user_is_angry(user_input):
            return self.respond_angry_confirmation()

        for zodiac in self.zodiac_perfume_map:
            if zodiac in user_input:
                suggestion = self.recommend_perfume_based_on_zodiac(zodiac)
                return f"Based on your zodiac sign ({zodiac}), I suggest a perfume with: {suggestion}. Of course, you don't have to pay attention to my advice if you have a favourite scent, it's most important to pursue what you like! \nAre you satisfied with the answer? You can keep asking me questions."

        return self.default_response() + "\n" + self.with_guidance()