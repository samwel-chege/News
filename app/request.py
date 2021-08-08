from app.models.highlights import Highlights
import urllib.request,json
from .config import Config 
from app import app 

api_key = app.config['NEWS_API_KEY']

#Getting the news base url

base_url = app.config['NEWS_API_BASE_URL']

def get_news():
    '''
    Function that gets the json response to the url request
    '''
    get_news_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results   


def process_results(results_list):
    '''
    Function that processes the news articles and transform them to a list of objects

    Args:
        articles_list: A list of dictionaries that contain movie details   

    Returns: 
           news_results: A list of news objects      
    ''' 

    news_results = []  
    for news_item in results_list:
           
        author = news_item.get('author')  
        title = news_item.get('title') 
        description  = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        

        if urlToImage:
            news_object = Highlights(author,title,description,url,urlToImage)
            news_results.append(news_object)

    return news_results    

