import requests
from bs4 import BeautifulSoup

for i in range(10000):
    response = requests.get(f"http://www.macausports.com.mo/news/show_{i}.html")
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all("div", class_="news-item")

    for j in result:
        a = j.getText()
        if ("尤啓樂" in a) or ("尤啟樂" in a):
            print(a, i)