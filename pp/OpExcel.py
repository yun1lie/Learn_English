import xlrd
from .OpDataBase import OpDataBase


class OpExcel:
    def __init__(self, filename):
        # filename 文件名。就是要打开的文件名称
        self.ex = xlrd.open_workbook(filename=filename)
        self.sh = self.ex.sheet_by_index(0)
        # 根据 sheet 名称获取 sheet

    def display(self):
        for i in range(self.sh.nrows):
            print(self.sh.row_values(i))

            # 我觉得在这生成一个操作数据库的对象，然后每个循环就往数据库中插入一个单词
            # print(self.sh.col_values(i))
            
    def Insert_into_database(self):

        # 先创建一个操作数据库对象
        eop = OpDataBase()
        print("zzzzzzzzzz")

        for i in range(self.sh.nrows):
            print("aaaaaaaa")
            print(self.sh.row_values(i))
            eop.insertWord(self.sh.row_values(i)[0], self.sh.row_values(i)[1])

        del eop



# if __name__ == "__main__":
#     # # 打开
#     # wb = xlrd.open_workbook('aaa.xlsx')
#     # print( 'sheet名称:', wb.sheet_names())
#     # print( 'sheet数量:', wb.nsheets)
#     # # 根据 sheet 索引获取 sheet
#     # sh = wb.sheet_by_index(0)
#     # # 根据 sheet 名称获取 sheet
#     # # sh = wb.sheet_by_name('test')
#     # print( u'sheet %s 有 %d 行' % (sh.name, sh.nrows))
#     # print( u'sheet %s 有 %d 列' % (sh.name, sh.ncols))
#     # # print('第二行内容:', sh.row_values(1))
#     # # print('第三列内容:', sh.col_values(2))
#     # # print('第二行第三列的值为:', sh.cell_value(1, 2))
#     # # print('第二行第三列值的类型为:', type(sh.cell_value(1, 2)))
#     # print("aaaa")

#     op = OpExcel("aaa.xlsx")
#     op.display()
#     op.Insert_into_database()
