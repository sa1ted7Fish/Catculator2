import pymysql

class DataGenerator:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            port=3306,
            database="catculator2",
            charset='utf8'
        )

        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def select(self, sql):

        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()

            return results
        except:
            return "Error: unable to fecth data"

    def insert(self, sql):
        try:
            relVal = self.cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
            return relVal
        except:
            # 发生错误时回滚
            self.conn.rollback()
            return "Error: unable to insert data"
