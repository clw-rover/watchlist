from flask import Flask,url_for,render_template
app=Flask(__name__)

#define virtual data
v_name='jojo'
v_movies=[
     {'title':'bilibili','year':'2018'},
     {'title':'bilibili2','year':'2018'},
     {'title':'bilibili3','year':'2018'},
     {'title':'bilibili4','year':'2018'},
     {'title':'bilibili5','year':'2018'},
     ]

@app.route('/')
def index():
     return render_template('index.html',name=v_name,movies=v_movies)


'''
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
'''
