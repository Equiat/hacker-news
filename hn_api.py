import requests
from twisted.internet import task, reactor
from news.models import NewsItem

BASE_URL = 'https://hacker-news.firebaseio.com/v0'
ALL_NEWS = {}
NEWS_ITEMS = []


def get_all_news():
    ''' get list of 100 most recent news from Hacker News API '''
    
    print('\n**********************\n Fetching data from Hacker News API. . .')
   

    response = requests.get(f'{BASE_URL}/newstories.json?print=pretty&orderBy="$key"&limitToFirst=100')
    data = response.json()

    ALL_NEWS['data'] = data

    # Get data for each news item 
    for item in ALL_NEWS['data']:
        response = requests.get(f'{BASE_URL}/item/{item}.json')
        data = response.json()

        # persist news items to database
        for news in [data]:
            if 'text' in news.keys():
                news_item = NewsItem(
                    title=news['title'], 
                    author=news['by'], 
                    type=news['type'], 
                    text=news['text'], 
                    is_from_api=True, 
                    time=news['time'],
                    score=news['score']
                ) 
                news_item.save()

            if 'url' in news.keys():
                news_item = NewsItem(
                    title=news['title'], 
                    author=news['by'], 
                    type=news['type'], 
                    url=news['url'], 
                    is_from_api=True, 
                    time=news['time'],
                    score=news['score']
                ) 
                news_item.save()
    print('\n**********************\n done')
    return
    
timeout = 300.0 # 5 minutes 

def ready():
    return get_all_news()

l = task.LoopingCall(ready)
l.start(timeout) # call every 5 minutes

reactor.run()