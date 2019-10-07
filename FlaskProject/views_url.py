"""
flask当中，可以直接创建应用，进行开发，而django是现有项目，再创建应用，但是在工作当中flask
也会遇到多应用问题，也需要有项目框架，只不过这个框架被称为 蓝图（blueprint）
"""

from flask import Flask
from flask import render_template
import datetime


#创建一个应用
app = Flask(__name__)

@app.route("/") #路由
def index(): #视图
    return "hello world"

@app.route("/index/")
def base():
    return render_template("index.html")

@app.route("/userinfo/")
def userinfo():
    return render_template("userinfo.html")


@app.route("/birthday/<username>/<month>/<day>/")
def birthday(username,month,day):
    month=int(month)
    day=int(day)
    day_number=datetime.datetime.now().strftime("j")
    return "%s的生日,是今年的%s天"%(username,day_number)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True) #启动这个应用

