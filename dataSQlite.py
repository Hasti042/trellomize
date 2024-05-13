import sqlite3
from sys import path
import bcrypt
#  path[0] for one of vs codes problem doestn dopend on program

def create_table():
    cursor .execute('CREATE TABLE IF NOT EXISTS users_table(password TEXT PRIMARY KEY , username TEXT , email TEXT , phone_number INTEGER )') 


def insert_info(password , user_name , email , phone_number) :
    try :
        password = b"password"
        salt = bcrypt .gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        cursor .execute('INSERT INTO users_table VALUES(?,?,?,?)' , (hashed_password , user_name , email , phone_number))
        database .commit()
    except :
        raise sqlite3 .IntegrityError ('password must be with len 8 with at least one number and one letter')
    return True

# query with password i mean primary key
def users_info(password) :   
  users = cursor .execute('SELECT * FROM users_table WHERE password = ?' , (password,)) .fetchone()
  if users == None :
      raise ValueError('password as primary key dosent exist!')
  print(users)
  return users

# query with email
def read_info(email) : 
   emails = cursor .execute("SELECT * FROM users_table WHERE email = ?" , (email ,)) .fetchone()
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

# main-------------------------------------------------------

database = sqlite3 .connect(path[0] +"/data.db")
cursor = database . cursor()
database .commit()

