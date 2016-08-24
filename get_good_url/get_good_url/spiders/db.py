#coding:utf-8
import MySQLdb
import string
import json

class kang:
    def __init__(self):
        self.num_list = []
        self.conn = MySQLdb.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = '123456',
            db = 'sugo',
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor()
        # print self.conn
        # print self.cursor

    #获取了各字段的值
    # ===========================================need to be changed===========================
    def process_raw_world(self,sku, name, div_name):
        sql = 'insert into jdguoji_goods_name_id values (%i,"%s","%s")' % (sku, name, div_name)
        if self.isResist(sku) == 0:
            print sql
            ret = self.cursor.execute(sql)
            self.conn.commit()
            if ret == 0:
                pass
            else:
                self.conn.commit()


    #负责关闭连接对象的游标
    def destr(self):

        self.cursor.close()
        self.conn.close()

    #判断该记录是否存在，存在返回1，不存在返回0
    # ===========================================need to be changed===========================
    def isResist(self,num):
        sql = "select * from jdguoji_goods_name_id where sku = %i"%num
        re = self.cursor.execute(sql)

        print re
        if re == 0:
            print "不存在"
            return 0
        else:
            print int(num)
            print "已经存在"
            return  1



