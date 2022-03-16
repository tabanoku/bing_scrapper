import threading
from pprint import pprint

import requests
from bs4 import BeautifulSoup

array = ("filetype%3Apdf+test", "enthec")

user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
}

def _scrapper(term: str):
    bing_url = f"https://www.bing.com/search?q={term}"
    
    response = requests.get(bing_url, headers=user_agent)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    result_block = soup.select("li.b_algo > h2 > a")

    print(f"{term}:")
    pprint([i.get_text() for i in result_block] )
    pprint([i.get_attribute_list("href") for i in result_block])

for search_item in array:
    _scrapper(search_item)
