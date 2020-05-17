import urllib
import re

print " "
print " "
print "we will try to open a url, in order to get your public IP Address"
print " "

url = "http://checkip.dyndns.org"

print url

request = urllib.urlopen(url).read()

theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request)

print " "
print " "
print "your IP Address is: ",  theIP
print " "
print " "
