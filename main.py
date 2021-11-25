from re import L, T, I
from bs4 import BeautifulSoup
import requests
import datetime
import time
from pprint import pprint

URL = 'https://habr.com/ru/all/'

KEYWORDS = {'Game development', '.NET', 'DevOps', 'Python', 'Пайтон'}
PARSER = 'html.parser'
#
response = requests.get(url=URL)
response.raise_for_status()
print(response)

soup = BeautifulSoup(response.text, features=PARSER)
articles_ = soup.find_all('article')
print(len(articles_))
# text_links = []


def finders():
    for atisles in articles_:

        hubs = atisles.find_all('span', class_="tm-article-snippet__hubs-item")
        hubs = set([hub.find('span').text for hub in hubs])
        for serh_world in KEYWORDS:
            if serh_world in hubs:
                header = atisles.find('h2').text
                public_date = atisles.find('span', class_='tm-article-snippet__datetime-published').text
                link = atisles.find('a', class_="tm-article-snippet__title-link").get('href')
                headlines = atisles.find('tm-article-snippet__title tm-article-snippet__title_h2')
                post_preview_text = atisles.div.div.text
                headline = atisles.h2.a.text
                owners = atisles.find('a', class_='tm-user-info__username').text
                owner_link = atisles.find('a', class_='tm-user-info__username').get('href')
                owners1 = atisles.find('a', class_='tm-article-snippet__hubs-item-link').text
                owner_link1 = atisles.find('a', class_='tm-article-snippet__hubs-item-link').get('href')
                text_ = atisles.find('div', class_='tm-article-body tm-article-snippet__lead').text
                if serh_world in "".join(text_.split()):
                    header = atisles.find('h2').text
                    text_ = atisles.find('div', class_='tm-article-body tm-article-snippet__lead').text
                    public_date = atisles.find('span', class_='tm-article-snippet__datetime-published').text
                    link = atisles.find('a', class_="tm-article-snippet__title-link").get('href')
                    print('=' * 33)
                    print(f'заголовок: - {header}, \n превью текст: - {" ".join(text_.split())}, '
                          f'\n дата публикации: - {public_date}, \n ссылка - {"https://habr.com" + link}')

finders()

def finder2():
    asd ='https://habr.com'
    for artical in articles_:
        link = set(artical.find('a', class_="tm-article-snippet__title-link").get('href').split())
        for i in link:
            url2 = asd + i
            if url2:
                responses = requests.get(url=url2)
                print(responses)
                soup = BeautifulSoup(responses.text, features=PARSER)
                articless_ = soup.find_all('article')
                for art in articless_:
                    # TODO КАК ПЕРЕДАТЬ В СУП 2 ССЫЛКИ?????
                    texts_post_ = art.find('div','article-formatted-body article-formatted-body_version-2').text or art.find(
                        'div','article-formatted-body article-formatted-body_version-1'
                    ).text
                    for serch_wworld1 in  KEYWORDS:
                        if serch_wworld1 in texts_post_:
                            print('*' * 33)
                            print(texts_post_)

finder2()



































