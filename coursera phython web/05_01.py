import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

url = input('enter url: ')
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)

counts = tree.findall('comments/comment/count')

total = 0

for count in counts:
    total += int(count.text)

print('total: ',total)
