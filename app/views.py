
from flask import render_template
from app import app 
from .request import get_news

#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    business_news = get_news('business')
    technology_news = get_news('technology')
    general_news = get_news('general')
    return render_template('index.html',business = business_news,technology = technology_news,general = general_news)

@app.route('/news/<int:news_id>') 
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    ''' 
    return render_template('news.html',id  = news_id)  