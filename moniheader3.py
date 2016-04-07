import urllib
import urllib.request
import http.cookiejar
import gzip
import re


def makeMyOpener(head=None):
    if head is None:
        head = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        header = []
        for key, value in head.items():
            elem = (key, value)
            header.append(elem)
        opener.addheaders = header
        return opener


def save_file(data):
    save_path = "d:\\sbuu\\temp.html"
    f_obj = open(save_path, 'wb')
    f_obj.write(data)
    f_obj.close()


def ungzip(data):
    try:
        print('正在尝试解压....')
        data = gzip.decompress(data)
        print('解压完毕')
    except:
        print('无需解压')
    return data


def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags=0)
    strlist = cer.findall(data)
    return strlist[0]


oper = makeMyOpener()
uop = oper.open('http://www.zhihu.com', timeout=1000)
data = uop.read()
data = ungzip(data)
print(data.decode())

save_file(data)
