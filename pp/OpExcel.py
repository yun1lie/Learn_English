import xlrd
from .OpDataBase import OpDataBase


class OpExcel:
    def __init__(self, filename):
        # filename 文件名。就是要打开的文件名称
        self.ex = xlrd.open_workbook(filename=filename)
        self.sh = self.ex.sheet_by_index(0)  # 根据 sheet 名称获取 sheet

    def display(self):
        """
        显示第一个sheet的所有内容
        """
        for i in range(self.sh.nrows):
            print(self.sh.row_values(i))

    def Insert_into_database(self):
        """
        将第一个sheet的所有内容插入到数据库中
        """
        # 先创建一个操作数据库对象
        eop = OpDataBase()

        try:
            # 按行将excel中读取出来的数据插入到数据库中
            for i in range(self.sh.nrows):
                print(self.sh.row_values(i))
                eop.insertWord(self.sh.row_values(i)[0], self.sh.row_values(i)[1])
        except:
            print("插入失败")
        del eop
