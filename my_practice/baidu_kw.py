import requests
#百度的关键词接口：
#http://www.baidu.com/s?wd=keyword
url = 'http://www.baidu.com/s'
keyworld = input('输入你要搜索的关键词：')
kv = {'wd':keyworld}
try:
    r = requests.get(url,params=kv)
    print(r.request.url)         #向百度发出请求的URL
    r.raise_for_status()
    print(len(r.text))
    print(r.text[:2000])
except:
    print("获取错误")