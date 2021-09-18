import sqlite3

dbname='books.db'
table_name='library'
def get_db():
  global dbname
  connection=sqlite3.connect(dbname)
  cursor=connection.cursor()
  return connection,cursor

def close_db(connection,cursor):
  if cursor:
    cursor.close()
  if connection:
    connection.close()

def create():
  try:
    connection,cursor=get_db()
    sql_command='''create table if not exists library(
        id integer primary key AUTOINCREMENT,
        name Text,
        title Text,
        year Text,
        status Text
    )'''
    cursor.execute(sql_command)
    connection.commit()
  except sqlite3.Error as err:
    print(' Create Sql error: %s' % (' '.join(err.args)))
    print("Exception class is: ", err.__class__)
    return 1
  finally:
    close_db(connection,cursor)
# create()

def view(table_name):
  try:
    connection,cursor=get_db()
    sql_command=f'select * from {table_name}'
    cursor.execute(sql_command)
    rows=cursor.fetchall()
    connection.commit()
    return rows
  except sqlite3.Error as err:
    print('View Sql error: %s' % (' '.join(err.args)))
    print("Exception class is: ", err.__class__)
    return 1
  finally:
    close_db(connection,cursor)
# view(table_name=table_name)

def search(table_name,id=None,name=None,title=None,year=None,status=None):
  try:
    connection,cursor=get_db()
    sql_command=f'select * from {table_name} where '
    where_condition=list()
    parameter_value=tuple()
    if id :
      where_condition.append(' id=? ')
      parameter_value+=(id,)
    if name:
      where_condition.append(' name=? ')
      parameter_value+=(name,)
    if title :
      where_condition.append(' title=? ')
      parameter_value+=(title,)
    if year :
      where_condition.append(' year=? ')
      parameter_value+=(year,)
    if status :
      where_condition.append(' status=? ')
      parameter_value+=(status,)
    where='and'.join(where_condition)
    cursor.execute(sql_command+where,parameter_value)
    rows=cursor.fetchall()
    connection.commit()
    return rows,where_condition
  except sqlite3.Error as err:
    print('Search Sql error: %s' % (' '.join(err.args)))
    print("Exception class is: ", err.__class__)
    return 1
  finally:
    close_db(connection,cursor)
# search(table_name,name='test',title='test',year='2019')

def insert(table_name,name,title,year,status):
  try:
    connection,cursor=get_db()
    sql_command=f"insert into {table_name} (name,title,year,status) values(?,?,?,?)"
    data_tuple=(name,title,year,status)
    cursor.execute(sql_command,data_tuple)
    connection.commit()
  except sqlite3.Error as err:
    print('Insert Sql error: %s' % (' '.join(err.args)))
    print("Exception class is: ", err.__class__)
    return 1
  finally:
    close_db(connection,cursor)
# insert(table_name,name='test1',title='test1',year='2020',status='Available')

def issue(table_name,id):
  try:
    connection,cursor=get_db()
    data_tuple = (id,)
    sql_command = f'select * from {table_name} where id=? and status="Available"'
    cursor.execute(sql_command, data_tuple)
    rows=cursor.fetchall()
    connection.commit()
    if rows:
      sql_command=f'Update {table_name} set status="Issued" where id=?'
      cursor.execute(sql_command,data_tuple)
      connection.commit()
    return rows
  except sqlite3.Error as err:
    print('Issue Sql error: %s' % (' '.join(err.args)))
    print("Exception class is: ", err.__class__)
    return 1
  finally:
    close_db(connection,cursor)
# issue(table_name,1)

def return_table(table_name,id):
  try:
    connection,cursor=get_db()
    data_tuple = (id,)
    sql_command = f'select * from {table_name} where id=? and status="Issued"'
    cursor.execute(sql_command, data_tuple)
    rows=cursor.fetchall()
    connection.commit()
    if rows:
      sql_command=f'Update {table_name} set status="Available" where id=?'
      cursor.execute(sql_command,data_tuple)
      connection.commit()
    return rows
  except sqlite3.Error as err:
    print('Return Sql error: %s' % (' '.join(err.args)))
    print("Exception class is: ", err.__class__)
    return 1
  finally:
    close_db(connection,cursor)
# return_table(table_name,1)

def delete(table_name,id):
  try:
    connection,cursor=get_db()
    data_tuple = (id,)
    sql_command = f'select status from {table_name} where id=?'
    cursor.execute(sql_command, data_tuple)
    status = cursor.fetchall()
    connection.commit()
    if status:
      sql_command=f'delete from {table_name} where id=?'
      cursor.execute(sql_command,data_tuple)
      connection.commit()
    return status
  except sqlite3.Error as err:
    print('Delete Sql error: %s' % (' '.join(err.args)))
    print("Exception class is: ", err.__class__)
    return 1
  finally:
    close_db(connection,cursor)
# delete(table_name,1)

def delete_all(table_name):
  try:
    connection,cursor=get_db()
    sql_command = f'delete from {table_name}'
    cursor.execute(sql_command)
    connection.commit()
    return 0
  except sqlite3.Error as err:
    print('Delete All Sql error: %s' % (' '.join(err.args)))
    print("Exception class is: ", err.__class__)
    return 1
  finally:
    close_db(connection,cursor)
# delete_all(table_name)
def drop(table_name):
  try:
    connection,cursor=get_db()
    sql_command = f'drop table {table_name}'
    cursor.execute(sql_command)
    connection.commit()
    return 0
  except sqlite3.Error as err:
    print('Drop Sql error: %s' % (' '.join(err.args)))
    print("Exception class is: ", err.__class__)
    return 1
  finally:
    close_db(connection,cursor)
    create()
# drop(table_name)

def main():
  create()
  global table_name
  while True:
    print('1:View','2:Search','3:Add','4:Issue','5:Delete','6:Exit',sep='\t')
    option=int(input('In'))
    if option==1:
      rows=view(table_name=table_name)
      for row in rows:
        print('--'*10)
        print(row,'\n')
        print('--'*10)
    elif option==2:
      name=input('Name: ')
      title=input('Title: ')
      year=input('Year: ')
      rows=search(table_name,name=name,title=title,year=year)
      for row in rows:
        print('*'*10)
        print(row,'\n')
        print('*'*10)
    elif option==3:
      name=input('New Name: ')
      title=input('New Title: ')
      year=input('New Year: ')
      insert(table_name,name,title,year,status='Available')
    elif option==4:
      id=int(input('Id : '))
      issue(table_name,id)
    elif option==5:
      id=int(input('Delete Id : '))
      delete(table_name,id)
    elif option==6:
      break

if __name__ == "__main__":
    main()
    print('End')