#!/usr/bin/python
# -*- coding: utf-8 -*-
package = 'mysql-connector'

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])

import mysql.connector as mysql
import sys
import os

sys.path.append('../')
from MaliciousActivities.readConfig import read_config

config_data = read_config()

host = config_data.get('db_host')
database = config_data.get('db_name')
port = config_data.get('db_port')
user = config_data.get('db_user')
passwd = config_data.get('db_password')
testdb = "demo_db"

db_create_file = "Injections/basic_table_built.sql"
injections_test_queries = "Injections/basic_test_queries.sql"
create_sales = "Threat/create_sales.sql"
create_salary = "Threat/create_salary.sql"
create_acct_group = "Threat/create_acct_group.sql"
change_sales = "Threat/change_my_sales.sql"
change_salary = "Threat/change_salary.sql"
call_stp_salary = "Threat/call_stp_salary.sql"
call_stp_sales = "Threat/call_sales_stp.sql"
call_acct_group = "Threat/call_acct_group.sql"
bad_acct_action = "Threat/bad_acct_action.sql"
bad_alter_sales = "Threat/bad_alter_sales.sql"
bad_salary_action = "Threat/bad_salary_action.sql"
cleanup_sql = "Threat/cleanup.sql"
threat_sql = "Threat/threatsql.sql"



def exec_query(query, test):
  connection = mysql.connect(
      	host = host,
      	database = database,
      	user = user,
      	passwd = passwd,
      	port = port,
        auth_plugin='mysql_native_password',
        use_pure=False,
  )

  cursor = connection.cursor(buffered=True)
  if test:
    cursor.execute("use " + testdb + ";")

  cursor.execute(query)
#   cursor.execute('COMMIT')
#   connection.commit()
#   sql = 'CREATE DATABASE demo_db'
#   cursor.execute(sql)


  if test:
    connection.commit()

  print("query", query)
    # fetch a single row using fetchone() method.
    #   row = cursor.fetchone()
    #   print("rowwwwww", row[0])

  cursor.close()
  connection.close()

def build_external_db():
    print("building sql tables")
    with open(db_create_file, 'r') as create_file:
        rollback_on_error=True
        lines = create_file.readlines()
        sql = " ".join(lines)
        print("sql here is", host, database, port, user)
        conn = mysql.connect(
            host = host,
            database = database,
            user = user,
            passwd = passwd,
            port = port,
            auth_plugin='mysql_native_password',
            use_pure=False,
        )
        try:
            cursor = conn.cursor()
            for statement in lines:
                cursor.execute(statement)
                if not rollback_on_error:
                    conn.commit() # commit on each statement
        except Exception as e:
            if rollback_on_error:
                conn.rollback()
            raise
        else:
            if rollback_on_error:
                conn.commit()
        # exec_query(sql, False)
    print("done building sql tables 1111111")


def is_commented(line):
    if line.isspace():
        return True
    if line.startswith("--"):
        return True
    return False


def ignore_wrapping_quotes(line):
    line = line.strip()
    if line.startswith('"') and line.endswith('"'):
        print(line[1:-1], "checlkingggg")
        return line[1:-1]

def test_injection_queries(file):
    print("start testing sql injections...")

    selected_file = injections_test_queries if len(file) == 0 else file

    print(selected_file, 'selectedFile')

    with open(selected_file) as test_queries:
        line = test_queries.readline()
        print('line', line)
        cnt = 1
        while line:
            if is_commented(line):
                print('commented')
                line = test_queries.readline()
                continue
            # line = ignore_wrapping_quotes(line)
            print("Line {}: {}".format(cnt, line), 'hello worldddd')
            exec_query(line, True)
            print('line', line)
            line = test_queries.readline()
            cnt += 1
    print("done testing. tested {} cases.\n".format(cnt - 1))

#if len(sys.argv) != 4:
#    print("arguments for this script are: 1.'build'/'test'  2. <username>  3.<password>")
#elif sys.argv[1] == "build":
if sys.argv[1] == "build":
    print('111111 inside function')
    build_external_db()
elif sys.argv[1] == "test":
    test_injection_queries("")
if sys.argv[1] == "createSales":
    test_injection_queries(create_sales)
elif sys.argv[1] == "createSalary":
    test_injection_queries(create_salary)
elif sys.argv[1] == "createAcctGroup":
    test_injection_queries(create_acct_group)
elif sys.argv[1] == "changeSales":
    test_injection_queries(change_sales)
elif sys.argv[1] == "changeSalary":
    test_injection_queries(change_salary)
elif sys.argv[1] == "callSalary":
    test_injection_queries(call_stp_salary)
elif sys.argv[1] == "callSales":
    test_injection_queries(call_stp_sales)
elif sys.argv[1] == "callAcctgroup":
    test_injection_queries(call_acct_group)
elif sys.argv[1] == "badAcctAction":
    test_injection_queries(bad_acct_action)
elif sys.argv[1] == "alterSales":
    test_injection_queries(bad_alter_sales)
elif sys.argv[1] == "badSalaryAction":
    test_injection_queries(bad_salary_action)
elif sys.argv[1] == "cleanup":
    test_injection_queries(cleanup_sql)
elif sys.argv[1] == "threatsql":
    test_injection_queries(threat_sql)
