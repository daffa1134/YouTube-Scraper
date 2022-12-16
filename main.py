import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import time

def search(query):
    if "watch?v=" in query:
        query = query.split('/')[-1].split('&ab_channel')[0]
    
    f = {'search_query' : query}
    return 'https://www.youtube.com/results?' + urlencode(f)

def scrape(link, all=True):
    req = requests.get(link)
    
    soup = BeautifulSoup(req.text, 'html.parser')
    soup = str(soup)
    soup = ("=".join(("".join(soup.split("\n"))).split("var ytInitialData")[1].split("=")[1:])).split(";</script>")[0]

    result = json.loads(soup)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]['sectionListRenderer']['contents'][0]['itemSectionRenderer']
    
    if not all:
        result = result['contents'][0]

    return result

def getVideoId(result):
    if len(result) != 1:
        result = res['contents']
        vidId = []
        
        for i in range(len(result)):
            temp = result[i].get('videoRenderer', 'None')
            if "videoId" in temp:
                vidId.append(temp['videoId'])
        
        return vidId
    else:
        return result['videoRenderer']['videoId']