import pymysql.cursors


connections = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", passwd="")

try:
    cursor=connections.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connections.close()