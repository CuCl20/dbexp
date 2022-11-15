from django.shortcuts import render
from .models import Order, Client, Room   #引用模板层中的类

# Create your views here.
#主界面
def mainview(request):
    return render(request, 'main.html')
#添加新订单
def addview(request):
    return render(request, 'add.html')
#
def display_order(request):
    Order_list = Order.objects.all()  
    # 获取Order表中的全部内容
    return render(request, 'main.html', locals())  
    # 将数据返回到网页中