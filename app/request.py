from os import name
from app.models.highlights import  Articles,Sources
import urllib.request,json
from config import Config 
# from app import app 

api_key = None
base_url =  None
source_url = None
cast_url =  None


#Getting the news base url
def configure_request(app):
    global base_url,source_url,cast_url,api_key
    base_url = app.config['NEWS_ARTICLES_URL']
    source_url = app.config['NEWS_SOURCE_URL']
    cast_url = app.config['NEWS_CAST_URL']
    api_key = app.config['NEWS_API_KEY']

def get_news(category):
    '''
    Function that gets the json response to the url request
    '''
    get_news_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results  


def process_results(news_list):
    '''
    Function that processes the news articles and transform them to a list of objects

    Args:
        articles_list: A list of dictionaries that contain movie details   

    Returns: 
           news_results: A list of news objects      
    ''' 

    news_results = []  
    for news_item in news_list:
           
        author = news_item.get('author')  
        title = news_item.get('title') 
        description  = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
       

        if urlToImage:
            news_object = Articles(author,title,description,url,urlToImage,publishedAt,content)
            news_results.append(news_object)

    return news_results  


def get_sources(): 

    get_sources_url = source_url.format(api_key)  

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data) 

        news_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            news_results = process_results(sources_results_list)

    return news_results   


def process_results(sources_list):
    '''
    Function that processes the news articles and transform them to a list of objects

    Args:
        articles_list: A list of dictionaries that contain movie details   

    Returns: 
           news_results: A list of news objects      
    ''' 

    sources_results = []  
    for news_item in sources_list:
           
        name = news_item.get('name')
        description  = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')
        language = news_item.get('language')
        

        if name:
            sources_object = Sources(name,description,url,category,language,country)
            sources_results.append(sources_object)

    return sources_results     

def get_cast(id):
    get_cast_url = cast_url.format(id,api_key)

    with urllib.request.urlopen(get_cast_url) as url:
        cast_url_data = url.read()
        cast_url_response = json.loads(cast_url_data)  

        cast_object = None
        if cast_url_response:
            id = cast_url_response.get('id')
            name = cast_url_response.get('name')
            description = cast_url_response.get('description')
            url = cast_url_response.get('url')
            category = cast_url_response.get('category')
            language = cast_url_response.get('language')
            country = cast_url_response.get('country')

            cast_object = Sources(name,description,url,category,language,country)

        return cast_object    



       

