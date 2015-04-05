#coding=utf8
__author__ = 'cheng'
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

filename = sys.argv[1]
from goose import Goose
from goose.text import StopWordsChinese
g = Goose({'stopwords_class': StopWordsChinese})
from HTMLParser import HTMLParser
import os

rootpath = '../data/raw'
hparser = HTMLParser()
files = os.listdir(rootpath)
outfile = open('../data/'+filename+'.raw.txt','w')
fin = open(rootpath+'/'+filename)
htmlstr = ''
inpool = False
count = 1
while True:
    count +=1
    line = fin.readline()
    if line.strip().lower() == '<doc>':
        print 1,count
        inpool = True
        htmlstr=''
        continue
    if line.strip().lower() == '</doc>':
        print 2,count
        inpool = False
        try:
            print 'begin extracting...'
            article = g.extract(raw_html=htmlstr.encode('utf8'))
            print 'finish extracting...,writing to file'
            outfile.write(article.cleaned_text[:].replace('\n','')+'\n')
            print filename,count
        except:
            print 'Exception'
            pass
            continue
    if inpool == True:
        print 3,count
        htmlstr += line.decode('gbk','ignore')

    if not line:
        print 4,count
        break