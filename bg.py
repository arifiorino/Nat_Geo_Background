from urllib.request import urlretrieve
response = urlretrieve("http://photography.nationalgeographic.com/photo-of-the-day/#", "pic.html")
pic = open("pic.html", "r", encoding="utf8")
pic = str(pic.readlines())
count = 0
picurl = pic[pic.find("images.nationalgeographic.com"):]
picurl = picurl[:picurl.find("\"")]
print(picurl)
urlretrieve("http://"+picurl, "final.png")

