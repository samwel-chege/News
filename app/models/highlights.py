class Articles:
    '''
    Articles class to define articles 
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class Sources:
    '''
    Sources class to describe sources 
    ''' 
    def __init__(self,name,description,url,category,language,country):
        self.name = name
        self.description = description 
        self.url = url
        self.category = category
        self.language = language
        self.country = country

              
        