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
loopRange = config_data.get('loop_range')


try:
    conn = mysql.connect(
        host = host,
        database = database,
        user = user,
        passwd = passwd,
        port = port,
        auth_plugin='mysql_native_password',
        use_pure=False,
    );
    try:
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS SALARY')
        cursor.execute('create table salary(ssn varchar(40), first_name varchar(40), last_name varchar(40), base_sal int);')
        for x in range(loopRange):
            statement = f"insert into salary (ssn, first_name, last_name, base_sal) values ({x},'Thu', 'Lett',78000);"
            cursor.execute(statement)
            conn.commit()
        cursor.execute('Select * from salary')
    except Exception as e:
        print("error here ius", e)
        raise
    conn.close()
except Exception as e:
    print("error here is", e)

