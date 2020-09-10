import requests 

#图片的URL链接，需为.jpg格式
url = "https://desk-fd.zol-img.com.cn/t_s1680x1050c5/g5/M00/01/0F/\
ChMkJ1bKwoyIGan6AAXIXC3GU6gAALGpgNXMn0ABch0921.jpg"

#图片保存的路径及图片的名字
path = "D:/vscode/pictures/abc.jpg"
try:
    r = requests.get(url)
    r.raise_for_status()
    with open(path,'wb') as f:
        f.write(r.content)  #r.content表示返回内容的二进制形式
        f.close()
    print("获取成功")
except:
    print("获取失败")