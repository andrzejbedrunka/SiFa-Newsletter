#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import feedparser
import smtplib, ssl

file = open("Newsletter.txt","w")
hyperlink_format = '<li> <a href="{link}">{text}</a></li><br>'

#DGUV
file.write("<br>" + "\n")
file.write("<h2><center>DGUV</center></h2>")
file.write("\n")
file.write("<p>")

NewsFeed = feedparser.parse("https://www.dguv.de/de/index.xml.jsp")
for i in range(10):
    entry = NewsFeed.entries[i]
    file.write(hyperlink_format.format(link=entry.link, text=entry.title))
    file.write("\n")
file.write("</p>")

#BG Bau
file.write('\n')
file.write("<br>" + "\n")
s = requests.get("https://www.bgbau.de/")
soup = BeautifulSoup(s.content, 'html.parser')
file.write('<h2><center>BG BAU</center></h2>\n')
file.write("<p>")
file.write("\n")
for link in soup.find_all("a", "bgbaunews__list__img"):
    #file.write("Title: {}\n".format(link.get("title")))
    #file.write("Link: https://bgbau.de{}\n".format(link.get("href")))
    titel = link.get("title")
    linky = "https://bgbau.de" + link.get("href")
    file.write(hyperlink_format.format(link=linky, text=titel) +"\n")
file.write("</p>")


#Arbeitssicherheit.de
file.write('\n')
file.write("<br>" + "\n")
p = requests.get("https://www.arbeitssicherheit.de/")
soup = BeautifulSoup(p.content, "html.parser")
file.write('<h2><center>arbeitssicherheit.de</center></h2>\n')
file.write("<p>")
file.write("\n")
for link in soup.find_all("a", "button secondary arrow-left-btn btn-fixed-right large-btn", limit=5):
    titel = link.get("title")
    linky = "https://www.arbeitssicherheit.de" + link.get("href")
    file.write(hyperlink_format.format(link=linky, text=titel) +"\n")
    #file.write("Title: {}\n".format(link.get("title")))
    #file.write("Link: https://www.arbeitssicherheit.de/{}\n".format(link.get("href")))
file.write("</p>")

#IFA
file.write('\n')
file.write("<br>" + "\n")
q = requests.get("https://www.dguv.de/ifa/index.jsp")
soup = BeautifulSoup(q.content, "html.parser")
file.write('<h2><center>DGUV/IFA</center></h2>\n')
file.write("<p>")
file.write("\n")
for link in soup.find_all("a", "teaser-link"):
    titel = link.get("title")
    linky = "https://dguv.ifa.de/" + link.get("href")
    file.write(hyperlink_format.format(link=linky, text=titel) +"\n")
    #file.write("Title: {}\n".format(link.get("title")))
    #file.write("Link: https://dguv.ifa.de/{}\n".format(link.get("href")))
file.write("</p>")

#KAN
file.write('\n')
file.write("<br>" + "\n")
m = requests.get("https://www.kan.de/")
soup = BeautifulSoup(m.content, "html.parser")
file.write('<h2><center>Kommission Arbeitsschutz und Normung (KAN)</center></h2>\n')
file.write("<p>")
file.write("\n")
links = []
titles = []
for title in soup.find_all("h3", limit=4):
    titles.append(title.get_text())
for link in soup.find_all("a", class_="more", limit=4):
    links.append("https://www.kan.de" + link.get("href"))
for i in range(4):
    file.write(hyperlink_format.format(link=links[i], text=titles[i]) +"\n")
    #file.write(titles[i] +'\n')
    #file.write(links[i] +'\n')
file.write("</p>")

#sifa-news.de
file.write('\n')
file.write("<br>" + "\n")
n = requests.get("https://www.sifa-news.de/")
soup = BeautifulSoup(n.content, "html.parser")
file.write('<h2><center>sifanews</center></h2>\n')
file.write("<p>")
file.write("\n")
for link in soup.find_all("a", class_="btn"):
    x = link.get("aria-label")
    #file.write("Title:" + x[13:])
    #file.write("Link: https://www.sifa-news.de{}\n".format(link.get("href")))
    linky = "https://www.sifa-news.de" + link.get("href")
    titel = x[13:]
    file.write(hyperlink_format.format(link=linky, text=titel) +"\n")
file.write("</p>")

#BG RCI
file.write('\n')
file.write("<br>" + "\n")
t = requests.get("https://www.bgrci.de/presse-medien/aktuelle-meldungen")
soup = BeautifulSoup(t.content, "html.parser")
file.write('<h2><center>BGRCI</center></h2>\n')
file.write("<p>")
file.write("\n")
for link in soup.select("dt > a", limit=10):
    titel = link.get("title")
    linky = "https://www.bgrci.de" + link.get("href")
    file.write(hyperlink_format.format(link=linky, text=titel) +"\n")
    #file.write("Title: {}\n".format(link.get("title")))
    #file.write("Link: https://www.bgrci.de/{}\n".format(link.get("href")))
file.write("</p>")

