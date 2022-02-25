from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def helloWorld():

    # 显示首页index.html
    return render_template('index.html')

@app.route('/hello')
def hello():

    # hello world 页面用来测试
    return render_template('helloworld.html')


app.run()