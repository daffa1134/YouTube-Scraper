import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode

def search(query):
    f = {'search_query' : query}
    return 'https://www.youtube.com/results?' + urlencode(f)

def scrape(link, mode='all'):
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'html.parser')
    soup = str(soup)
    soup = ("=".join(("".join(soup.split("\n"))).split("var ytInitialData")[1].split("=")[1:])).split(";</script>")[0]
    
    if mode == 'first':
        result = json.loads(soup)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]
    else:
        result = json.loads(soup)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]['sectionListRenderer']['contents'][0]['itemSectionRenderer']

    return result

def get_information():
    pass

link = search('lilas')

re = scrape(link)