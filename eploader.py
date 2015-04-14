import urllib.request as ulib

def loadpic(url,name):
	picobj=ulib.urlopen(url)
	data = picobj.read()
	print("Downloading :"+url)
	pic = open(name,"wb")
	pic.write(data)
	print(name +" created")
	pic.close()

url = "http://www.reddit.com/r/earthporn"
u = ulib.urlopen(url)
html = str(u.read())
sstring = "http://imgur.com/"
slen = len(sstring)
while sstring in html:
	html=html[html.find(sstring)+slen:]
	picid = html[0:html.find('"')]
	loadpic("http://www.i.imgur.com/"+picid+".jpg",picid+".jpg")
	
