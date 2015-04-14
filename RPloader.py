import urllib.request as ulib
import os
import os.path

def loadpic(url,name,savedir):
	picobj=ulib.urlopen(url)
	data = picobj.read()
	if not os.path.exists(savedir):
    		os.makedirs(savedir)	
	if not os.path.isfile(savedir+"/"+name):
		print("Downloading :"+url)
		pic = open(savedir+"/"+name,"wb")
		pic.write(data)
		print(name +" created")
		pic.close()
	else: print("File already exists")

def createcfg():
	config = open("config.cfg","w")
	subredd = input("Enter the subreddit: \t")
	config.write("subreddit:"+subredd+"\n")
	savedir = input("Enter the directory to save the pictures in: \t")
	config.write("ddir:"+savedir+"\n")


def readconf():
	config = open("config.cfg","r")
	condata = []
	for line in config:
		data = line.split(":")
		if data[0] == "subreddit":
			condata.append(data[1][:-1])
		if data[0] == "ddir":
			condata.append(data[1][:-1])
			
	return condata			
		
configfile = "config.cfg"

if os.path.isfile(configfile) and os.access(configfile, os.R_OK):
	print("Config File Found")
	
else:
	print("Config Filer either not found or unreadable")
	createcfg()

conf = readconf()
url = "http://www.reddit.com/r/" + conf[0]
u = ulib.urlopen(url)
html = str(u.read())
sstring = "http://imgur.com/"
slen = len(sstring)
while sstring in html:
	html=html[html.find(sstring)+slen:]
	picid = html[0:html.find('"')]
	loadpic("http://www.i.imgur.com/"+picid+".jpg",picid+".jpg",conf[1])
	
