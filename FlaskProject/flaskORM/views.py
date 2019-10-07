import datetime
import hashlib
import functools
import os

# from main import csrf
from flask import render_template
from main import app
from models import Curriculum
from flask import request
from flask import redirect
from models import *
from flask import session


class Calendar:
    """
    当前类实现日历功能
    1、返回列表嵌套列表的日历
    2、安装日历格式打印日历

    如果一号周一那么第一行1-7号   0
    如果一号周二那么第一行empty*1+1-6号  1
    如果一号周三那么第一行empty*2+1-5号  2
    如果一号周四那么第一行empty*3+1-4号  3
    如果一号周五那么第一行empyt*4+1-3号  4
    如果一号周六那么第一行empty*5+1-2号  5
    如果一号周日那么第一行empty*6+1号   6
    输入 1月
    得到1月1号是周几
    [] 填充7个元素 索引0对应周一
    返回列表
    day_range 1-30
    """

    def __init__(self, month="now"):
        self.result = []

        big_month = [1, 3, 5, 7, 8, 10, 12]
        small_month = [4, 6, 9, 11]

        # 获取当前月
        now = datetime.datetime.now()
        if month == "now":
            month = now.month
            first_date = datetime.datetime(now.year, now.month, 1, 0, 0)
            # 年 月 日 时 分
        else:
            # assert int(month) in range(1,13)
            first_date = datetime.datetime(now.year, month, 1, 0, 0)

        if month in big_month:
            day_range = range(1, 32)  # 指定月份的总天数
        elif month in small_month:
            day_range = range(1, 31)
        else:
            day_range = range(1, 29)

        # 获取指定月天数
        self.day_range = list(day_range)
        first_week = first_date.weekday()  # 获取指定月号是周几 (python中 6 代表星期日)

        linel = []  # 第一行数据
        for e in range(first_week):
            linel.append("empty")
        for d in range(7 - first_week):
            linel.append(
                str(str(self.day_range.pop(0)) + "--django开发")
            )
        self.result.append(linel)
        while self.day_range:  # 如果总天数列表有值,就接着循环
            line = []  # 每个子列表
            for i in range(7):
                if len(line) < 7 and self.day_range:
                    line.append(str(self.day_range.pop(0)) + "--django开发")
                else:
                    line.append("empty")
            self.result.append(line)

    def return_month(self):
        """
        返回嵌套列表的日历
        """
        return self.result

    def print_month(self):
        """
        安装日历格式打印日历
        """
        print("星期一  星期二  星期三  星期四  星期五  星期六  星期日")
        for line in self.result:
            for day in line:
                day = day.center(6)
                print(day, end="  ")
            print()


@app.route("/")  # 路由
def index():  # 视图
    return "hello world"


def setPassword(password):
    result = hashlib.md5(password.encode()).hexdigest()
    return result


def loginValid(fun):
    @functools.wraps(fun)  # 保留原函数的名称
    def inner(*args, **kwargs):
        username = request.cookies.get("username")
        id = request.cookies.get("id", "0")
        session_username = session.get("username")
        user = User.query.get(int(id))
        if user:  # 检测是否有对应的用户
            if user.user_name == username and username == session_username:  # 用户是否对应
                return fun(*args, **kwargs)
            else:
                return redirect("/login/")
        else:
            return redirect("/login/")

    return inner


@app.route("/logout/")
def logout():
    response = redirect("/login/")
    response.delete_cookie("username")
    response.delete_cookie("email")
    response.delete_cookie("id")
    # 下面两种方法任意取其一种
    session.pop("username")
    # del session["username"]
    return response


@app.route("/login/", methods=["GET", 'POST'])
# @csrf.exempt
def login():
    error = ""
    if request.method == "POST":
        form_data = request.form
        email = form_data.get("user_email")
        password = form_data.get("user_password")

        user = User.query.filter_by(user_email=email).first()
        if user:
            db_password = user.user_password
            if password == db_password:
                response = redirect("/index/")
                response.set_cookie("username", user.user_name)
                response.set_cookie("email", user.user_email)
                response.set_cookie("id", str(user.id))
                session["username"] = user.user_name
                return response
            else:
                error = "密码错误"
        else:
            error = "用户名不存在"
    return render_template("login.html", error=error)


