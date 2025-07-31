import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from unittest.mock import patch, MagicMock
import random

import pandas as pd

from chatbot.chatbot_base import ChatbotBase
from chatbot.intent_chatbot import IntentChatbot
from chatbot.perfume_chatbot import PerfumeChatbot, TfidfVectorizer

# Sample data for PerfumeChatbot tests
data = {
    'Name': ['Rose Delight', 'Citrus Splash'],
    'Brand': ['BrandA', 'BrandB'],
    'Notes': ['rose lavender', 'citrus lemon']
}

class TestChatbotBase(unittest.TestCase):
    def setUp(self):
        self.bot = ChatbotBase(name='TestBot')

    @patch('builtins.print')
    def test_greeting_and_farewell(self, mock_print):
        self.bot.greeting()
        mock_print.assert_called_with('Hello I am TestBot')
        self.bot.farewell()
        mock_print.assert_called_with('Goodbye!')

    @patch('builtins.input', return_value='Hi')
    def test_respond_flow(self, mock_input):
        class DummyBot(ChatbotBase):
            def process_input(self, user_input):
                return user_input.lower()
            def generate_response(self, processed_input):
                return f"Echo: {processed_input}"
        dummy = DummyBot(name='Dummy')
        response = dummy.respond()
        self.assertEqual(response, 'Echo: hi')

class TestIntentChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = IntentChatbot(name='IntentTest')
        # Mock sentiment analyzer
        self.bot.analyzer = MagicMock()
        self.bot.analyzer.polarity_scores.side_effect = (
            lambda text: {'compound': 0.7} if 'happy' in text else {'compound': -0.7} if 'angry' in text else {'compound': 0.0}
        )

    def test_sentiment_methods(self):
        self.assertTrue(self.bot.user_is_happy('I am happy'))
        self.assertFalse(self.bot.user_is_happy('I am sad'))
        self.assertTrue(self.bot.user_is_angry('I am angry'))
        self.assertFalse(self.bot.user_is_upset('I am calm'))

    def test_sentiment_analyzer_exception(self):
        # Simulate analyzer throwing an exception
        self.bot.analyzer.polarity_scores.side_effect = Exception("sentiment error")
        with self.assertRaises(Exception) as cm:
            self.bot.user_is_happy('hello')
        self.assertIn('sentiment error', str(cm.exception))

    def test_recommend_perfume_based_on_zodiac(self):
        resp = self.bot.recommend_perfume_based_on_zodiac('Aries')
        self.assertIsInstance(resp, str)

        resp_unknown = self.bot.recommend_perfume_based_on_zodiac('UnknownSign')
        self.assertEqual(resp_unknown, "Sorry, I don't have a perfume suggestion for that sign.")

    @patch('random.choice', lambda seq: seq[0])
    def test_default_help_joke(self):
        self.assertEqual(self.bot.default_response(), "Sorry, I didn't quite catch that.")
        self.assertIn('help', self.bot.help().lower())
        joke = self.bot.get_joke()
        self.assertIn('perfume', joke.lower())

class TestPerfumeChatbot(unittest.TestCase):
    def setUp(self):
        df = pd.DataFrame(data)
        # Patch TF-IDF to avoid empty vocabulary errors during init
        with patch.object(TfidfVectorizer, 'fit_transform', return_value=None):
            self.bot = PerfumeChatbot(name='PerfumeTest', dataset=df)
        # scent_keywords controls filtering; brand not used
        self.bot.scent_keywords = {'rose': ['rose'], 'citrus': ['citrus']}

    def test_extract_keywords(self):
        text = 'I love rose and citrus scents!'
        keywords = self.bot.extract_keywords(text)
        self.assertIn('rose', keywords)
        self.assertIn('citrus', keywords)

    def test_filter_calculate_select(self):
        filtered = self.bot._filter_by_scent_category('rose')
        self.assertEqual(len(filtered), 1)
        scores = self.bot._calculate_scores(filtered, ['rose'])
        self.assertEqual(scores, [1])
        best = self.bot._select_best_perfume(filtered, scores)
        self.assertEqual(best.Name, 'Rose Delight')

    @patch('random.choice', lambda seq: seq[0])
    def test_compose_response_name_only(self):
        row = pd.Series({'Name': 'Test', 'Brand': 'B', 'Notes': 'n1 n2'})
        resp = self.bot._compose_recommendation_response(row)
        self.assertIn('Test', resp)

    def test_recommend_perfume_not_found(self):
        with self.assertRaises(ValueError):
            PerfumeChatbot(name='Empty', dataset=pd.DataFrame(columns=['Name','Brand','Notes']))

    def test_process_input(self):
        resp = self.bot.process_input('I like rose')
        self.assertIn('Rose Delight', resp)
        resp2 = self.bot.process_input('hello')
        self.assertIsInstance(resp2, str)

if __name__ == '__main__':
    unittest.main()