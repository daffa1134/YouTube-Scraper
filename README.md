# YouTube-Scraper

This is a YouTube scraper without API key and the result will stored in `.json` file

## Dependencies
> I'm assuming you have clone this project

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
python main.py -q galaxy anthem
```

or you can search by `YouTube watch link`
```
python main.py -q https://www.youtube.com/watch?v=dfOsUNxc2Xg
```

## Using Options
1. Get only one result scrape
```
python main.py -q galaxy anthem -one
```

2. Change the output file
```
python main.py -q galaxy anthem -o output
```
Then the result will stored in `output.json`

## Output
The result stored in `results.json`. This is the result using `-one`
```
[
  {
    "channel": {
      "name": "Diva (Vo.Kairi Yagi) - Topic",
      "link": "https://www.youtube.com/channel/UCxNM34epbZ_PoZiJa6I6zDQ"
    },
    "videoId": "nbSwgEWkM6w",
    "title": "Galaxy Anthem",
    "link": "https://www.youtube.com/watch?v=nbSwgEWkM6w",
    "thumbnail": "https://i.ytimg.com/vi/nbSwgEWkM6w/hqdefault.jpg",
    "duration": "4:32",
    "uploaded": "Not showed",
    "views": "1.296.663 x ditonton"
  }
]
```