@app.route("/register/", methods=["GET", "POST"])
def register():
    """
    form表单提交的数据有request.form接受
    """
    if request.method == "POST":
        user_name = request.form.get("user_name")
        user_password = request.form.get("user_password")
        user_email = request.form.get("user_email")
        user = User()
        user.user_name = user_name
        user.user_email = user_email
        user.user_password = user_password
        user.save()
    return render_template("register.html")


@app.route("/index/")
@loginValid
def exindex():
    # c=Curriculum()
    # c.c_id="004"
    # c.c_name='儿歌三百首'
    # c.c_time=datetime.datetime.now()
    # c.save()
    curr_list = Curriculum.query.all()
    return render_template("exindex.html", curr_list=curr_list)


@app.route("/userinfo/")
def userinfo():
    calendar = Calendar().return_month()
    now = datetime.datetime.now()
    return render_template("userinfo.html", **locals())

# from main import csrf

@app.route("/leave/", methods=["GET", "POST"])
# @csrf.exempt
def holiday_leave():
    if request.method == "POST":
        leave_name = request.form.get("leave_name")
        leave_type = request.form.get("leave_type")
        leave_start_time = request.form.get("leave_start_time")
        leave_end_time = request.form.get("leave_end_time")
        leave_phone = request.form.get("leave_phone")
        leave_description = request.form.get("leave_description")
        leave = Leave()
        leave.leave_id = request.cookies.get("id")
        leave.leave_name = leave_name
        leave.leave_type = leave_type  # 假期类型
        leave.leave_start_time = leave_start_time  # 起始时间
        leave.leave_end_time = leave_end_time  # 结束时间
        leave.leave_phone = leave_phone  # 联系电话
        leave.leave_description = leave_description  # 请假事由
        leave.leave_status = "0"  # 请假状态
        leave.save()
    return render_template("holiday_leave.html")


@app.route("/leave_list/<int:page>/")
@loginValid
def leave_list(page):
    leaves = Leave.query.all()
    pager=Pager(leaves,2)
    page_data=pager.page_data(page)
    return render_template("leave_list.html", **locals())


from flask import jsonify #flask封装后的json方法

# @app.route("/cancel/<int:id>/")
# def cancel(id):
#     leave=Leave.query.get(id)
#     leave.delete()
#     return jsonify({"data":"删除成功"})

@app.route("/cancel/",methods=["GET","POST"])
def cancel():
    data=request.args
    # data2=request.data
    # data3=request.form
    id=request.form.get("id") #通过args接受get请求数据
    leave=Leave.query.get(int(id))
    leave.delete()
    return jsonify({data:"删除成功"}) #返回json数据


class Pager:
    """
    flask 分页通过sqlalachemy 查询进行分页
    offset 偏移,开始查询的位置
    limit 单页条数
    分页器需要具备的功能
    页码
    分页数据
    是否第一页
    是否最后一页
    """
    def __init__(self,data,page_size):
        """

        :param data:要分页的数据
        :param page_size: 每页多少条
        """
        self.data=data #总数据
        self.page_size=page_size #单页数据
        self.is_start=False
        self.is_end=False
        self.page_count=len(data)
        self.next_page=0 #下一页
        self.previous_page=0 #上一页
        self.page_number=self.page_count/page_size
        #(data+page_size-1)//page_size
        if self.page_number==int(self.page_number):
            self.page_number=int(self.page_number)
        else:
            self.page_number=int(self.page_number)+1

        self.page_range=range(1,self.page_number+1) #页码范围
    def page_data(self,page):

        """
        返回分页数据
        :param page:页码
        page_size=10
        1   offect 0 limit(10)
        2   offect 10 limit(10)
        page_size=10
        1   start 0 end 10
        2   start 10 end 20
        3   start 20 end 30
        """
        self.next_page=int(page)+1
        self.previous_page=int(page)-1
        if page<=self.page_range[-1]:
            page_start=(page-1)*self.page_size
            page_end = page * self.page_size
            # data = self.data.offset(page_start).limit(self.page_size)
            data = self.data[page_start:page_end]
            if page == 1:
                self.is_start = True
            else:
                self.is_start = False
            if page == self.page_range[-1]:
                self.is_end = True
            else:
                self.is_end = False
        else:
            data = ["没有数据"]
        return data

from form import TaskForm

