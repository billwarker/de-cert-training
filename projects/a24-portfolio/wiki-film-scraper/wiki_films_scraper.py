import pandas as pd
import requests as re
from bs4 import BeautifulSoup

wiki_films_url = 'https://en.wikipedia.org/wiki/List_of_A24_films'

page = re.get(url=wiki_films_url)
soup = BeautifulSoup(page.text, 'html.parser')

all_tables_data = []

for table in soup.find_all('table'):
    
    t_header = table.thead
    print(t_header)
    # t_header_names = [th.text for th in t_header.find_all('th')]

    # print(t_header_names)
