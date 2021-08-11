
from flask import render_template,request,redirect,url_for
from ..request import get_news, get_sources,get_cast
from . import main

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    business_news = get_news('business')
    technology_news = get_news('technology')
    general_news = get_news('general')

    return render_template('index.html',business = business_news,technology = technology_news,general = general_news)

@main.route('/news') 
def news():

    '''
    View news page function that returns the news details page and its data
    '''
    source =  get_sources()
    

    return render_template('news.html',source = source)  

@main.route('/cast')
def cast():
    bbc_news = get_cast('bbc-news')
    abc_news = get_cast('abc-news')
    ary_news = get_cast('ary-news')
    bbc_sport = get_cast('bbc-sport')

    return render_template('cast.html',bbc = bbc_news,abc= abc_news,ary = ary_news,bbcs = bbc_sport)
