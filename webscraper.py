from bs4 import BeautifulSoup
import requests

def scrapePosts():
    pass
    pageToScrape = requests.get("https://www.cnn.com/")
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    items = soup.findAll('span', attrs={'class':'container__headline-text'})
    # addresses = soup.findAll()
    
    for item in items:
        print(item.text)
        
scrapePosts()