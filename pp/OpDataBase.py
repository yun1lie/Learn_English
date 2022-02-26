import pymysql  # 导入pymysql库


class OpDataBase:
    def __init__(self) -> None:
        # 打开数据库链接
        self.db = pymysql.connect(
            host="localhost", user="root", password="root", db="le"
        )

    # 而且笔者发现不同版本，有的报错有的不报错。
    # 最后修改如下：
    # db=pymysql.connect(host='*******',user='root',password='123456',db='shuai')
    # 笔者猜测可能新旧版本之间有不同，没有指定参数造成了混乱。## 卑微异步
    # ————————————————
    # 版权声明：本文为CSDN博主「卑微异步」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    # 原文链接：https://blog.csdn.net/weixin_51712887/article/details/115430444

    # def __del__(self):
    #     # print('这是析构函数')
    #     # 关闭数据库链接
    #     self.db.close()

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
