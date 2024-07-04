#!/usr/bin/python
package = 'mysql-connector'
import sys
from mysql.connector.errors import ProgrammingError
from mysql.connector import Error
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
failed_login_array= config_data.get('failed_login_array')
passwd = "wrong_password"
user = "N\A"

# listOfUsers = sys.argv[1:]
listOfUsers = list(failed_login_array.split(" "))


print(type(listOfUsers), listOfUsers, 'listOfUsers')

for user in listOfUsers:
    print("trying to log in with user " + user + " with wrong password")
    try:
        connection = mysql.connect(host=host, database=database, user=user, password=passwd, port=port, auth_plugin='mysql_native_password')
        print('connection', connection)
        connection.close()
    except Error as e:
        print("error here is", e, type(e))
        continue


print("Done. Number of users tried to log in:" + str(len(sys.argv)-1))
