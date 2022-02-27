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

        ## 这一行可能导致一次输入两个我先把他给注释掉000
        # # 使用 execute()  方法执行 SQL 查询
        # cursor.execute(sql)
        try:
            cursor.execute(sql)  # 执行sql语句
            self.db.commit()
        except:
            self.db.rollback()  # 发生错误时回滚

    def print(self):
        print("aaa")
