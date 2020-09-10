import requests
from bs4 import BeautifulSoup

url = "http://python123.io/ws/demo.html"

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print("解析前：")
    print(r.text)
    demo = r.text
    soup = BeautifulSoup(demo,"html.parser")  #html.parser为html解释器，用于解析demo
    print("解析后：")
    print(soup.prettify())   #打印解析后的内容
except:
    print("获取失败")



