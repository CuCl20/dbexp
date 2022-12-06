import pymysql
import datetime


def register(id, password):  # 注册
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_admin(id, password) values(%d,'%s')" % \
              (id, password)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_client(phone, email, name, sex):  # 增加旅客信息
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='', port=3306, db='datademo')
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
        sql = "select * from main_order"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
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
              f" main_order where (id={element[0]} or {element[0]} is null) and (phone={element[2]} or {element[2]} is null) and (pay_method={element[4]} or {element[4]} is null) " \
              f"and (state={element[3]} or {element[3]} is null) and (submit_date={element[5]} or {element[5]} is null) and (check_in_date={element[6]} or {element[6]} is null) and (check_out_date={element[7]} or {element[7]} is null) and (rid={element[1]} or {element[1]} is null)"
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
    except:
        print("Error:unable to fetch data")


def update_order_check(phone, new_check_in, new_check_out):  # 修改订单时间
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        now_time = datetime.date.today()
        sql = "select phone,id,state,pay_method,submit_date,check_in_date,check_out_date,rid from" \
              " main_order where phone='%s'" % phone
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            check_in = row[5].date()
            check_out = row[6].date()
            rid = row[7]
            change_room_state(rid, check_in, check_out, 0)
            change_room_state(rid, new_check_in, new_check_out, 1)
        sql = "update main_order set check_in_date='%s',check_out_date='%s'" \
              ",submit_date='%s' where phone='%s'" % (new_check_in, new_check_out, now_time, phone)
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


def change_room(phone, old_rid, new_rid):  # 换房&修改订单房间
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "update main_order set rid = %d where phone='%s'" % (new_rid, phone)
        cursor.execute(sql)
        db.commit()
        sql = "select check_in_date,check_out_date from main_order where phone='%s'" % phone
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            check_in = row[0].date()
            check_out = row[1].date()
            change_room_state(old_rid, check_in, check_out, 0)
            change_room_state(new_rid, check_in, check_out, 1)
        db.close()
    except:
        print("Error:unable to change rooms")


def update_order_payment(phone):  # 订单付款
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password=' ', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "update main_order set state = 1 where phone='%s'" % phone
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


def delete_order(phone):  # 按电话删除订单
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "select check_in_date,check_out_date,rid from main_order where phone='%s'" % phone
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            check_in = row[0].date()
            check_out = row[1].date()
            rid = row[2]
            change_room_state(rid, check_in, check_out, 0)
        db.commit()
        sql = "delete from main_order where phone='%s'" % phone
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        print("Error:unable to update pay state")
