from django.db import models
import main


# Create your models here.
# 订单
class Order(models.Model):
    id = models.CharField(max_length=15, primary_key=True)  # 订单号
    phone = models.CharField(max_length=11)  # 电话号码
    pay_method = models.IntegerField()  # 支付方式
    state = models.IntegerField()  # 订单状态
    submit_date = models.DateField()  # 订单提交时间
    check_in_date = models.DateField()  # 入住时间
    check_out_date = models.DateField()  # 退房时间
    rid = models.IntegerField()  # 房号

    def __str__(self):
        return self.id, self.phone, self.pay_method, self.state, self.submit_date, \
               self.check_in_date, self.check_out_date, self.rid


# 顾客
class Client(models.Model):
    phone = models.CharField(max_length=11, primary_key=True)  # 电话号码
    email = models.CharField(max_length=30)  # 电子邮件
    name = models.CharField(max_length=40)  # 姓名
    sex = models.CharField(max_length=4)  # 性别

    def __str__(self):
        return self.phone, self.email, self.name, self.sex


# 房间
class Room(models.Model):
    id = models.IntegerField(primary_key=True)  # 房号
    kind = models.IntegerField()  # 房间类型

    def __str__(self):
        return self.id, self.kind


# 房间状态
class State(models.Model):
    id = models.IntegerField(primary_key=True)  # 房号
    day1 = models.IntegerField()  # 今日
    day2 = models.IntegerField()  # 第二天
    day3 = models.IntegerField()  # 第三天
    day4 = models.IntegerField()  # 第四天
    day5 = models.IntegerField()  # 第五天
    day6 = models.IntegerField()  # 第六天
    day7 = models.IntegerField()  # 第七天

    def __str__(self):
        return self.id, self.day1, self.day2, self.day3, self.day4, self.day5, self.day6, self.day7


# 管理员
class Admin(models.Model):
    id = models.IntegerField(primary_key=True)  # 编号
    password = models.CharField(max_length=20, default='0000')  # 密码
    last_log_time = models.DateField(default='2022-12-22')

    def __str__(self):
        return self.id, self.password, self.last_log_time
