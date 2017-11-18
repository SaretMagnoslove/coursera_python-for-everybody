import urllib
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('enter-')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

total = []
spans = soup('span')
for span in spans:
    total.append(int(span.string))

print (sum(total))
