from bs4 import BeautifulSoup
import imgkit
import requests

def removeFluff(fluff):
    quote =""
    x = fluff.find("―")
    for i in range(0,x,1):
        quote += fluff[i]
    return quote

file = open("quotes.txt","a")

page = "16"
url = "https://www.goodreads.com/quotes/tag/mindfulness?page=" + page
r = requests.get(url)
html = r.text

soup = BeautifulSoup(html,features="html.parser")
large_fluffs = soup.find_all("div", attrs = {"class" : "quoteText"})
print(len(large_fluffs))
for q in large_fluffs:
    f = q.text
    f = str(f).strip()
    quo = removeFluff(f)
    
    if len(quo) < 220:
        file.write(quo + "\n")
    
file.close()
print("done")
