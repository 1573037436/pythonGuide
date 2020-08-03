import requests
import os
from bs4 import BeautifulSoup
import re


# 爬取具体每个新闻内容
def getNews(url, title):
    response = requests.get(url)
    response.encoding = 'utf-8'
##第一步:
#bs=BeautifulSoup(html,"lxml")
#这里注意第二个参数,解析器,
#解析器有很多种:lxml,html.parser,html5lib--最好的容错性(速度慢),xml
#一般用lxml,遇见奇葩网站用htnl5lib

    soup = BeautifulSoup(response.text, 'html.parser')
    folder = os.path.join(os.getcwd(), 'rubboHtml\\')  # 这里有个坑：python中字符串的最后一个字符是斜杠会导致出错。
    if not os.path.exists(folder):
        os.mkdir(folder)
    file_name = folder + title + '.html'
    # print(file_name)
    with open(file_name, 'w', encoding="utf-8") as file:
        file.write(title)
        file.write(soup.get_text())


# 获取各个新闻标题和链接
def getNews_title(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    tag = soup.find('div', class_='sidebar-box gallery-list')
    for tag in tag.find_all('a', attrs={"target": "_top"}):
        news_site = tag.get('href')
        news_site=news_site.replace('/python/','')
        news_site=url+news_site
        news_title = tag.get_text().strip()
        getNews(news_site, news_title)


# 运行程序
url = "https://www.runoob.com/python/"
getNews_title(url)