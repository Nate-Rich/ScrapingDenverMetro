import requests
from bs4 import BeautifulSoup as bs

page_to_scrape = requests.get("https://www.fillmoreauditorium.org/events/")
soup = bs(page_to_scrape.text, "html.parser")
artist = soup.findAll("div", attrs={"class":"em-entry-main"})
date = soup.findAll("time", attrs={"class":"em-entry-time"})

for artist, date in zip(artist, date):
    print(artist.text + " - " + date.text)
#Location =Fillmore Auditorium