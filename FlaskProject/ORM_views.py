import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__) #实例化app

# 配置参数
BASE_DIR=os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(BASE_DIR,"ORM.sqlite") #数据库地址 sqlite
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True #请求结束后自动提交
app.config["SQLALCHEMY_RTACK_MODIFICATIONS"]=True # flask1版本之后,添加的选项,目的是跟踪修改

#orm关联应用
models=SQLAlchemy(app)

# 定义表
class Curriculum(models.Model):
    __tablename__="curriculum"
    id=models.Column(models.Integer,primary_key=True)
    c_id=models.Column(models.String(32))
    c_name=models.Column(models.String(32))
    c_time=models.Column(models.Date)
# models.create_all()

# 增加数据
import datetime

session=models.session() #创建操作数据库的会话


# c2=Curriculum(c_id="003",c_name="html",c_time=datetime.datetime.now())
# c3=Curriculum(c_id="004",c_name="html",c_time=datetime.datetime.now())
# c4=Curriculum(c_id="005",c_name="html",c_time=datetime.datetime.now())
# c5=Curriculum(c_id="006",c_name="html",c_time=datetime.datetime.now())
#
# session.add_all([c2,c3,c4,c5])
# session.commit()

#查询所有数据
# all_c=Curriculum.query.all()
# for c in all_c:
    # print(c.id,c.c_name)

#条件查询
# all_c=Curriculum.query.filter_by(c_id="001") #返回列表对象
# for c in all_c:
#     print(c.id,c.c_name)

# 查询一条
# c=Curriculum.query.get(5) #返回列表对象
# print(c)
# print(c.id,c.c_name)

# c=Curriculum.query.first()
# print(c.id,c.c_name)

#排序
# all_c=Curriculum.query.order_by("id")
# all_c=Curriculum.query.order_by(models.desc("id")) #倒叙
#
# for c in all_c:
#     print(c.id,c.c_name)

# all_c=Curriculum.query.offset(0).limit(2).all()
    #offset 偏移,在这里指的是查询的起始位置
    #limit  具体查询的数量
# select * from curriculum limit 0,2 # 效果和上述句子效果相同  从0号索引开始,查询两条
# for c in all_c:
#     print(c.id,c.c_name)

#删除数据
# c = Curriculum.query.get(4)
# print(c)
# session.delete(c)
# session.commit()
#修改数据
c = Curriculum.query.get(3)
c.c_name = "MySQL"
session.add(c)
session.commit()

#创建表（同步）
#models.create_all()











