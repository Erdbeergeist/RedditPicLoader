import urllib.request as ulib
import os
import os.path

def loadpic(url,name):
	picobj=ulib.urlopen(url)
	data = picobj.read()
	print("Downloading :"+url)
	pic = open(name,"wb")
	pic.write(data)
	print(name +" created")
	pic.close()

def createcfg():
	config = open("config.cfg","w")
	subredd = input("Enter the subreddit: \t")
	config.write("subreddit:"+subredd+"\n")


def readconf():
	config = open("config.cfg","r")
	subredd = ""
	for line in config:
		data = line.split(":")
		if data[0] == "subreddit":
			subredd = data[1][:-1]
			
	return subredd			
		
configfile = "config.cfg"

if os.path.isfile(configfile) and os.access(configfile, os.R_OK):
	print("Config File Found")
	
else:
	print("Config Filer either not found or unreadable")
	createcfg()

sred = readconf()
url = "http://www.reddit.com/r/" + sred+"?count=100"
u = ulib.urlopen(url)
html = str(u.read())
sstring = "http://imgur.com/"
slen = len(sstring)
while sstring in html:
	html=html[html.find(sstring)+slen:]
	picid = html[0:html.find('"')]
	loadpic("http://www.i.imgur.com/"+picid+".jpg",picid+".jpg")
	
