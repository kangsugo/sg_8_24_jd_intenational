#coding:utf-8
import string
class Kang:
    def __init__(self,name):
        self.name = name

    def read_file(self):
        f = open(self.name)
        for line in f:
            self.parse(line)
        f.close()

    def parse(self,line):
        token = line.split('@')

        #两种情况
        #1.URL 包含list.jd.hk
        if token[2].find('list')==-1:
            # print "--------------开始-----------------"
            # print token[1]
            # print token[2]
            # print token[3].replace("\n", "").strip()+"不包含"
            page_num = string.atoi(token[3].replace("\n", "").strip())
            pos = token[2].find('&')
            i = 1
            while i <= page_num:
                url = token[2][:pos+1] + "page="+str(i)
                with open("good_url.txt","a") as ff:
                    ff.write(token[1]+"  "+url+'\n')
                i = i + 1


        #2.URL为其他格式
        else:
            # print "---------------开始-----------------"
            # print token[1]
            # print token[2]
            # print token[3].replace("\n", "").strip() + "包含"


            page_num = string.atoi(token[3].replace("\n", "").strip())
            pos = token[2].find('&')
            i = 1
            while i <= page_num:
                url = token[2][:pos+1] + "page="+str(i)
                with open("good_url.txt", "a") as ff:
                    ff.write(token[1]+"  "+url+'\n')
                i = i + 1








k = Kang('goods_page_num.txt')
k.read_file()

