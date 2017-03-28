import urllib2

for line in urllib2.urlopen('http://www.baidu.com'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    print line
