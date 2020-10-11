
import urllib.request, urllib.parse, urllib.error
import json
url =  'http://py4e-data.dr-chuck.net/comments_424041.json'
data = urllib.request.urlopen(url).read().decode()
print(len(data))
js = json.loads(data)
ks = js['comments']
y=0
for item in ks :
    x = item['count']
    y+= x
print(y)
    


    