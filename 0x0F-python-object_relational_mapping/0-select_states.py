#!/usr/bin/python3
-- create state table in hbtn_0e_0_usa with data
CREAT DATABASE IF EXIST hbtn_0e_0_usa
import MySQLdb
db = MySQLdb.connect(host=MY_HOST ,name=MY_USERNAME, passwd=MY_PASSW, db=MY_DB)
