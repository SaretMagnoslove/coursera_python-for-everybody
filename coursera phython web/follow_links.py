import urllib
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('enter main url: ')
count = int(input('enter count: ')) 
position = int(input('enter position: ')) -1

while count>=0:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print(url)
    url = tags[position].get('href', None)
    count = count - 1



