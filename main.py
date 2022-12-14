import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode

def search(query):
    f = {'search_query' : query}
    return 'https://www.youtube.com/results?' + urlencode(f)

def scrape(link, all=True):
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'html.parser')
    soup = str(soup)
    soup = ("=".join(("".join(soup.split("\n"))).split("var ytInitialData")[1].split("=")[1:])).split(";</script>")[0]
    
    if all:
        result = json.loads(soup)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]['sectionListRenderer']['contents'][0]['itemSectionRenderer']
    else:
        result = json.loads(soup)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]

    return result

def getVideoId(result):
    if len(result) != 1:
        result = res['contents']
        vidId = []
        
        for i in range(len(result)):
            x = result[i].get('videoRenderer', 'None')
            if "videoId" in x:
                vidId.append(x['videoId'])
        
        return vidId
    else:
        return result['videoRenderer']['videoId']
        
