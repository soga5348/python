from urllib import response
import feedparser
import requests

rdf_url = "https://www.youtube.com/feeds/videos.xml?channel_id=UCTyKZzmKi95wxmCg9rU-j6Q"
doument = feedparser.parse(rdf_url)

print(type(doument))

for entry in doument.entries:
    print(entry["title"])

count = 0
for entry in document.entries:
    url = entry["media_thumbnail"][0]["url"]
    response = requests.get(url)
    image = response.content


    file_name = "reiwanotora_" + str(count) + ".jpg"
    count +=1

with open(desktop/python_important/abcde.py,"wb") as image_file:
    image_file.write(image)
