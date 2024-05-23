import sqlite3
from sys import path
import bcrypt
#  path[0] for one of vs codes problem doestn dopend on program
database = sqlite3 .connect(path[0] +"/data.db")
cursor = database . cursor()

# users table
def create_table():
    cursor .execute('CREATE TABLE IF NOT EXISTS users_table(password TEXT PRIMARY KEY , username TEXT , email TEXT , phone_number INTEGER )') 

def insert_info(password , user_name , email , phone_number) :
    try :
        cursor .execute('INSERT INTO users_table VALUES(?,?,?,?)' , 
                       (password , user_name , email , phone_number))
        database .commit()
    except sqlite3 .IntegrityError :
           print('Password must be unique.') 
           return False
    return True

# query with password i mean primary key
def verify_password(password , user_name) :   
  users = cursor .execute('SELECT username , password FROM users_table WHERE password = ? AND username = ?' ,
                         (password,user_name)) .fetchone()
  if users == None :
      raise ValueError('password as primary key dosent exist!')
  return users

# query with email
def read_info(email) : 
   emails = cursor .execute("SELECT * FROM users_table WHERE email = ?" , 
                           (email ,)) .fetchone()
   if emails is None :
      raise ValueError('email dosent exist!')
   return emails

# query with phone number
def give_info(phone_number) :
    phoneNumber = cursor .execute("SELECT * FROM users_table WHERE phone_number = ? " , (phone_number,)) .fetchone()
    if phoneNumber == None :
        raise ValueError ('phone number dosent exist!')
    return True


def delete_fired_user(password) :
    cursor .execute('DELETE FROM users_table WHERE password = ?' , (password ,))
    database . commit()
    
def update_info(password , username , email , phone_number) :
    cursor .execute('UPDATE users_table SET username = ? , email = ? , phone_number = ? WHERE password = ?' , (username , email , phone_number , password))
    database . commit()

# ********************************************************************
# superusers table

def creat_admins_table():
    cursor .execute('CREATE TABLE IF NOT EXISTS admins_table ( username TEXT , password TEXT PRIMARY KEY  )')


def insert_admin_data(username , password):
    try :
       cursor .execute("INSERT INTO admins_tabel VALUES (?,?) " , (username , password))
       database .commit()
    except :
        sqlite3 .IntegrityError('Admin with this data already exist !')
        return False
    return True

def autuntication(username , password) :
    user=cursor .execute('SELECT * FROM admins_table WHERE username = ? , password = ?' , (username , password)) .fetchone()
    if user ==None :
        print('there isnt any admins with this data !')
    return user



if __name__ == '__main__' :

   



    database .commit()
    # database .close()







