from django.shortcuts import render
from .models import Order, Client, Room  # 引用模板层中的类
from . import funcs
import logging
import datetime

logger = logging.getLogger(__name__)


# Create your views here.
# 主界面
def mainview(request):
    return render(request, 'main.html')


# 添加新订单
def addview(request):
    return render(request, 'add.html')


#
def display_order(request):
    id = request.GET.get("OID")
    print(id)
    if id is None:
        results = funcs.seek_all_order()
    else:
        results = funcs.seek_order(id)
    results = list(results)
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
    print(submit)
    print(check_in)
    funcs.add_order(id, phone, pay_method, state, submit, check_in, check_out, rid)
    return render(request, 'addorder.html')
