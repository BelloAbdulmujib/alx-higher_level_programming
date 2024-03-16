#!/usr/bin/python3
-- create state table in hbtn_0e_0_usa with data
CREAT DATABASE IF EXIST hbtn_0e_0_usa;
import MySQLdb
db = MySQLdb.connect(host="MY_HOST", port="3360", user="my_user", passwd="MY_PASSW", db="MY_DB")
