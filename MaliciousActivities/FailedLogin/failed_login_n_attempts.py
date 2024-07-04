#!/usr/bin/python
package = 'mysql-connector'
import sys
sys.path.append('../')

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])


import mysql.connector as mysql
from MaliciousActivities.readConfig import read_config

config_data = read_config()

host = config_data.get('db_host')
database = config_data.get('db_name')
port = config_data.get('db_port')
passwd = "wrong_password"
numOfAttempts = 1;
user = "N\A"


if len(sys.argv) >= 2:
    user = sys.argv[1]
if len(sys.argv) >= 3:
    numOfAttempts = int(sys.argv[2])
cnt = 0
#print "trying to log in with user " + user + " with wrong password for " + str(numOfAttempts) + " times"
for i in range(numOfAttempts):
    try:
        connection = mysql.connect(host=host, database=database, user=user, passwd=passwd, port=port, auth_plugin='mysql_native_password')
        connection.close()
    except Exception as e:
        print("error here is", e)
        cnt += 1

print("Done. Number of failed login attempts:" + str(cnt))
