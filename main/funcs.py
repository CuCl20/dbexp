import pymysql
import datetime


def add_client(phone, email, name, sex):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_client(phone, email, name, sex) values('%s','%s','%s','%s')" % (phone, email, name, sex)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_order(id, pay_method, state, submit_date, check_in_date, check_out_date):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='yhv5tgh233', port=3306, db='datademo')
        cursor = db.cursor()
        sql = "insert into main_order(id, pay_method, state, submit_date, check_in_date, check_out_date) " \
              "values('%s',%d,%d,'%s','%s','%s')" % (id, pay_method, state, submit_date, check_in_date, check_out_date)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


def add_room(id, kind, state):
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

