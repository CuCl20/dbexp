from django.db import models
import main


# Create your models here.
# 订单
class Order(models.Model):
    id = models.CharField(max_length=15, primary_key=True)  # 订单号
    phone = models.CharField(max_length=11)  # 电话号码
    pay_method = models.IntegerField()  # 付款方式
    state = models.IntegerField()  # 订单状态
    submit_date = models.DateTimeField()  # 订单提交时间
    check_in_date = models.DateTimeField()  # 入住时间
    check_out_date = models.DateTimeField()  # 退房时间
    rid = models.IntegerField()  # 房号

    def __str__(self):
        return self.id, self.phone, self.pay_method, self.state, self.submit_date, \
               self.check_in_date, self.check_out_date, self.rid


# 顾客
class Client(models.Model):
    phone = models.CharField(max_length=11, primary_key=True)  # 电话号码
    email = models.CharField(max_length=40)  # 电子邮箱
    name = models.CharField(max_length=6)  # 姓名
    sex = models.CharField(max_length=4)  # 性别

    def __str__(self):
        return self.phone, self.email, self.name, self.sex


# 房间
class Room(models.Model):
    id = models.IntegerField(primary_key=True)  # 房号
    kind = models.IntegerField()  # 房间类型
    state = models.BooleanField()  # 房间状态

    def __str__(self):
        return self.id, self.kind, self.state
