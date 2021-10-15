import requests
from bs4 import BeautifulSoup
import csv

def parse_univ(url):
    newheaders = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64)'
    }
    page1 = requests.get(url, headers = newheaders) # change headers or get blocked
    soup = BeautifulSoup(page1.text, features="lxml")
    # rankings = soup.find(id="rankings").find_all("ol")[0].find_all("li")[0]
    rankings = soup.select("#rankings > ol > li > section")
    info = []

    for uni in rankings:
        uni_info = {};
        uni_info["name"] = uni.find("h2").get_text()
        uni_info["info"] = uni.find("h2").find("a").get("href")
        uni_info["country"] = uni.select("p > span")[0].get_text()
        uni_info["location"] = uni.select("p > span")[2].get_text()
        uni_info["rank"] = uni.find("strong").get_text()[1: len(uni.find("strong").get_text())]
        if (len(uni.select("picture > source")) == 0):
            uni_info["img"] = "none"
        else:
            uni_info["img"] = uni.select("picture > source")[0].get("srcset")
        uni_info["num_stu"] = uni.select("dd")[1].get_text()
        info.append(uni_info)
    # print(rankings[0].find("h2").get_text())
    # print(rankings[0].find("h2").find("a").get("href"))
    # print(rankings[0].select("p > span")[0].get_text())
    # print(rankings[0].select("p > span")[2].get_text())
    # print(rankings[0].find("strong").get_text())
    # print(rankings[0].select("picture > source")[0].get("srcset"))
    # print(rankings[0].select("dd")[1].get_text())

    return info

baseurl = 'https://www.usnews.com/education/best-global-universities/rankings?page='
all_uni_info = []

for p in range(1, 151): #151
    all_uni_info.extend(parse_univ(baseurl + str(p)))


with open("rank.csv", 'w', encoding="utf-8") as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = ["name", "info", "country", "location", "rank", "img", "num_stu"])

    # writing headers (field names)
    writer.writeheader()

    # writing data rows
    writer.writerows(all_uni_info)