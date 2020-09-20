import requests
from bs4 import BeautifulSoup

# Debe de poder ser asada por el problema
qry = "corruption"

URL = "https://knowledgehub.transparency.org/search?q={}#".format(qry)

HTML_from_page = requests.get(URL)

soup = BeautifulSoup(HTML_from_page.content, "html.parser")

results = soup.find(id = "filterable-entries")

#Method 2:
card_Results = results.find_all('a', class_='knowledge-card')

for card in card_Results:    
    link = card['href']
    
    title_elem = card.find('h2', class_='heading heading--snippet')

    print(title_elem.text, "|", link)
    
    print()