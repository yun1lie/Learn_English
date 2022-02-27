from pickle import GET

from flask import Flask, render_template, request

from pp.OpDataBase import OpDataBase
from pp.OpExcel import OpExcel

app = Flask(__name__)
# 开启flask的调试模式
app.debug = True


@app.route("/")
def helloWorld():

    # 显示首页index.html
    return render_template("index.html")


@app.route("/hello")
def hello():
    # hello world 页面用来测试
    # data = "hello world !!!!"
    op = OpDataBase()
    data = op.random_query()
    return render_template("helloworld.html", data=data)


# 插入单词
@app.route("/insert", methods=["GET", "POST"])
def ins():

    # 增加一开始判断请求语句，可以避免一上来就提交一个NONE
    if request.method == "POST":
        name = request.form.get("name")
        translate = request.form.get("translate")

        # 增加判断，如果表单内容为空则不上传到数据库中
        if name != None and translate != None:
            db = OpDataBase()
            db.insertWord(name, translate)
            print(name, translate)
            del db

        # 上传文件
        try:
            f = request.files["file"]  # 这里面放的参数应该是文件表单input 的name
            if f.filename.split(".")[-1] == "xlsx":  # 判断文件后缀名
                f.save(dst="temp.xlsx")  # dst 参数表示文件上传后的名称 f.filename 显示文件上传文件的名字
                f.close()  # 关闭f对象

                # 创建OpExcel类的对象，调用
                ope = OpExcel("temp.xlsx")
                # ope.display()
                ope.Insert_into_database()
                return "file upload successfully!"
            else:
                return "文件格式不符合要求"
        except:
            print("文件上传失败")

    return render_template("insert.html")


if __name__ == "__main__":
    app.run()
