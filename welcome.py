import urllib.request
from bs4 import BeautifulSoup, SoupStrainer
import urllib
import re

def get_url_byte(url):
    output_url = urllib.request.urlopen(url)
    return (len(output_url.read()))

def getLinks(url):
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page, "html.parser")
    links = []

    for link in soup.findAll('a'):
        links.append(link.get('href'))
        linkstodomain = SoupStrainer('a', href=re.compile(url))

    return links

url = input("Enter url ")
print ("Total bytes =", get_url_byte(url))

print ("Total number of tags =",len(url))