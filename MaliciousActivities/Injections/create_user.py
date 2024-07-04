#!/usr/bin/python
# -*- coding: utf-8 -*-
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
user = config_data.get('db_user')
passwd = config_data.get('db_password')


print('values here', host, database, port, user, passwd)

if len(sys.argv) < 3:
    print("Illegal num. of arguments. enter username and password")
else:
    try:
        mkuser = sys.argv[1]
        mkpass = sys.argv[2]
        mkhost = '%'

        connection = mysql.connect(host = host, database = database, user = user, passwd = passwd, port = port, auth_plugin='mysql_native_password', use_pure=False)

        cursor = connection.cursor (buffered=True)

        createQuery = "CREATE USER IF NOT EXISTS %s@'%s' IDENTIFIED WITH mysql_native_password BY '%s'" %(mkuser, mkhost, mkpass)
        cursor.execute(createQuery)
        grantQuery = "GRANT ALL PRIVILEGES ON *.* TO %s@'%s'" %(mkuser, mkhost)
        cursor.execute(grantQuery)
        cursor.close ()
        connection.close ()
    except Exception as e:
        print(e)
