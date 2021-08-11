import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles("Daniel Cooper","Airpods","Upstart, AMD and Nucor rallied", "https://www.investors.com","https://www.investors.com","2021-08-11","Stocks climbed at the starting bell Wednesday")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles)) 
        
           