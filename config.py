from instance.config import NEWS_API_KEY
from re import DEBUG
import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = ' https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_ARTICLES_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_CAST_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
# https://newsapi.org/v2/everything?q=business&apiKey=d81f0b72e8394be9a3dddcc574e249ae
class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configurations settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG  = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
    }