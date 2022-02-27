import pymysql  # 导入pymysql库


class OpDataBase:
    def __init__(self) -> None:
        # 打开数据库链接
        self.db = pymysql.connect(
            host="localhost", user="root", password="root", db="le"
        )

    def insertWord(self, name, translate):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()

        # sql 语句
        sql = "INSERT INTO `word` VALUES ('%s', '%s')" % (name, translate)
        # # 使用 execute()  方法执行 SQL 查询
        try:
            cursor.execute(sql)  # 执行sql语句
            self.db.commit()
        except:
            self.db.rollback()  # 发生错误时回滚

        cursor.close()

    def random_query(self):
        """
        从数据库中随机抽取一条数据
        """
        sql = "SELECT * FROM word ORDER BY rand() LIMIT 1"
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)  # 执行sql语句
            data = cursor.fetchall()[0]
            self.db.commit()
        except:
            self.db.rollback()  # 发生错误时回滚
        return data 

    def print(self):
        print("aaa")


# if __name__ == "__main__":
#     o = OpDataBase()
#     print("aaaaaa")
#     print(o.random_query())