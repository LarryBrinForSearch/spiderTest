#coding:utf-8
'''
Created on 2017��6��29��

@author: JKChen
'''
import bsddb
import os,sys,string

home = "db_home"
filename = 'newUrl.db'
filename2 = 'oldUrl.db'
filePath = os.getcwd()

'''
# 创建数据库环境
dbenv = bsddb.db.DBEnv()
# 打开数据库环境
dbenv.open(home, bsddb.db.DB_CREATE | bsddb.db.DB_INIT_MPOOL)
# 创建数据库对象
d = bsddb.db.DB(dbenv)
# 打开数据库, 这里的第二个参数就是指定使用什么数据访问方法
# btree是 bsddb.db.DB_BTREE， hash是bsddb.db.DB_HASH
# queu 是 bsddb.db.DB_QUEUE,  recno 是bsddb.db.DB_RECNO
d.open(filename, bsddb.db.DB_QUEUE, bsddb.db.DB_CREATE, 0666)
# 插入一条数据，注意queue和recno的key不能是字符串的，应该是数字
'''

class bdb_solve:
    def __init__(self):
        home = "db_home"
        filename = "url.db"
        try:
            # 创建home目录
            os.mkdir(home)
        except:
            pass
        # 创建数据库环境
        self.dbenv = bsddb.db.DBEnv()
        # 打开数据库环境
        self.dbenv.open(home, bsddb.db.DB_CREATE | bsddb.db.DB_INIT_MPOOL)
        
        self.bdbQueue = bsddb.db.DB(self.dbenv)
        self.bdbHash = bsddb.db.DB(self.dbenv)
        
    def createQueue(self):
        # queue必须要设置一个value的长度，它的value是定长的
        self.bdbQueue.set_re_len(180)
        self.bdbQueue.open(filename, bsddb.db.DB_QUEUE, bsddb.db.DB_CREATE, 0666)
        
        return self.bdbQueue
    
    def createHash(self):
        self.bdbHash.open(filename2, bsddb.db.DB_HASH, bsddb.db.DB_CREATE, 0666) 
        return self.bdbHash
    
    def close_db(self):
        try:
            self.bdbHash.close()
            self.bdbQueue.close()
            self.dbenv.close()
        except:
            pass
    
    