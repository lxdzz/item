import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_wtf import CSRFProtect #导入csrf保护
from flask_restful import Api
from flask_migrate import Migrate

pymysql.install_as_MySQLdb()

app=Flask(__name__) #实例化app
app.config.from_pyfile("settings.py")
app.config.from_object("settings.Config") #来源于类对象
app.secret_key="655825"


models=SQLAlchemy(app)
# csrf=CSRFProtect(app) #使用csrf保护
api=Api(app)
migrate=Migrate(app,models) #安装数据库管理插件