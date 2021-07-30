import requests
from news.models.news_item import NewsItem

BASE_URL = 'https://hacker-news.firebaseio.com/v0'
ALL_NEWS = {}
NEWS_ITEMS = []


def get_all_news():
    ''' get list of 100 most recent news from Hacker News API '''

    response = requests.get(f'{BASE_URL}/newstories.json?print=pretty&orderBy="$key"&limitToFirst=30')
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
    return

get_all_news()
print('\n**********************\n done')