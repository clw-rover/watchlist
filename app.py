from flask import Flask
app=Flask(__name__)

from flask import url_for

@app.route('/')
def hello():
     return '<h1>march<h1>'

@app.route('/user/<name>')
def user_page(name):
     return 'output:%s'%name

@app.route('/test')
def test_url_for():
     print(url_for('hello'))
     print(url_for('user_page',name='jojo'))
     print(url_for('test_url_for'))
     print(url_for('test_url_for',num=3))
     return 'test page'