import requests
from bs4 import BeautifulSoup

def parse_univ(url):
    newheaders = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64)'
    }
    page1 = requests.get(url, headers = newheaders) # change headers or get blocked
    soup = BeautifulSoup(page1.text, features="lxml")
    # rankings = soup.find(id="rankings").find_all("ol")[0].find_all("li")[0]
    rankings = soup.select("#rankings > ol > li > section")

    print(rankings[0].find_all("p"))

baseurl = 'https://www.usnews.com/education/best-global-universities/rankings?page='

for p in range(1, 2): #151
    parse_univ(baseurl + str(p))