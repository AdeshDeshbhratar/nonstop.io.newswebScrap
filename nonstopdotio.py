import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sys
import time

# url = "https://indianexpress.com/section/cities/"
# r = requests.get(url)
# print(r.status_code)

pages = 1
upFrame = []

for i in range(1,pages+1):
    print("Processing Page:",i)
    url = "https://indianexpress.com/section/cities/page/{i}/"
    try: i = requests.get(url)
    except Exception as e:
        error_type, error_obj,error_info = sys.exc_info()
        print("Error For Link:",url)
        print(error_type,"line",error_info.tblineno)
        continue
    time.sleep(2)

    soup = BeautifulSoup(i.content,"html5lib")
    frame = []
    links = soup.find_all("div",class_ ="nation")
    print(len(links))

    filename = "IE_news.csv"
    f = open(filename, "w")
    headers = "Statement, link \n"
    f.write(headers)

    for j in links:

        Statement = j.find("h2",class_ ="title").find("a").text
        link = j.find("h2",class_ ="title").find("a")["href"].strip()

        frame.append((Statement,link))
        f.write(Statement.replace(",","^")+","+link.replace(",","^"))

    upFrame.extend(frame)

f.close

data = pd.DataFrame(upFrame,columns = ["Statement","link"])
print(data)

#________________Enhanced_code ____
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
#
# pages = 100  # Let's scrape 3 pages for example
# upFrame = []
#
# for i in range(1, pages + 1):
#     print("Processing Page:", i)
#     url = f"https://indianexpress.com/section/cities/page/{i}/"
#
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.content, "html.parser")
#         links = soup.find_all("div", class_="nation")
#
#         frame = []
#         for j in links:
#             statement = j.find("h2", class_="title").find("a").text
#             link = j.find("h2", class_="title").find("a")["href"].strip()
#             frame.append((statement, link))
#             upFrame.append((statement, link))
#
#         time.sleep(2)  # Add a small delay to avoid hitting the server too frequently
#
#     except Exception as e:
#         print("Error occurred:", e)
#         continue
#
# filename = "IE_news.csv"
# with open(filename, "w", encoding="utf-8") as f:
#     headers = "Statement,Link\n"
#     f.write(headers)
#     for statement, link in upFrame:
#         f.write(f"{statement.replace(',', '^')},{link}\n")
#
# data = pd.DataFrame(upFrame, columns=["Statement", "Link"])
# print(data)
