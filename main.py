from pprint import pprint
import json
from bs4 import BeautifulSoup
import requests
#
# response = requests.get("https://news.ycombinator.com/")
#
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# noodles = soup.select(selector='body '
#                                'center '
#                                'tr '
#                                'td '
#                                'table '
#                                'tr '
#                                'td.title '
#                                'a.storylink')
#
# for noodle in noodles:
#     print(noodle.text)
#     if 'item' in noodle["href"]:
#         print(f'https://news.ycombinator.com/{noodle["href"]}')
#     else:
#         print(noodle["href"])
#
#
empire_movie_list = requests.get(url='https://www.empireonline.com/movies/features/best-movies-2/')
eml_txt = empire_movie_list.text

movie_soup = BeautifulSoup(eml_txt, "html.parser")
# print(movie_soup.prettify())
jsoooon = movie_soup.select_one(selector='script#__NEXT_DATA__').string

jsoon = json.loads(jsoooon)

with open('dog.json', mode='w') as file:
    dog = json.dumps(jsoon, indent=4)
    file.write(dog)
    # /props/pageProps/data/getArticleByFurl/_layout/7/content/coverImage/titleText
    # /props/pageProps/data/getArticleByFurl/_layout/7/content/images/1/titleText
    # /props/pageProps/data/getArticleByFurl/_layout/7/content/images/20/titleText
for inty in range(1, 100):
    print(jsoon['props']['pageProps']['data']['getArticleByFurl']['_layout'][7]['content']['images'][inty]['titleText'])