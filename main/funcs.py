import pymysql
import datetime

def add_worker(id, name, sex, age, department, position, phone):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='xyl1278157445', port=3306, db='djangodemo')
        cursor = db.cursor()
        sql = "insert into app01_worker(worker_id, worker_name, worker_sex, worker_age," \
              "worker_department, worker_position, worker_phone, worker_entry_time) value " \
              "(\'{id}\', \'{name}\', \'{sex}\', \'{age}\', \'{department}\', \'{position}\', " \
              "\'{phone}\', \'{entry_time}\');".format(id=id, name=name, sex=sex, age=age,
                                                      department=department, position=position,
                                                      phone=phone, entry_time=datetime.datetime.now())
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False