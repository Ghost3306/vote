import mysql.connector
import random
from django.shortcuts import render
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vote"
    )    
db =mydb.cursor()
def select_all(tab_nm):
    sql = "select * from "+tab_nm
    db.execute(sql)
    res = db.fetchall()
    return res


    

def reg_admin(name,address,phone,email,age,org,password):
    s = "select * from admins where phone = '"+phone+"'"
    db.execute(s)
    res = db.fetchall()
    if len(res)!=0:
        return False
    
    uniqueid = random.randint(11111,99999)         
    sql="insert into admins(name,address,phone,email,age,organization,uniqueid,password) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(name,address,phone,email,age,org,uniqueid,password)
    db.execute(sql,val)
    mydb.commit()
    return True
    
        
    
def reg_user(name,address,phone,age,votestatus,password):
    s = "select * from users where phone = '"+phone+"'"
    db.execute(s)
    res = db.fetchall()
    if len(res)!=0:
        return False
    
    uniqueid = random.randint(11111,99999)         
    sql="insert into admins(name,address,phone,age,organization,uniqueid,password) values(%s,%s,%s,%s,%s,%s,%s)"
    val=(name,address,phone,age,votestatus,uniqueid,password)
    db.execute(sql,val)
    mydb.commit()
    return True


def show_tab():
    db.execute('show tables')
    res = db.fetchall()
    return res


def cr_election(str1,user):
    sql = "create table if not exists "+str1+"(name varchar(30))"
    sql1 = "insert into "+user+" values('"+str1+"')" 
    db.execute(sql1)
    mydb.commit()
    db.execute(sql)
    mydb.commit()
    return True

def insert_tab(tab_name,can_name):
    sql = "INSERT INTO "+ tab_name+ "(name) VALUES ('"+can_name+"')"
    db.execute(sql)
    mydb.commit()
    return True


def verify(user,password):       
    db.execute("select * from users")
    res = db.fetchall()
    for x in res:
        if x[2]==user and x[6]==password:
            return True
        
    return False

