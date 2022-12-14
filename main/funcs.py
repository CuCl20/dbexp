import pymysql
import datetime


def register(id, password):  # 注册
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        today = datetime.date.today()
        sql = "insert into main_admin(id, password, last_log_time) values(%d,'%s','%s')" % \
              (id, password, today)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def login(id):  # 登录
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select password from main_admin where id=%d" % id
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
    except:
        print("error")


def find_log_time():
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select last_log_time from main_admin"
        cursor.execute(sql)
        results = cursor.fetchone()
        db.close()
        return results[0]
    except:
        print("error")


def update_log_time():
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        today = datetime.date.today()
        sql = "update main_admin set last_log_time = '%s'" % today
        cursor.execute(sql)
        db.commit()
    except:
        print("error")


def add_client(phone, email, name, sex):  # 增加旅客信息
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_client(phone, email, name, sex) values('%s','%s','%s','%s')" % \
              (phone, email, name, sex)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_order(id, phone, pay_method, state, submit_date, check_in_date, check_out_date, rid):  # 增加订单信息
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_order(id, phone, pay_method, state, submit_date, check_in_date, check_out_date, rid) " \
              "values('%s','%s',%d,%d,'%s','%s','%s',%d)" % (id, phone, pay_method, state, submit_date, check_in_date,
                                                             check_out_date, rid)
        cursor.execute(sql)
        db.commit()
        change_room_state(rid, check_in_date, check_out_date, 1)
        return True
    except Exception as e:
        print("error")
        return False


def add_room(id, kind):  # 增加房间信息
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_room(id, kind) values(%d,%d)" % (id, kind)
        cursor.execute(sql)
        db.commit()
        sql = "insert into main_state(id,day1,day2,day3,day4,day5,day6,day7)" \
              " values(%d,%d,%d,%d,%d,%d,%d,%d)" % (id, 0, 0, 0, 0, 0, 0, 0)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def seek_client(thephone):  # 按电话寻找旅客
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password=' ', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select name,sex,main_client.phone,email,check_in_date,check_out_date from" \
              " main_order join main_client on main_client.phone" \
              " where main_client.phone='%d'" % thephone
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            name = row[0]
            sex = row[1]
            phone = row[2]
            email = row[3]
            check_in_date = row[4]
            check_out_date = row[5]
            print(name, sex, phone, email, check_in_date, check_out_date)
        db.close()
    except:
        print("Error:unable to fetch data")


def seek_room():  # 查询房间余量
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password=' ', port=3306, db='datademo')
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


def seek_all_order():  # 显示所有订单
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select id,phone,pay_method,state,submit_date,check_in_date,check_out_date,rid from main_order " \
              "order by check_in_date"
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
    except:
        print("Error:unable to fetch data")


def seek_order(element):  # 查找订单
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select id,phone,pay_method,state,submit_date,check_in_date,check_out_date,rid from" \
              f" main_order where (id={element[0]} or {element[0]} is null) and" \
              f" (phone={element[2]} or {element[2]} is null) and (pay_method={element[4]} or {element[4]} is null) " \
              f"and (state={element[3]} or {element[3]} is null) and (submit_date={element[5]} or {element[5]} is " \
              f"null) and (check_in_date={element[6]} or {element[6]} is null) and (check_out_date={element[7]} or" \
              f" {element[7]} is null) and (rid={element[1]} or {element[1]} is null) order by check_in_date"
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
    except:
        print("Error:unable to fetch data")


def update_order_check(id, new_check_in, new_check_out):  # 修改订单时间
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        now_time = datetime.date.today()
        sql = "select phone,id,state,pay_method,submit_date,check_in_date,check_out_date,rid from" \
              " main_order where id='%s'" % id
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            check_in = row[5]
            check_out = row[6]
            rid = row[7]
            change_room_state(rid, check_in, check_out, 0)
            change_room_state(rid, new_check_in, new_check_out, 1)
        sql = "update main_order set check_in_date='%s',check_out_date='%s'" \
              ",submit_date='%s' where id='%s'" % (new_check_in, new_check_out, now_time, id)
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        print("Error:unable to update date")


def change_room_state(rid, check_in_date, check_out_date, come):  # 改变房间状态
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        now_time = datetime.date.today()
        start = (check_in_date - now_time).days
        finish = (check_out_date - now_time).days
        for i in range(start, finish):
            sql = "update main_state set day%d = %d where id = %d" % (i + 1, come, rid)
            cursor.execute(sql)
            db.commit()
        db.close()
    except:
        print("Error:unable to change room state")


