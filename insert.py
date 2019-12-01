import pymysql


db = pymysql.connect('localhost', 'root', 'root', 'TESTDB')
cursor = db.cursor()

sql = """INSERT INTO t_employee
            (first_name, last_name, age, sex, income)
            VALUES
            ('Jack', 'Brown', 23, 'M', 3000.00)
            """
try:
    cursor.execute(sql)
    db.commit()
except:
# 如果发生错误，则回滚；
    db.rollback()

db.close()