@app.route("/add_task/",methods=["GET","POST"])
def add_task():
    """
    print(task.errors) 表单校验错误
    print(task.validate_on_submit()) 判断是否是一个有效的post请求
    print(task.validate()) 判断是否是一个合法的post请求
    print(task.data) 提交的数据
    """
    errors=""
    task=TaskForm()
    if request.method=="POST":
        if task.validate_on_submit(): #判断是否是一个有效的POST请求
            fromData=task.data
        else:
            errors_list=list(task.errors.keys())
            errors=task.errors
            print(errors)
    return render_template("add_task.html",**locals())

from settings import STATICFILES_DIR
@app.route("/picture/",methods=["GET","POST"])
def picture():
    p={"picture":"img/"}
    if request.method=="POST":
        file=request.files.get("photo")
        file_name=file.filename
        file_path="img/%s"%file_name
        save_path=os.path.join(STATICFILES_DIR,file_path)
        file.save(save_path)
        p=Picture()
        p.picture=file_path
        p.save()
    return render_template("picture.html",p=p)

from main import api
from flask_restful import Resource
@api.resource("/Api/leave/")
class LeaveApi(Resource):
    def __init__(self):
        """
        定义返回的格式
        """
        super(LeaveApi,self).__init__()
        self.result={
            "version":"1.0",
            "data":""
        }
    def set_data(self,leave):
        """
        定义返回的数据
        """
        result_data={
            "leave_name":leave.leave_name,
            "leave_type":leave.leave_type,
            "leave_start_time":leave.leave_start_time,
            "leave_end_time":leave.leave_end_time,
            "leave_description":leave.leave_description,
            "leave_phone":leave.leave_phone,
        }
        return result_data
    def get(self):
        """
        处理get请求
        """
        data=request.args #获取请求的数据
        id=data.get("id") #获取id
        if id: #如果id存在,返回所有数据
            leave=Leave.query.get(int(id))
            result_data=self.set_data(leave)
        else: #如果id不存在,返回所有的数据
            leaves=Leave.query.all()
            result_data=[]
            for leave in leaves:
                result_data.append(self.set_data(leave))
        self.result["data"]=result_data
        return self.result
    def post(self):
        """
        这是post请求,负责保存数据
        """
        data=request.form
        leave_id=data.get("leave_id")
        leave_name=data.get("leave_name")
        leave_type=data.get("leave_type")
        leave_start_time=data.get("leave_start_time")
        leave_end_time=data.get("leave_end_time")
        leave_description=data.get("leave_description")
        leave_phone=data.get("leave_phone")

        leave=Leave()
        leave.leave_id=leave_id
        leave.leave_name=leave_name
        leave.leave_type=leave_type
        leave.leave_start_time=leave_start_time
        leave.leave_end_time=leave_end_time
        leave.leave_description=leave_description
        leave.leave_phone=leave_phone
        leave.leave_status="0"
        leave.save()

        self.result["data"]=self.set_data(leave)
        return self.result
    def put(self):
        """
        这是post请求,负责修改数据
        """
        #第一种方法
        data=request.form
        leave=Leave.query.get(id)

        leave_name=data.get("leave_name",leave.leave_name)
        leave_type=data.get("leave_type",leave.leave_type)
        leave_start_time=data.get("leave_start_time",leave.leave_start_time)
        leave_end_time=data.get("leave_end_time",leave.leave_end_time)
        leave_description=data.get("leave_description",leave.leave_description)
        leave_phone=data.get("leave_phone",leave.leave_phone)

        leave.leave_name=leave_name
        leave.leave_type=leave_type
        leave.leave_start_time=leave_start_time
        leave.leave_end_time=leave_end_time
        leave.leave_description=leave_description
        leave.leave_phone=leave_phone
        leave.save()
        self.result["data"]=self.set_data(leave)
        return self.result
        # 第二种方法
        # data=request.form #请求数据,类字典对象
        # id=data.get("id") #data里面的id
        # leave=Leave.query.get(int(id)) #在数据库里面找到
        # for key,value in data.items():
        #     if key!="id":
        #         setattr(leave,key,value)
        # leave.save()
        # self.result["data"]=self.set_data(leave)
        # return self.result
    def delete(self):
        """
        这是post请求,负责删除数据
        """
        data=request.form #请求数据,类字典对象
        id=data.get("id") #data里面的id
        leave=Leave.query.get(int(id))
        leave.delete()
        self.result["data"]="%s 删除成功"%id
        return self.result