def change_room(id, old_rid, new_rid):  # 换房&修改订单房间
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "update main_order set rid = %d where id='%s'" % (new_rid, id)
        cursor.execute(sql)
        db.commit()
        sql = "select check_in_date,check_out_date from main_order where id='%s'" % id
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            check_in = row[0]
            check_out = row[1]
            change_room_state(old_rid, check_in, check_out, 0)
            change_room_state(new_rid, check_in, check_out, 1)
        db.close()
    except:
        print("Error:unable to change rooms")


def update_order_payment(pay_method, phone):  # 订单付款
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "update main_order set pay_method = %d, state = 1 where phone='%s' and state = 0" % (pay_method, phone)
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        print("Error:unable to update pay state")


def show_all_rooms():
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select * from main_room natural join main_state where main_room.id = main_state.id"
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
        db.close()
        return results
    except:
        print("Error:unable to show all rooms")


def delete_order(id):  # 按订单号删除订单
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select check_in_date,check_out_date,rid from main_order where id='%s'" % id
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            check_in = row[0]
            check_out = row[1]
            rid = row[2]
            change_room_state(rid, check_in, check_out, 0)
        db.commit()
        sql = "delete from main_order where id='%s'" % id
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        print("Error:unable to delete order")


def update_time():  # 时间更新
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        for i in range(1, 6):
            sql = "update main_state set day%d = day%d" % (i, i + 1)
            cursor.execute(sql)
            db.commit()
        sql = "update main_state set day7 = 0"
        cursor.execute(sql)
        db.commit()
    except:
        print("Error:unable to update time")


def get_max_id():  # 获取最大订单号
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select max(id) from main_order"
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        if result[0] is None:
            return 0
        return result[0]
    except:
        result = 0
        return result


def if_room_exist(rid):  # 是否存在房间
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select id from main_room where id = %d" % rid
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        return result[0]
    except:
        result = 0
        return result


def if_order_exist(id):  # 是否存在订单
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select id from main_order where id = '%s'" % id
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        return result[0]
    except:
        result = 0
        return result


def if_room_occupied(rid, check_in, check_out):  # 房间是否占用
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select * from main_state where id = %d" % rid
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        start = (check_in - datetime.date.today()).days + 1
        finish = (check_out - datetime.date.today()).days + 1
        if_r = 0
        for i in range(start, finish):
            if result[i] == 1:
                print(i)
                if_r = 1
        return if_r
    except:
        print("error")


def if_room_occupied_for_change(id, rid, check_in, check_out):  # 换房状态for时间
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select * from main_state where id = %d" % rid
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        sql = "select check_in_date,check_out_date from main_order where id = '%s'" % id
        cursor.execute(sql)
        db.commit()
        result2 = cursor.fetchone()
        start = (check_in - datetime.date.today()).days + 1
        finish = (check_out - datetime.date.today()).days + 1
        start2 = (result2[0] - datetime.date.today()).days + 1
        finish2 = (result2[1] - datetime.date.today()).days + 1
        if_r = 0
        for i in range(start, finish):
            if result[i] == 1 and (i < start2 or i > finish2):
                if_r = 1
        return if_r
    except:
        print("error")


def if_room_occupied_for_r(id, rid):  # 换房状态for房间
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select * from main_state where id = %d" % rid
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        sql = "select check_in_date,check_out_date from main_order where id = '%s'" % id
        cursor.execute(sql)
        db.commit()
        result2 = cursor.fetchone()
        start2 = (result2[0] - datetime.date.today()).days + 1
        finish2 = (result2[1] - datetime.date.today()).days + 1
        if_r = 0
        for i in range(start2, finish2):
            if result[i] == 1:
                if_r = 1
        return if_r
    except:
        print("error")


def if_today_check(phone):  # 是否今天入住
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        come_day = datetime.date.today()
        sql = "select * from main_order where phone = '%s' and check_in_date = '%s'" % (phone, come_day)
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        if result is None:
            return 0
        return 1
    except:
        print("error")


def room_follow_id(id):  # 订单查询房间
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select rid from main_order where id = '%s'" % id
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        if result is None:
            return 0
        return result[0]
    except:
        print("error")


def if_today_cout(phone):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        come_day = datetime.date.today()
        sql = "select * from main_order where phone = '%s' and check_out_date = '%s'" % (phone, come_day)
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        if result is None:
            return 0
        return 1
    except:
        print("error")


def check_out(phone):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "delete from main_client where phone = '%s'" % phone
        cursor.execute(sql)
        db.commit()
        sql = "update main_order set state = 2 where phone = '%s' and state = 1" % phone
        cursor.execute(sql)
        db.commit()
    except:
        print("error")

