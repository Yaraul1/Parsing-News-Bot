from bs4 import BeautifulSoup
import requests


def get_first_news():
    headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 102.0.5005.63Safari / 537.36'
    }
    url = 'https://charter97.org/'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')
    articles_cards = soup.find_all('div', class_='news news_latest')

    for article in articles_cards:
        article_url = article.get('a', 'href')

        print(article_url)

get_first_news()
