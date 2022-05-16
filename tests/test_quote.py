import unittest
from app.models import Quote  

class TestQuote(unittest.TestCase):
    def setUp(self):
        self.my_quote = Quote("Robert", "A journey of a thousand miles begins with a single step") 

    def test_instance(self):
        self.assertTrue(isinstance(self.my_quote, Quote))

    def test_init(self):
        self.assertEqual(self.my_quote.author, "Robert") 
        self.assertEqual(self.my_quote.quote,"A journey of a thousand miles begins with a single step")  