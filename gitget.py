# ####################################################
# My first python program! :D
# It's a little script for download all repositories
# of a Github account
# ####################################################
# 	by Gabriel Nunes
# 	23/09/2014
# ####################################################

import urllib, os, re, time, sys

if len(sys.argv) < 2:
	sys.exit("Usage: gitget.py [github repo name]\n\nExample: gitget Google")
	
reponame = sys.argv[1];
downdir = 'gitget'

def download(filename, url):
	filedir = downdir + filename.replace(filename.split('/')[-1], "")
	if not os.path.isdir(filedir):
		os.makedirs(filedir)
	urllib.urlretrieve (url, downdir + filename)
	time.sleep(0.5)
	
p = re.compile('\<h3 class=\"repo-list-name\"\>(.*?)\</h3\>')
s = urllib.urlopen("https://github.com/%s?tab=repositories" % reponame).read().replace('\n', '')
s = str(p.findall(s)).strip('[]')
p = re.compile('href=\"(.*?)\"')
p = p.findall(s)

if len(p) < 1:
	sys.exit("Sorry, invalid repository.")
	
print "%s repositories found. Starting downloads:\n" % (len(p))
for itm in p:
	item = itm
	if not item.startswith("/"):
		item = "/" + item
	name = "%s.zip" % (item)
	url = "https://github.com%s/archive/master.zip" % (item)
	print "Downloading %s... " % (name)
	download(name, url)

print "\nThanks for using!"