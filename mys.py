import pymysql

db = pymysql.connect("localhost", "root","`123","robotest")

cur = db.cursor()
cur.execute("SHOW TABLES")

    
cur.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
version = cur.fetchone()
print("Database version: {}".format(version[0]))