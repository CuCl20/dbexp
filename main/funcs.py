import pymysql
import datetime


def add_client(phone, email, name, sex, rid):  # 增加旅客信息
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_client(phone, email, name, sex, rid) values('%s','%s','%s','%s',%d)" % \
              (phone, email, name, sex, rid)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_order(id, phone, pay_method, state, submit_date, check_in_date, check_out_date):  # 增加订单信息
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_order(id, phone, pay_method, state, submit_date, check_in_date, check_out_date) " \
              "values('%s','%s',%d,%d,'%s','%s','%s')" % (id, phone, pay_method, state, submit_date, check_in_date,
                                                          check_out_date)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_room(id, kind, state):  # 增加房间信息
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_room(id, kind, state) values(%d,%d,%d)" % (id, kind, state)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def seek_client(thephone):  # 按电话寻找旅客
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select name,sex,phone,email,id,check_in_date,check_out_date from" \
              "main_order left join main_client on main_order.phone = main_client.phone where phone='%d'" % thephone
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            name = row[0]
            sex = row[1]
            phone = row[2]
            email = row[3]
            id = row[4]
            check_in_date = row[5]
            check_out_date = row[6]
            print(name, sex, phone, email, id, check_in_date, check_out_date)
        db.close()
    except:
        print("Error:unable to fetch data")


def seek_room():  # 查询房间余量
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select kind,count(id) as num from" \
              " main_room where state = 1 group by kind order by kind"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            kind = row[0]
            num = row[1]
            print(kind, num)
        db.close()
    except:
        print("Error:unable to fetch data")


def seek_order(theid):  # 查找订单
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select phone,id,state,pay_method,submit_date,check_in_date,check_out_date from" \
              " main_order where id='%d'" % theid
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            phone = row[0]
            id = row[1]
            state = row[2]
            pay_method = row[3]
            submit_date = row[4]
            check_in_date = row[5]
            check_out_date = row[6]
            print(phone, id, state, pay_method, submit_date, check_in_date, check_out_date)
        db.close()
    except:
        print("Error:unable to fetch data")


def update_order_check(phone, new_check_in, new_check_out):  # 修改订单时间
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        now_time = datetime.datetime.now()
        sql = "update main_order set check_in_date='%s',check_out_date='%s'" \
              ",submit_date='%s' where phone='%s'" % (new_check_in, new_check_out, now_time, phone)
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        print("Error:unable to update date")


def change_room_state(rid, state):  # 换房
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "update main_room set state = %d where id = %d" % (state, rid)
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        print("Error:unable to change room state")


def change_room(phone, old_rid, new_rid):  # 换房
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "update main_client set rid = %d where phone='%s'" % (new_rid, phone)
        cursor.execute(sql)
        db.commit()
        change_room_state(old_rid, 0)
        change_room_state(new_rid, 1)
        db.close()
    except:
        print("Error:unable to change rooms")


def update_order_payment(phone):  # 订单付款
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        now_time = datetime.datetime.now()
        sql = "update main_order set state = 1 where phone='%s'" % phone
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        print("Error:unable to update pay state")

