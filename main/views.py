from django.shortcuts import render, redirect
from .models import Order, Client, Room  # 引用模板层中的类
from django.db import models
from . import funcs
import logging
import datetime
import pymysql

logger = logging.getLogger(__name__)


# Create your views here.
# 登陆界面
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    # 如果是POST请求，获取用户提交的数据
    username = int(request.POST.get("user"))
    password = request.POST.get("pwd")
    try:
        results = funcs.login(username)
        if results[0][0] == password:
            return redirect("/main/")
        else:
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})
    except:
        return render(request, "login.html", {"error_msg": "用户名或密码错误"})


def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    try:
        username = int(request.POST.get("user"))
        password = request.POST.get("pwd")
        funcs.register(username, password)
        return render(request, "login.html")
    except:
        return render(request, "register.html", {"error_msg": "注册失败"})


# 主界面
def mainview(request):
    return render(request, 'main.html', locals())


# 添加新订单
def addview(request):
    day1 = datetime.date.today()
    day2 = day1 + datetime.timedelta(days=1)
    day3 = day1 + datetime.timedelta(days=2)
    day4 = day1 + datetime.timedelta(days=3)
    day5 = day1 + datetime.timedelta(days=4)
    day6 = day1 + datetime.timedelta(days=5)
    day7 = day1 + datetime.timedelta(days=6)
    results = funcs.show_all_rooms()
    return render(request, 'add.html', locals())


#
def display_order(request):
    id = request.GET.get("OID")
    rid = request.GET.get("RID")
    phone = request.GET.get("PHO")
    state = request.GET.get("STA")
    method = request.GET.get("MET")
    submit_date = request.GET.get("SUB")
    in_date = request.GET.get("IND")
    out_date = request.GET.get("OUT")
    element = [id, rid, phone, state, method, submit_date, in_date, out_date]
    # print(all(element))
    if any(element):
        for x in range(len(element)):
            if element[x] == '':
                element[x] = 'null'
            else:
                element[x] = f"'{element[x]}'"
        result = funcs.seek_order(element)
        results = []
        for i in result:
            if i[2] == 1:
                temp = list(i)
                temp[2] = "云闪付"
                i = tuple(temp)
            if i[2] == 2:
                temp = list(i)
                temp[2] = "微信支付"
                i = tuple(temp)
            if i[2] == 3:
                temp = list(i)
                temp[2] = "支付宝"
                i = tuple(temp)
            if i[3] == 0:
                temp = list(i)
                temp[3] = "未支付"
                i = tuple(temp)
            if i[3] == 1:
                temp = list(i)
                temp[3] = "已支付"
                i = tuple(temp)
            results.append(i)
    else:
        result = funcs.seek_all_order()
        results = []
        for i in result:
            if i[2] == 1:
                temp = list(i)
                temp[2] = "云闪付"
                i = tuple(temp)
            if i[2] == 2:
                temp = list(i)
                temp[2] = "微信支付"
                i = tuple(temp)
            if i[2] == 3:
                temp = list(i)
                temp[2] = "支付宝"
                i = tuple(temp)
            if i[3] == 0:
                temp = list(i)
                temp[3] = "未支付"
                i = tuple(temp)
            if i[3] == 1:
                temp = list(i)
                temp[3] = "已支付"
                i = tuple(temp)
            results.append(i)
    return render(request, 'main.html', locals())
    # 将数据返回到网页中


def display_add(request):
    day1 = datetime.date.today()
    day2 = day1 + datetime.timedelta(days=1)
    day3 = day1 + datetime.timedelta(days=2)
    day4 = day1 + datetime.timedelta(days=3)
    day5 = day1 + datetime.timedelta(days=4)
    day6 = day1 + datetime.timedelta(days=5)
    day7 = day1 + datetime.timedelta(days=6)
    results = funcs.show_all_rooms()
    id = str(int(funcs.get_max_id()) + 1)

    if request.POST.get("rid") == '':
        error = "请输入房间"
        return render(request, 'add.html', locals())

    rid = int(request.POST.get("rid"))

    if funcs.if_room_exist(rid) == 0:
        error = "房间不存在"
        return render(request, 'add.html', locals())

    phone = request.POST.get("phone")

    if phone == '':
        error = "请输入电话号码"
        return render(request, 'add.html', locals())

    if len(phone) >= 12:
        error = "电话号码超过11位！"
        return render(request, 'add.html', locals())

    if not phone.isdigit():
        error = "电话号码应全是数字！"
        return render(request, 'add.html', locals())

    pay_method = int(request.POST.get("pay_method"))
    state = int(request.POST.get("state"))
    submit = datetime.date.today()

    if request.POST.get("check_in") == '' or request.POST.get("check_out") == '':
        error = "请输入日期！"
        return render(request, 'add.html', locals())

    check_in = datetime.datetime.strptime(request.POST.get("check_in"), "%Y-%m-%d").date()
    check_out = datetime.datetime.strptime(request.POST.get("check_out"), "%Y-%m-%d").date()

    if check_in >= check_out:
        error = "退房日期应在入住日期前！"
        return render(request, 'add.html', locals())

    if check_in < submit:
        error = "不能选择今日之前入住！"
        return render(request, 'add.html', locals())

    if check_out > submit + datetime.timedelta(days=7):
        error = "可选日期为7日之内！"
        return render(request, 'add.html', locals())

    if funcs.if_room_occupied(rid, check_in, check_out) == 1:
        error = "该房间在该时段已被预订！"
        return render(request, 'add.html', locals())

    funcs.add_order(id, phone, pay_method, state, submit, check_in, check_out, rid)
    return render(request, 'submit.html')


