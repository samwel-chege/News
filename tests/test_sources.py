import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    def setUp(self):
        self.new_sources = Sources("ABC-news","Upstart, AMD and Nucor rallied", "https://www.investors.com","general","en","Kenya")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources)) 
        