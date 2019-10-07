import datetime
from flask import Flask
from flask import render_template

#创建一个应用
app=Flask(__name__)

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
    def __init__(self,month="now"):
        self.result=[]

        big_month=[1,3,5,7,8,10,12]
        small_month=[4,6,9,11]

        #获取当前月
        now=datetime.datetime.now()
        if month=="now":
            month=now.month
            first_date=datetime.datetime(now.year,now.month,1,0,0)
            # 年 月 日 时 分
        else:
            # assert int(month) in range(1,13)
            first_date=datetime.datetime(now.year,month,1,0,0)

        if month in big_month:
            day_range=range(1,32) # 指定月份的总天数
        elif month in small_month:
            day_range=range(1,31)
        else:
            day_range=range(1,29)

        # 获取指定月天数
        self.day_range=list(day_range)
        first_week=first_date.weekday() # 获取指定月号是周几 (python中 6 代表星期日)

        linel=[] #第一行数据
        for e in range(first_week):
            linel.append("empty")
        for d in range(7-first_week):
            linel.append(
                str(str(self.day_range.pop(0))+"--django开发")
            )
        self.result.append(linel)
        while self.day_range: # 如果总天数列表有值,就接着循环
            line=[] # 每个子列表
            for i in range(7):
                if len(line)<7 and self.day_range:
                    line.append(str(self.day_range.pop(0))+"--django开发")
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
                day=day.center(6)
                print(day,end="  ")
            print()

@app.route("/") #路由
def index(): #视图
    return "hello world"

@app.route("/index/")
def base():
    return render_template("index.html")

@app.route("/userinfo/")
def userinfo():
    calendar=Calendar().return_month()
    now=datetime.datetime.now()
    return render_template("userinfo.html",**locals())

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True) #启动这个应用