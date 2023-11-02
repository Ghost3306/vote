import mysql.connector
import random
from django.shortcuts import render
from .file import *
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


def get_elec_list():
    user = read_login()
    sql = "select * from electionslist where admin = '"+user+"'"
    db.execute(sql)
    res = db.fetchall()
    list_tab = []
    for x in res:
        list_tab.append(x[0])

    return list_tab


def reg_admin(name,email,phone,age,address,typeuser,password):
    s = "select * from allusers where phone = '"+phone+"'"
    db.execute(s)
    res = db.fetchall()
    if len(res)!=0:
        print('user already exist')
        return False
    
        
    sql="insert into allusers(name,email,phone,age,address,typeuser,password) values(%s,%s,%s,%s,%s,%s,%s)"
    val=(name,email,phone,age,address,typeuser,password)
    db.execute(sql,val)
    mydb.commit()
    
    return True
    

def admin_tab(name):
    admin = read_login()
    unique = name+"_"+admin[0:5]

    sql="insert into electionslist(elenm,admin,uniqueid) values(%s,%s,%s)"
    val=(name,admin,unique)
    db.execute(sql,val)
    mydb.commit()
    print('table name %s add to database',name)


    
def reg_user(name,email,phone,age,address,typeuser,password):
    s = "select * from allusers where phone = '"+phone+"'"
    db.execute(s)
    res = db.fetchall()
    if len(res)!=0:
        print('user already exist')
        return False
    
       
    sql="insert into allusers(name,email,phone,age,address,typeuser,password) values(%s,%s,%s,%s,%s,%s,%s)"
    val=(name,email,phone,age,address,typeuser,password)
    db.execute(sql,val)
    mydb.commit()
    print('user registered successful')
    return True


def show_tab():
    db.execute('show tables')
    res = db.fetchall()
    return res


def cr_election(str1):
    sql = "create table if not exists "+str1+"(name varchar(30),vote varchar(10))"
    db.execute(sql)
    mydb.commit()
    admin_tab(str1)
    return True

def insert_tab(tab_name,can_name):
    sql = "INSERT INTO "+ tab_name+ "(name) VALUES ('"+can_name+"')"
    db.execute(sql)
    mydb.commit()
    print('data inserted successfully')
    return True


def verify(user,password):       
    db.execute("select * from allusers")
    res = db.fetchall()
    print('Given : ',user,password)
    for x in res:
        
        print(x[2],x[6])
        if x[2]==user and x[6]==password:
            print('authenticate user/admin detected')
            return x[5]
        
    return False

def tab_selection(tab_name):
    s = "show tables"
    db.execute(s)
    res = db.fetchall()
    for i in res:
        if i==tab_name:
            return False
        
def get_uid(tab):
    db.execute(f"select * from electionslist where elenm = '{tab}'")
    res = db.fetchall()
    for x in res:
        print(x[2])
        ret = x[2]
        return ret
    

def show_cam(tab):
    try:
        sql = f"select * from {tab}"
        print(sql)
        db.execute(sql)
        res = db.fetchall()
        ret = []
        for x in res:
            ret.append(x[0])

        return ret
    except:
        pass

def fil_vote(cam_name,tab_name):
    sql = f"select * from {tab_name}"
    db.execute(sql)
    res = db.fetchall()

    for x in res:
        if x[0]==cam_name:
            cou = x[1]
            try:
                count = int(cou)
                
            except:
                count = 0
    count = count+1
    sql1 = f"update {tab_name} set vote = '{str(count)}' where name = '{cam_name}'"
    db.execute(sql1)
    user = read_login()
    sql2 = f"insert into sta_{user} values('{tab_name}')"
    db.execute(sql2)
    try:
        mydb.commit()
        return True
    except:
        return False
    

def user_status(name):
    sql = f"CREATE TABLE IF NOT EXISTS sta_{name} (name varchar(25))"
    db.execute(sql)

def search_user(name,tab):
    sql = f"select * from sta_{name}"
    db.execute(sql)
    res = db.fetchall()

    for x in res:
        if x[0]==tab:
            return 'false'
    return 'true'