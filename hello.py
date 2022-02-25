from flask import Flask, render_template

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
@app.route('/insert')
def ins():
    return  render_template('insert.html')


app.run()