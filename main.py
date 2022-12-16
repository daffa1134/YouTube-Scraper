import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode

def search(query):
    if "watch?v=" in query:
        return query
    
    f = {'search_query' : query}
    return 'https://www.youtube.com/results?' + urlencode(f)

def scrape(link, all=True):
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'html.parser')
    soup = str(soup)

    if "watch?v=" in link:
        soup = ("=".join(("".join(soup.split("\n"))).split("var ytInitialData")[1].split("=")[1:])).split(";</script>")[0]
        soup = json.loads(soup)['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['title']['runs'][0]['text']
        return scrape(search(soup), False)

    else:
        soup = ("=".join(("".join(soup.split("\n"))).split("var ytInitialData")[1].split("=")[1:])).split(";</script>")[0]
        
        result = json.loads(soup)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]['sectionListRenderer']['contents'][0]['itemSectionRenderer']
        
        if not all:
            result = result['contents'][0]

    return json.dumps(result, indent=2)

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