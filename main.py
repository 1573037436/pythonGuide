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
    if soup.find('div', class_='date-source') is None:
        return
    else:
        news_Date = soup.find('div', class_='date-source').span.string
        news_Source = soup.find('div', class_='date-source').a.string
        news_Content = soup.find('div', id='article').get_text()
        rep = re.compile("[\s+\.\!\/_,$%^*(+\"\']+|[+<>?、~*（）]+")
        title = rep.sub('', title)
        title = title.replace(':', '：')

    folder = os.path.join(os.getcwd(), 'news\\')  # 这里有个坑：python中字符串的最后一个字符是斜杠会导致出错。
    if not os.path.exists(folder):
        os.mkdir(folder)
    file_name = folder + title + '.txt'
    # print(file_name)
    with open(file_name, 'w', encoding="utf-8") as file:
        file.write(news_Date)
        file.write(news_Source)
        file.write(title)
        file.write(news_Content)


# 获取各个新闻标题和链接
def getNews_title(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    tag = soup.find('div', class_='ct_t_01')
    for tag in tag.find_all('a', attrs={"target": "_blank"}):
        news_site = tag.get('href')
        news_title = tag.get_text()
        getNews(news_site, news_title)


# 运行程序
url = "https://news.sina.com.cn/"
getNews_title(url)