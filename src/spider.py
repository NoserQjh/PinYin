# coding=utf-8
# encoding=utf8

import urllib2

import requests

import config
from load import *

conf = config.Config()


def getUrl_multiTry(url):
    user_agent = '"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'
    headers = {'User-Agent': user_agent}
    maxTryNum = 20
    for tries in range(maxTryNum):
        try:
            req = urllib2.Request(url, headers=headers)
            z = urllib2.urlopen(req).read()
            break
        except:
            if tries < (maxTryNum - 1):
                continue
            else:
                break
    return z


if __name__ == '__main__':
    dataset = load_dataset(conf.dataset_path + '/spider')
    count = 0
    for x in dataset:
        count = count+len(x)
    file_name = conf.dataset_path + '/spider/%05d.txt' % count
    with open(unicode(file_name, "utf-8"), 'w+') as fr:
        for id in range(5500001, 5820000):
            if id % 10000 == 0:
                count = count + 1
                file_name = conf.dataset_path + '/spider/%5d.txt' % count
                open(unicode(file_name, "utf-8"), 'w+')
            url1 = "http://bbs.tianya.cn/post-free-"
            url2 = "-1.shtml"
            url = url1 + str(id) + url2
            code = requests.get(url).status_code
            if code == 200:
                z = unicode(getUrl_multiTry(url), "utf-8")
                z = re.sub(u'[　\r\n\s\t\xa0]', u'', z)
                content = re.findall(pattern=u'''bbs-contentclearfix">(.*?)<br></div''', string=z,
                                     flags=re.S)
                if len(content):
                    print>> fr, content[0].encode('GBK')
                print('Get page' + url)
