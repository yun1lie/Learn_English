from pickle import GET

from flask import Flask, render_template, request

app = Flask(__name__)
# 开启flask的调试模式
app.debug = True


@app.route('/')
def helloWorld():

    # 显示首页index.html
    return render_template('index.html')

@app.route('/hello')
def hello():

    # hello world 页面用来测试
    return render_template('helloworld.html')


# 插入单词
@app.route('/insert',methods=['GET', 'POST'])
def ins():

    # 增加一开始判断请求语句，可以避免一上来就提交一个NONE
    if request.method == 'POST':
        name = request.form.get('name')
        translate = request.form.get('translate')
        print(name, translate)
    return  render_template('insert.html')


app.run()
