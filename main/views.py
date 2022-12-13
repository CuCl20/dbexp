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
    print(results)
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
    print(all(element))
    if any(element):
        for x in range(len(element)):
            if element[x] == '':
                element[x] = 'null'
            else:
                element[x] = f"'{element[x]}'"
        results = funcs.seek_order(element)
    else:
        results = funcs.seek_all_order()
    return render(request, 'main.html', locals())
    # 将数据返回到网页中


def display_add(request):
    id = request.POST.get("id")
    phone = request.POST.get("phone")
    pay_method = int(request.POST.get("pay_method"))
    state = int(request.POST.get("state"))
    submit = datetime.date.today()
    check_in = datetime.datetime.strptime(request.POST.get("check_in"), "%Y-%m-%d").date()
    check_out = datetime.datetime.strptime(request.POST.get("check_out"), "%Y-%m-%d").date()
    rid = int(request.POST.get("rid"))
    funcs.add_order(id, phone, pay_method, state, submit, check_in, check_out, rid)
    return render(request, 'submit.html')


def update_order(request):
    return render(request, 'update_order.html')


def update_o(request):
    phone = request.POST.get("phone")
    check_in = datetime.datetime.strptime(request.POST.get("new_in"), "%Y-%m-%d").date()
    check_out = datetime.datetime.strptime(request.POST.get("new_out"), "%Y-%m-%d").date()
    funcs.update_order_check(phone, check_in, check_out)
    return render(request, 'submit2.html')


def update_r(request):
    phone = request.POST.get("phone")
    old_id = int(request.POST.get("old_rid"))
    new_id = int(request.POST.get("new_rid"))
    funcs.change_room(phone, old_id, new_id)
    return render(request, 'submit3.html')


def delete_o(request):
    phone = request.POST.get("phone")
    funcs.delete_order(phone)
    return render(request, 'submit4.html')


def check_in_progress(request):
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    name = request.POST.get("name")
    sex = request.POST.get("sex")
    pay = request.POST.get("pay")
    if pay == '0':
        return render(request, 'checkin.html', {"error": "办理失败"})
    else:
        funcs.add_client(phone, email, name, sex)
        funcs.update_order_payment(phone)
        return render(request, 'checkin.html')
