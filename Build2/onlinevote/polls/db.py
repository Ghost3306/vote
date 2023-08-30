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


def reg_admin(name,address,phone,age,org,password):
    result = select_all('admins')
    print(result)
    for res in result:
        print(phone,res[2])
        if phone==res[2]:
            return False
    uniqueid = 0
    uniqueid = random.randint(11111,99999)
    for res in result:
        if uniqueid==res[5]:
            uniqueid = random.randint(11111,99999)
        else:
            sql="insert into admins(name,address,phone,age,organization,uniqueid,password) values(%s,%s,%s,%s,%s,%s,%s)"
            val=(name,address,phone,age,org,uniqueid,password)
            db.execute(sql,val)
            mydb.commit()
            
           
            return True
            
    return False

def reg_user(name,address,phone,age,votestatus,password):
    results = select_all('users')
    print(results)
    for res in results:
        print(phone,res[2])
        if phone==res[2]:
            
            return
    uniqueid = 0
    uniqueid = random.randint(11111,99999)
    print(uniqueid)
    for res in results:
        if uniqueid==res[5]:
            uniqueid = random.randint(11111,99999)
        else:
            sql="insert into admins(name,address,phone,age,votestatus,uniqueid,password) values(%s,%s,%s,%s,%s,%s,%s)"
            val=(name,address,phone,age,votestatus,uniqueid,password)
            db.execute(sql,val)
            mydb.commit()
           
            return True
            


def show_tab():
    db.execute('show tables')
    res = db.fetchall()
    return res
select_all('admins')

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

print(reg_admin('lalit rawool','halwal','9614449928','20','college','root'))