def update_order(request):
    return render(request, 'update_order.html')


def update_o(request):
    id = request.POST.get("id")

    if id == '':
        return render(request, 'update_order.html', {"error1": "请输入订单号！"})

    if not id.isdigit():
        return render(request, 'update_order.html', {"error1": "订单号应全是数字！"})

    id_t = funcs.if_order_exist(id)
    if id_t == 0:
        return render(request, 'update_order.html', {"error1": "查无此单！"})

    if request.POST.get("new_in") == '' or request.POST.get("new_out") == '':
        error1 = "请输入日期！"
        return render(request, 'update_order.html', locals())

    check_in = datetime.datetime.strptime(request.POST.get("new_in"), "%Y-%m-%d").date()
    check_out = datetime.datetime.strptime(request.POST.get("new_out"), "%Y-%m-%d").date()
    submit = datetime.date.today()

    if check_in >= check_out:
        error1 = "退房日期应在入住日期前！"
        return render(request, 'update_order.html', locals())

    if check_in < submit:
        error1 = "不能选择今日之前入住！"
        return render(request, 'update_order.html', locals())

    if check_out > submit + datetime.timedelta(days=7):
        error1 = "可选日期为7日之内！"
        return render(request, 'update_order.html', locals())

    rid = funcs.room_follow_id(id)
    if funcs.if_room_occupied_for_change(id, rid, check_in, check_out) == 1:
        error1 = "该房间在该时段已被预订！"
        return render(request, 'update_order.html', locals())

    funcs.update_order_check(id, check_in, check_out)
    return render(request, 'submit2.html')


def update_r(request):
    id = request.POST.get("id")
    if id == '':
        return render(request, 'update_order.html', {"error2": "请输入订单号！"})

    if not id.isdigit():
        return render(request, 'update_order.html', {"error2": "订单号应全是数字！"})

    id_t = funcs.if_order_exist(id)
    if id_t == 0:
        return render(request, 'update_order.html', {"error2": "查无此单！"})
    old_id = funcs.room_follow_id(id)

    if request.POST.get("new_rid") == '':
        return render(request, 'update_order.html', {"error2": "请输入房间号！"})
    new_id = int(request.POST.get("new_rid"))

    if funcs.if_room_exist(new_id) == 0:
        return render(request, 'update_order.html', {"error2": "此房间不存在！"})

    if funcs.if_room_occupied_for_r(id, new_id) == 1:
        return render(request, 'update_order.html', {"error2": "此房间已被占用！"})
    funcs.change_room(id, old_id, new_id)
    return render(request, 'submit3.html')


def delete_o(request):
    id = request.POST.get("id")
    if id == '':
        return render(request, 'update_order.html', {"error3": "请输入订单号！"})
    if not id.isdigit():
        return render(request, 'update_order.html', {"error3": "订单号应全是数字！"})
    funcs.delete_order(id)
    return render(request, 'submit4.html')


def check_in_progress(request):
    return render(request, 'checkin.html')


def check_in_p(request):
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    name = request.POST.get("name")
    sex = request.POST.get("sex")
    pay = request.POST.get("pay")
    if len(phone) >= 12:
        return render(request, 'checkin.html', {"error": "电话号码过长！"})
    if not phone.isdigit():
        return render(request, 'checkin.html', {"error": "请输入正确的电话号码！"})
    if not funcs.if_today_check(phone):
        return render(request, 'checkin.html', {"error": "订单不存在！"})
    if len(name) >= 41:
        return render(request, 'checkin.html', {"error": "姓名输入不合法！"})
    if len(sex) >= 7:
        return render(request, 'checkin.html', {"error": "性别输入不合法！"})
    if pay == '0':
        return render(request, 'checkin.html', {"error": "办理失败，未付款！"})
    funcs.add_client(phone, email, name, sex)
    funcs.update_order_payment(phone)
    return render(request, 'submit5.html')
