import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(html,ulist):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr.find_all('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])




def printUnivList(ulist,num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","省市"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))

if __name__ == "__main__":
    ulist = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming-zongbang-2020.html"
    html = getHTMLText(url)
    fillUnivList(html,ulist)
    printUnivList(ulist,20)