import requests
import json
import ast
import copy as cp
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
        
        if not all or 'watch' in link:
            result = result['contents']
            temp = result[0].get('videoRenderer')

            result = result[1] if temp is None else result[0]

            return [result]
            
        return result
    
    except:
        return Exception('Error Connection')

def getVideoData(result):
    if len(result) > 1:
        result = result['contents']
    
    extracted = []

    data = {
        "channel": {
            "name" : None,
            "link" : None,
            "thumbnail" : None
        },
        "videoId" : None,
        "title": None,
        "link" : None,
        "thumbnail": None,
        "duration" : None,
        "uploaded": None,
        "views": None
    }
    
    for i in range(len(result)):
        temp = result[i].get('videoRenderer', None)
        if temp is not None:
            data['channel']['name'] = temp['ownerText']['runs'][0]['text']
            data['channel']['link'] = 'https://www.youtube.com' + temp['ownerText']['runs'][0]['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
            data['channel']['thumbnail'] = temp['channelThumbnailSupportedRenderers']['channelThumbnailWithLinkRenderer']['thumbnail']['thumbnails'][0]['url']
            data['videoId'] = temp['videoId']
            data['title'] = temp['title']['runs'][0]['text']
            data['link'] = 'https://www.youtube.com/watch?v=' + temp['videoId']
            data['thumbnail'] = 'https://i.ytimg.com/vi/' + temp['videoId'] + '/hqdefault.jpg'
            data['duration'] = temp['lengthText']['simpleText'].replace('.', ':')
            data['uploaded'] = 'Not showed' if temp.get('publishedTimeText', None) is None else temp.get('publishedTimeText')['simpleText']
            data['views'] = 'Not showed' if temp.get('viewCountText', None) is None else temp.get('viewCountText')['simpleText']
            extracted.append(cp.deepcopy(data))
    
    return extracted

def toJson(extracted, filename):
    extracted = ast.literal_eval(str(extracted))

    with open(filename + '.json', 'w', encoding='utf-8') as json_file:
        json.dump(extracted, json_file, ensure_ascii=False, indent=2)