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


def create_admin_tab(name):
    s= 'create table '+name+"(names varchar(20))"
    db.execute(s)
    mydb.commit()

 

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
    create_admin_tab(name)
    print('admin registered successful')
    return True
    
        
    
def reg_user(name,address,phone,email,age,votestatus,password):
    s = "select * from users where phone = '"+phone+"'"
    db.execute(s)
    res = db.fetchall()
    if len(res)!=0:
        return False
    
    uniqueid = random.randint(11111,99999)         
    sql="insert into users(name,address,phone,email,age,votestatus,uniqueid,password) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(name,address,phone,email,age,votestatus,uniqueid,password)
    db.execute(sql,val)
    mydb.commit()
    print('user registered successful')
    return True


def show_tab():
    db.execute('show tables')
    res = db.fetchall()
    return res


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


def verify(user,password):       
    db.execute("select * from admins")
    res = db.fetchall()
    print('Given : ',user,password)
    for x in res:
        
        print(x[3],x[7])
        if x[3]==user and x[7]==password:
            print('authenticate admin detected')
            return True
        
    return False

def verify_user(user,password):       
    db.execute("select * from users")
    res = db.fetchall()
    print('Given : ',user,password)
    for x in res:
        
        print(x[3],x[7])
        if x[3]==user and x[7]==password:
            print('authenticate admin detected')
            return True
        
    return False

def tab_selection(tab_name):
    s = "show tables"
    db.execute(s)
    res = db.fetchall()
    for i in res:
        if i==tab_name:
            return False
    
