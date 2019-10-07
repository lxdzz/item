from app import models

class BaseModel(models.Model):
    __abstract__ = True #声明当前类是抽象类，被继承调用不被创建
    id = models.Column(models.Integer,primary_key = True,autoincrement=True)
    def save(self):
        db = models.session()
        db.add(self)
        db.commit()
    def delete(self):
        db = models.session()
        db.delete(self)
        db.commit()

#定义表
class Curriculum(BaseModel):
    __tablename__ = "curriculum"
    c_id = models.Column(models.String(32))
    c_name = models.Column(models.String(32))
    c_time = models.Column(models.Date)

class User(BaseModel):
    __tablename__="user"
    user_name=models.Column(models.String(32))
    user_email=models.Column(models.String(32))
    user_password=models.Column(models.String(32))

class Leave(BaseModel):
    """
    请假  0
    批准  1
    驳回  2
    销假  3
    """
    __tablename__="leave"
    leave_id=models.Column(models.Integer) #请假人id
    leave_name=models.Column(models.String(32)) #请假人姓名
    leave_type=models.Column(models.String(32)) #假期类型
    leave_start_time=models.Column(models.String(32)) #起始时间
    leave_end_time=models.Column(models.String(32)) #结束时间
    leave_description=models.Column(models.Text) #请假事由
    leave_phone=models.Column(models.String(32)) #联系方式
    leave_status=models.Column(models.String(32)) #请假状态

class Picture(BaseModel):
    name=models.Column(models.String(32))
    picture=models.Column(models.String(32))