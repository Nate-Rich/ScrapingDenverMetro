import requests
from bs4 import BeautifulSoup as bs

page_to_scrape = requests.get("https://www.redrocksonline.com/events/?view=grid")
soup = bs(page_to_scrape.text, "html.parser")
artist = soup.findAll("h3", attrs={"class":"card-title"})
date = soup.findAll("div", attrs={"class":"date"})

for artist, date in zip(artist, date):
    print(artist.text + " - " + date.text)
#Location = Redrocks*