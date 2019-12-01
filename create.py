import pymysql


db = pymysql.connect('localhost', 'root', 'root', 'TESTDB')
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS t_employee')

sql = """CREATE TABLE t_employee (
            first_name CHAR(20) NOT NULL,
            last_name CHAR(20),
            age INT,
            sex CHAR(1),
            income FLOAT)"""
cursor.execute(sql)

db.close()
