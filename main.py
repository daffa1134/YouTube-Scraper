import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode

def scrape(query, all=True):
    if "watch?v=" in query:
        query = query.split('/')[-1].split('&ab_channel')[0]
    
    f = {'search_query' : query}
    link = 'https://www.youtube.com/results?' + urlencode(f)

    try:
        req = requests.get(link)
    
        soup = BeautifulSoup(req.text, 'html.parser')
        soup = str(soup)
        soup = ("=".join(("".join(soup.split("\n"))).split("var ytInitialData")[1].split("=")[1:])).split(";</script>")[0]

        result = json.loads(soup)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]['sectionListRenderer']['contents'][0]['itemSectionRenderer']
        
        if not all:
            result = result['contents']
            temp = result[0].get('videoRenderer')
            
            if temp is None:
                result = result[1]
            else:
                result = result[0]
            
        return result
    
    except:
        return Exception('Error Connection')

def getVideoId(result):
    if len(result) != 1:
        result = result['contents']
        vidId = []
        
        for i in range(len(result)):
            temp = result[i].get('videoRenderer', None)
            if temp is not None:
                vidId.append(temp['videoId'])
        
        return vidId
    else:
        return result['videoRenderer']['videoId']

def extract():
    output = {
        "channel": {
            "name" : None,
            "link" : None
        },
        "videoId" : None,
        "title": None,
        "link" : None,
        "thumbnail": None,
        "duration" : None,
        "uploaded": None,
        "views": None
    }

    return output