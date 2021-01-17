import requests
from dotenv import load_dotenv
import argparse
import os

BITLY_TOKEN = ""


def get_shorten_link(token, url):
    bitlink_site_url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {"Authorization" : "Bearer {}".format(token)}
    payload = {"long_url": url}
    responce = requests.post(bitlink_site_url, json=payload, headers=headers)
    responce.raise_for_status()
    return responce.json()['id']


def get_count_clicks(token, shorted_url):
    bitlink_site_url = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(shorted_url)
    headers = {"Authorization" : "Bearer {}".format(token)}
    payload = {'unit':'month',
    'units': '-1' }
    responce = requests.get(bitlink_site_url, params=payload, headers=headers)
    responce.raise_for_status()
    return responce.json()['total_clicks']


def main():
    parser = argparse.ArgumentParser(description="For create short link from your url")
    parser.add_argument('url', help='Url should be here')
    args = parser.parse_args()
    if args.url: 
        load_dotenv()
        global BITLY_TOKEN
        BITLY_TOKEN = os.getenv("BITLY_TOKEN")
        if args.url.startswith('bit.ly'):
            print('Count clicks:', get_count_clicks(BITLY_TOKEN, args.url))
        else:
            print('Bitlink', get_shorten_link(BITLY_TOKEN, args.url))
    
              
if __name__=="__main__":
    main()    
              
              
              
              
              