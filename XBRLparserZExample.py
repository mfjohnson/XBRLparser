from xbrl import XBRLParser, GAAP, GAAPSerializer
import requests

def download_file():
    global dump
    url = "http://randomsite.com/file.gz"
    file = requests.get(url, stream=True)
    dump = file.raw


xbrl_parser = XBRLParser()
xbrl = xbrl_parser.parse(file("sam-20131228.xml"))