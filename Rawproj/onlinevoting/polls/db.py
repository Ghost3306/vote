import mysql.connector
import json

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="voting"
    )    
db =mydb.cursor()

def reg_user(name,address,phone,age,voters,uniid,password):
    sql="insert into voter(name,address,phone,age,voters,uniid,password) values(%s,%s,%s,%s,%s,%s,%s)"
    val=(name,address,phone,age,voters,uniid,password)
    db.execute(sql,val)
    if mydb.commit():
        return True
    return False

def verify(user,password):       
    db.execute("select *from voter")
    res = db.fetchall()
    for x in res:
        if x[5]==user and x[6]==password:
            return True
        
    
def cr_election(str1):
    sql = "create table if not exists "+str1+"(name varchar(30))"
    db.execute(sql)
    mydb.commit()
    return True

def insert_tab(tab_name,can_name):
    sql = "INSERT INTO "+ tab_name+ "(name) VALUES ('"+can_name+"')"
    db.execute(sql)
    mydb.commit()
    return True