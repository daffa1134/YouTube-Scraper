# YouTube-Scraper

This is a YouTube scraper without api key and the result will stored in `.json` file

## Dependencies
Install the requirements
```
pip install -r requirements.txt
```

## Usage
```
main.py [-h] -q [QUERY ...] -one -o [OUTPUT]
```
| Option | Description |
| ---    | -------------------------------------------------------- |
| `-h`   | Help |
| `-q`   | Insert query or YouTube watch link |
| `-one` | Option to get only one result video. Default is one page.|
| `-o`   | Change output filename. Default is results. |


## Example
You can search with `query`
```
python main.py -q lilas
```

or you can search by `YouTube watch link`
```
python main.py -q https://www.youtube.com/watch?v=dfOsUNxc2Xg
```

## Using Options
1. Get only one result scrape
```
python main.py -q lilas -one
```

2. Change the output file
```
python main.py -q lilas -o output
```
Then the result will stored in `output.json`

## Output
The result stored in `results.json`. This is the result using `-one`
```
[
  {
    "channel": {
      "name": "澤野弘之 / SawanoHiroyuki[nZk]",
      "link": "https://www.youtube.com/channel/UCbJM_Y06iuUOl3hVPqYcvng"
    },
    "videoId": "dfOsUNxc2Xg",
    "title": "SawanoHiroyuki[nZk]:Honoka Takahashi『LilaS』×TVアニメ「８６―エイティシックス―」Collaboration Movie",
    "link": "https://www.youtube.com/watch?v=dfOsUNxc2Xg",
    "thumbnail": "https://i.ytimg.com/vi/dfOsUNxc2Xg/hqdefault.jpg",
    "duration": "4:23",
    "uploaded": "9 bulan yang lalu",
    "views": "6.433.558 x ditonton"
  }
]
```