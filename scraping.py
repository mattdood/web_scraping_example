import requests
from bs4 import BeautifulSoup
import json

def hackernews_rss():
    try:
        r = requests.get()
        return print('The scraping job succeeded: ', r.status_code)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)

print('Starting scraping')
hackernews_rss()
print('Finished scraping')