import argparse
import scraper

def msg():
    return 'main.py [-h] -q [QUERY ...] -one -o [OUTPUT]'

def buildArgParser():
    parser = argparse.ArgumentParser(prog='scrape', 
                                     description='Scrape data from YouTube', 
                                     usage=msg(), 
                                     formatter_class=lambda prog: argparse.HelpFormatter('scrape', max_help_position=36)
                                    )
    
    parser.add_argument('-q', '--query', nargs='*', dest='query', required=True, help='insert query or video link from YouTube', metavar='')
    parser.add_argument('-one', dest='one', action='store_true', help='get one scrape result.')
    parser.add_argument('-o', '--output', nargs='*',dest='output', default='results', help='change output name. Default is "results"', metavar='')

    return parser


