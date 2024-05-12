import sqlite3
from sys import path
#  path[0] for one of vs codes problem doestn dopend on program

def create_table():
    curosr .execute('CREATE TABLE IF NOT EXISTS users_table(password INTEGER PRIMARY KEY , username TEXT , email TEXT , phone_number INTEGER )') 


def insert_info(*args) :
    try :
        curosr .execute('INSERT INTO users_table VALUES(?,?,?,?)' , (*args,))
        database .commit()
    except :
        raise sqlite3 .IntegrityError ('password must be 6 digit uniq number')
    return True

# query with password i mean primary key
def users_info(password) :   
  users= curosr .execute('SELECT * FROM users_table WHERE password = ?' , (password ,))
  if users == None :
      raise ValueError('password as primary key dosent exist!')
  return users

# query with email
def read_info(email) : 
   emails = curosr .execute("SELECT * FROM users_table WHERE email = ?" , (email ,))
   if emails == None :
      raise ValueError('email dosent exist!')
   return emails

# query with phone number
def give_info(phone_number) :
    phoneNumber =curosr .execute("SELECT * FROM users_table WHERE phone_number = ? " , (phone_number,))
    if phoneNumber == None :
        raise ValueError ('phone number dosent exist!')
    return True


def delete_fired_user(password) :
    curosr .execute('DELETE FROM users_table WHERE password = ?' , (password ,))
    database . commit()
# for somebody who wants to change his or her data
def update_info(password , username , email , phone_number) :
    curosr .execute('UPDATE users_table SET username = ? , email = ? , phone_number = ? WHERE password = ?' , (username , email , phone_number , password))
    database . commit()


# main-------------------------------------------------------

database = sqlite3 .connect(path[0] +"/data.db")
curosr = database . cursor()
database .commit()
