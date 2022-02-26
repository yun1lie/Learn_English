from pickle import GET

from flask import Flask, render_template, request

from pp.OpDataBase import OpDataBase

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
    return render_template("helloworld.html")


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

        # 上传文件
        try:

            f = request.files["file"]  # 这里面放的参数应该是文件表单input 的name
            # ['__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parse_content_type', 'close', 'content_length', 'content_type', 'filename', 'headers', 'mimetype', 'mimetype_params', 'name', 'save', 'stream']
            # 'close', 'content_length', 'content_type', 'filename', 'headers', 'mimetype', 'mimetype_params', 'name', 'save', 'stream']

            # f save
            # Save the file to a destination path or file object.  If the
            # destination is a file object you have to close it yourself after the
            # call.  The buffer size is the number of bytes held in memory during
            # the copy process.  It defaults to 16KB.

            # For secure file saving also have a look at :func:`secure_filename`.

            # :param dst: a filename, :class:`os.PathLike`, or open file
            #     object to write to.
            # :param buffer_size: Passed as the ``length`` parameter of
            #     :func:`shutil.copyfileobj`.

            # .. versionchanged:: 1.0
            #     Supports :mod:`pathlib`.

            # ## 测试用print
            # print("filename is >>")
            # print(f.filename)

            # # 获取文件的后缀名
            # filename = f.filename
            # fexten = filename.split(".")[-1]

            # # 只接受excel文件 ， 结尾为xlsx的文件
            # if fexten == "xlsx":
            #     f.save(dst="temp.xlsx")  # dst 参数表示文件上传后的名称 f.filename 显示文件上传文件的名字
            #     print("aaaaaaaa")
            #     f.close()  # 关闭f对象
            #     return "file uploaded successfully"
            # else:
            #     return "文件格式不符合要求"

            if f.filename.split(".")[-1] == "xlsx":  # 判断文件后缀名
                f.save(dst="temp.xlsx")  # dst 参数表示文件上传后的名称 f.filename 显示文件上传文件的名字
                f.close()  # 关闭f对象
                return "file upload successfully!"
            else:
                return "文件格式不符合要求"
        except:
            print("文件上传失败")

    return render_template("insert.html")


if __name__ == "__main__":
    app.run()
