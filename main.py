from rich.console import Console
import re
import time
import dataSQlite
from os import system
clear = lambda : system('cls')
console = Console()
class Account:

    def __init__(self,email,username,password,phone_number):
        self.email=email
        self.username=username
        self.password=password
        self.phone_number=phone_number
        self.active=True
        dataSQlite .insert_info(self .password , self .user_name , self .email , self .phone_number)
        self.users={}
        self.used_emails = set()
        self.used_username = set()
   
   
    def login(self,username,password):
       clear()
       count=0
       while True :
               try :
                    user_name = input ('Enter your user name :')
                    password = input ('Enter your pass :')
                    if  dataSQlite .verify_password(password , user_name) == (user_name , password) :
                        print ('this level show us you complte your personal information ... your welcome to our company ....')
                        break
               except ValueError :
                    print ('this user dosent exist please try again !')
                    count += 1 
                    if count == 3 :
                      print ('you try more than 3 times .... please try after 15 min ')
                      time . sleep (15*60)
                    elif count == 6 :
                      print ('you try more than 6 time plese try after one hour.....') 
                      time . sleep (60*60)
                    elif count == 10 :
                      print ('you are blocked! if you forget your pass plese call to our maneger to set new password for you. ')  #add_bot or messege system here 
                      break
             
               input ('this is just for our system press any key to continue.....')
   
    def inactive(self,username):
       if username not in self.users:
           console.print("the username does not exist",style="bold red")
           return

    def password(self) :
        return self ._password
 
    def password(self , value) :
        if self.check_password(value) and len(value) >= 8 :
            self ._password = value
            return True
        else :
            raise ValueError('password isn\'t valid')
         

    def check_password(password):
         has_digit=any(char.isdigit() for char in password)
         has_letter = any(char.isalpha() for char in password)
         if has_digit and has_letter:
              return True
         else:
              return False

    def email(self) :
         return self ._email

    
    def email(self , value) :
          if self.validate_email(value):
             self._email = value
          else:
             raise ValueError("Invalid email format")

    def check_email(email):
          pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
          if  re.match(pat,email):
              console.print("the email is invalid!",style="bold red")
          else:
             raise Exception("invalid email")
     
    def phone_number(self):
         return self ._phone_number

    
    def phone_number(self , value):
         if self .veryfing_phone_num(value)   :
             self ._phone_number = value
         else :
             raise ValueError('invalid phone number')

    def veryfing_phone_num(phone_number):
         pattern = r'^\d{4}\d{3}\d{4}$'
         if re.match(pattern,phone_number) :
              return True
         else :
             raise Exception('invalid phone_number')

    def make_password(): 
         pass

    def change_password():
         pass
    
    def register(self, username="", password="", email="", phone_number=""):
     if not password:
         password = input('Enter your password: ')
     if not username:
         username = input('Enter your userID: ')
     if not email:
         email = input('Enter your email: ')
     if not phone_number:
         phone_number = input('Enter your phone number: ')
     if username in self.used_username:
         raise ValueError('Username already exists')
     if email in self.used_emails:
         raise ValueError('Email already exists')
     if phone_number in self.users.values():
         raise ValueError('Phone number already exists')

     self.used_username.add(username)
     self.used_emails.add(email)

     return Account(username, password, email, phone_number)

       
