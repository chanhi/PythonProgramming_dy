from bs4 import BeautifulSoup as bs
import requests

url = "https://n.news.naver.com/mnews/article/009/0005130138?sid=103"

result = requests.get(url)
soup = bs(result.text, "html.parser")
title = soup.find("div", {"id":"ct"}).find("div", {"class":"media_end_head_title"})
title2 = soup.select_one("#ct").select_one(".media_end_head_title").get_text()
print(title2)