#BG ETEM
file.write('\n')
file.write("<br>" + "\n")
#o = requests.get("https://www.bgetem.de/")
#soup = BeautifulSoup(o.content, "html.parser")
file.write('<h2><center>BG ETEM</center></h2>\n')
file.write("<p>")
file.write("\n")
#for link in soup.find_all("img", width="500"):
#    file.write("Title: {}\n".format(link.get("alt")))
#    file.write("Link: {}\n".format(link.get("src")))
NewsFeed = feedparser.parse("https://www.bgetem.de/presse-aktuelles/pressemeldungen/aktuelle-pressemeldungen/RSS")
for i in range(5):
    entry = NewsFeed.entries[i]
    #file.write("Title: " + entry.title +'\n')
    #file.write("Link: " + entry.link +'\n')
    file.write(hyperlink_format.format(link=entry.link, text=entry.title))
    file.write("\n")
file.write("</p>")

#BGHM
file.write('\n')
file.write("<br>" + "\n")
o = requests.get("https://www.bghm.de/bghm/presseservice/pressemeldungen")
soup = BeautifulSoup(o.content, "html.parser")
file.write("<h2><center>BGHM</center></h2>\n")
file.write("<p>")
file.write("\n")
for link in soup.select("h3 > a", limit=10):
    #file.write("Title: {}\n".format(link.get("title")))
    #file.write("Link: https://www.bghm.de{}\n".format(link.get("href")))
    titel = link.get("title")
    linky = "https://www.bghm.de" + link.get("href")
    file.write(hyperlink_format.format(link=linky, text=titel))
    file.write("\n")
file.write("</p>")

#BGW
file.write('\n')
file.write("<br>" + "\n")
file.write("<h2><center>BG W</center></h2>\n")
file.write("<p>")
file.write("\n")
NewsFeed = feedparser.parse("https://www.bgw-online.de/SiteGlobals/Functions/RSSFeed/DE/RSSNewsfeed/RSSNewsfeed.xml")
for i in range(5):
    entry = NewsFeed.entries[i]
    #file.write("Title: ")
    #file.write(entry.title)
    #file.write("\n")
    #file.write("Link: ")
    #file.write(entry.link)
    #file.write("\n")
    file.write(hyperlink_format.format(link=entry.link, text=entry.title))
    file.write("\n")
file.write("</p>")

#VBG
file.write('\n')
file.write("<br>" + "\n")
file.write("<h2><center>VBG</center></h2>\n")
file.write("<p>")
file.write("\n")
NewsFeed = feedparser.parse("http://www.vbg.de/SiteGlobals/Functions/RSSFeed/DE/RSS_Allgemein/RSSNewsfeed.xml?nn=3360")
for i in range(3):
    entry = NewsFeed.entries[i]
    #file.write("Title: ")
    #file.write(entry.title)
    #file.write("\n")
    #file.write("Link: ")
    #file.write(entry.link)
    #file.write("\n")
    file.write(hyperlink_format.format(link=entry.link, text=entry.title))
    file.write("\n")
file.write("</p>")


#BAUA
file.write('\n')
file.write("<br>" + "\n")
file.write("<h2><center>Baua</center></h2>\n")
file.write("<p>")
file.write("\n")
NewsFeed = feedparser.parse("https://www.baua.de/DE/Angebote/Aktuelles/RSS/BAuA-Aktuell-RSS-Feed.xml")
for i in range(5):
    entry = NewsFeed.entries[i]
    #file.write("Title: ")
    #file.write(entry.title)
    #file.write("\n")
    #file.write("Link: ")
    #file.write(entry.link)
    #file.write("\n")
    file.write(hyperlink_format.format(link=entry.link, text=entry.title))
    file.write("\n")
file.write("</p>")

#BG VERKEHR
file.write('\n')
file.write("<br>" + "\n")
a = requests.get("https://www.bg-verkehr.de/")
soup = BeautifulSoup(a.content, "html.parser")
file.write('<h2><center>BG-Verkehr</center></h2>\n')
file.write("<p>")
file.write("\n")
for link in soup.find_all(class_="slide-read-more"):
    linky = link.get("href")
    titel = link.get_text()
    #file.write("Link: {}\n".format(link.get("href")))
    #file.write("Title: {}\n".format(link.get_text()))
    file.write(hyperlink_format.format(link=linky, text=titel))
    file.write("\n")
file.write("</p>")

#KOMNET
file.write('\n')
file.write("<br>" + "\n")
b = requests.get("https://www.komnet.nrw.de/_sitetools/komnetrecherche/index.html")
soup = BeautifulSoup(b.content, "html.parser")
file.write('<h2><center>KOMNET.NRW</center></h2>\n')
file.write("<p>")
file.write("\n")
for link in soup.find_all(class_="cosa", limit=10):
    #file.write("Link: {}\n".format(link.get("href")))
    #file.write("Title: {}\n".format(link.get_text()))
    linky = link.get("href")
    titel = link.get_text()
    file.write(hyperlink_format.format(link=linky, text=titel))
    file.write("\n")
file.write("</p>")

#Regelrecht aktuell
file.write('\n')
file.write("<br>" + "\n")
c = requests.get('https://regelrechtaktuell.de/category/vorschriften-regelwerk/vorschriften-und-regelwerk-der-dguv/')
soup = BeautifulSoup(c.content, "html.parser")
file.write('<h2><center>Regelrecht Aktuell</center></h2>\n')
file.write("<p>")
file.write('\n')
for link in soup.find_all(rel="bookmark"):
    #file.write("Link: {}\n".format(link.get("href")))
    linky = link.get("href")
    titel = link.get_text()
    file.write(hyperlink_format.format(link=linky, text=titel))
    file.write("\n")
file.write("</p>")

file.write('\n')
file.close()
