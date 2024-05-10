import mysql.connector as c
con=c.connect(
    host='localhost',
    user='root',
    password='123456')
cur=con.cursor()
cur.execute('create database if  not exists Railway_Management_System')
cur.execute('use Railway_Management_System')
cur.execute('create table if  not exists Train_Details(Train_ID integer(9) primary key,Name varchar(50),Route_Starting_Point varchar(50),Route_Ending_Point varchar(50),Departure_Time time,Arrival_Time time,carts integer(5),Per_cart_capacity integer(5))')
con.commit()
