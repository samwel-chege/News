from instance.config import NEWS_API_KEY
from re import DEBUG


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = ' https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_HIGHLIGHT_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'

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