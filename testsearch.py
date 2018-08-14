import MySQLdb
# 获取连接
class Mysqlsearch(object):
    def __init__(self):
        self.get_conn()

    def get_conn(self):
        #连接
        try:
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='',
                db='news',
                port=3306,
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print('Error:%s' % e)

    def close_conn(self):
        #关闭连接
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error:%s' % e)

    def get_one(self):
        sql = 'SELECT * FROM `news` WHERE `news_types`= %s ORDER BY `id` DESC;'
        #sql = 'select * from `news`;'
        cursor = self.conn.cursor()
        cursor.execute(sql,('百家', ))
        rest = dict(zip([k[0] for k in cursor.description],cursor.fetchone()))
        #print(cursor.description)
        cursor.close()
        self.close_conn()
        return rest

    def get_more(self,page,offet):
        pages = (page - 1) * offet#offet是每页个数 page第几页
        sql = 'select * from `news` where `news_types` = %s order by `id` desc limit %s,%s;'
        cursor = self.conn.cursor()
        cursor.execute(sql,('百家',pages,offet))
        rest = [dict(zip([k[0] for k in cursor.description],row))
                for row in cursor.fetchall()]
        cursor.close()
        self.close_conn()
        return rest

    def add_one(self):
        try:
            sql =("insert into `news`(`title`,`img_url`,`content`)value"
            "(%s,%s,%s);")
            cursor = self.conn.cursor()
            cursor.execute(sql,('a13','ab1','abc'))
            cursor.execute(sql, ('a13', 'ab1', 'abc','dd'))
            #提交事务保存没有这句ID增加但看不见
            self.conn.commit()
            cursor.close()

        except:
            print('error')
            #self.conn.rollback()#两条都不成功
            self.conn.commit()#一条成功 id不加
        self.close_conn()




if __name__ == '__main__':
    obj = Mysqlsearch()
    #rest = obj.get_one()
    #print(rest['title'])
    #rest = obj.get_more(1,5)
    #for item in rest:
        #print(item)
    obj.add_one()
