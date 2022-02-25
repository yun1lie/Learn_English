from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def helloWorld():
    return "hello world!"

@app.route('/hello')
def hello():
    return render_template('helloworld.html')


app.run()