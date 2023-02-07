import aiohttp
import json
import ast
import copy as cp
from urllib.parse import urlencode

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

async def scrape_video_page(link):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:

                html = await response.text()
                
                initial_data = ("=".join(("".join(html.split("\n"))).split("var ytInitialPlayerResponse")[1].split("=")[1:])).split(";</script>")[0]
                initial_data = json.loads(initial_data)['videoDetails']

                channel_data = ("=".join(("".join(html.split("\n"))).split("var ytInitialData")[1].split("=")[1:])).split(";</script>")[0]
                channel_data = json.loads(channel_data)['contents']['twoColumnWatchNextResults']['results']['results']['contents']
                
                return {
                    "data": initial_data,
                    "channel": channel_data
                }

    except:
        return Exception("Error Connection")

async def scrape_result_page(query, one=False):
    f = {'search_query' : query}
    link = 'https://www.youtube.com/results?' + urlencode(f)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:

                html = await response.text()
                
                initial_data = ("=".join(("".join(html.split("\n"))).split("var ytInitialData")[1].split("=")[1:])).split(";</script>")[0]
                initial_data = json.loads(initial_data)["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]['sectionListRenderer']['contents'][0]['itemSectionRenderer']
                
                if one:
                    initial_data = initial_data['contents']
                    temp = initial_data[0].get('videoRenderer')

                    initial_data = initial_data[1] if temp is None else initial_data[0]

                    return [initial_data]

                return initial_data

    except:
        return Exception("Error Connection")

def get_page_data(result):
    if len(result) > 1:
        result = result['contents']
    
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
            data['uploaded'] = 'Not showed' if temp.get('publishedTimeText', None) is None else temp['publishedTimeText']['simpleText']
            data['views'] = 'Not showed' if temp.get('viewCountText', None) is None else temp['viewCountText']['simpleText']
            
            extracted.append(cp.deepcopy(data))
    
    return extracted

def get_video_data(result_data, result_channel):
    data['channel']['name'] = result_data['author']
    data['channel']['link'] = 'https://www.youtube.com/channel/' + result_data['channelId']
    data['channel']['thumbnail'] = result_channel[1]['videoSecondaryInfoRenderer']['owner']['videoOwnerRenderer']['thumbnail']['thumbnails'][0]['url']
    data['videoId'] = result_data['videoId']
    data['title'] = result_data['title']
    data['link'] = 'https://www.youtube.com/watch?v=' + result_data['videoId']
    data['thumbnail'] = 'https://i.ytimg.com/vi/' + result_data['videoId'] + '/hqdefault.jpg'
    data['duration'] = second_to_minute(result_data['lengthSeconds'])
    data['uploaded'] = result_channel[0]['videoPrimaryInfoRenderer']['relativeDateText']['simpleText']
    data['views'] = result_channel[0]['videoPrimaryInfoRenderer']['viewCount']['videoViewCountRenderer']['viewCount']['simpleText']

    return data

def second_to_minute(second):
    minute = int(second) // 60
    second = int(second) % 60

    return f"{minute}:{second}"

def to_json(extracted, file_name):
    extracted = ast.literal_eval(str(extracted))

    with open(file_name + '.json', 'w', encoding='utf-8') as json_file:
        json.dump(extracted, json_file, ensure_ascii=False, indent=2)