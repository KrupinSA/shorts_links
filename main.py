import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse
import os


def get_shorten_link(token, url):
    """
    Requests and returns a short link
    """
    bitlink_site_url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {f"Authorization": "Bearer {token}"}
    payload = {"long_url": url}
    response = requests.post(bitlink_site_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['id']


def get_count_clicks(token, shorted_url):
    """
    Returns the number of requests for this short link
    """
    bitlink_site_url = f"https://api-ssl.bitly.com/v4/bitlinks/{shorted_url}/clicks/summary"
    headers = {f"Authorization": "Bearer {token}"}
    payload = {
        'unit': 'month',
        'units': '-1',
    }
    response = requests.get(bitlink_site_url, params=payload, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def main():
    parser = argparse.ArgumentParser(description="For create short link from your url")
    parser.add_argument('url', help='Url should be here')
    args = parser.parse_args()
    load_dotenv()
    bitly_token = os.getenv("BITLY_TOKEN")
    parsed_url = urlparse(args.url)
    try:
        print('Count clicks:', get_count_clicks(bitly_token, f'{parsed_url.netloc}{parsed_url.path}'))
    except requests.exceptions.HTTPError:
        try:
            print('Bitlink', get_shorten_link(bitly_token, args.url))
        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError(f'{args.url} incorrect url')
              
if __name__=="__main__":
    main()    
              
              
              
              
              