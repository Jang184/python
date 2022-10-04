import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://jang184.github.io") # 제 블로그 주소 입니다 ㅎㅎ
soup = bs(page.text, "html.parser")

elements = soup.select("div.post-preview a > h2")

for index, element in enumerate(elements, 1):
    print(f"{index}번째 포스팅 제목 : {element.text}")