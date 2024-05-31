import dataSQlite
import time
import bcrypt
from os import system
clear = lambda : system('cls')

class Loging_System :
    def __init__(self , password , user_name , email , phone_number) :
        self . password = password
        self . user_name = user_name
        self . email = email
        self .phone_number = phone_number
        dataSQlite .insert_info(self .password , self .user_name , self .email , self .phone_number)
    
    def Register(password="", user_name="", email="", phone_number=""):
        try :
            if not password:
                password = input('Enter your password: ')
            if not user_name:
                user_name = input('Enter your userID: ')
            if not email:
                email = input('Enter your email: ')
            if not phone_number:
                phone_number = input('Enter your phone number: ')
        except :
                raise ValueError(
            "one of your data isnot valid please try again"
            )
        return Loging_System(password, user_name, email, phone_number)
    
    
    def logging ():
            count = 0
            while True :
               try :
                    user_name = input ('Enter your user name :')
                    password = input ('Enter your pass :')
                    if  dataSQlite .verify_password(password , user_name) == (user_name , password) :
                        print ('corect info ✅this level show us you complte your personal information ... your welcome to our company ....')
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
    
    @staticmethod
    def users_info(password , user_name) :
        dataSQlite .verify_password(password , user_name)
    
    # validation for passwoed
    @property
    def password(self) :
        return self ._password
    @password.setter
    def password(self , value) :
        if self.check_password(value) and len(value) >= 8 :
            self ._password = value
            return True
        else :
            raise ValueError('password isn\'t valid')
    
    @staticmethod
    def check_password(password):
        has_digit = any(char.isdigit() for char in password)
        has_letter = any(char.isalpha() for char in password)
        if has_digit and has_letter:
            return True
        else:
          return False
    
    # validation for email
    @property
    def email(self) :
        return self ._email
    @email.setter
    def email(self , value) :
        if self.validate_email(value):
            self._email = value
        else:
            raise ValueError("Invalid email format")
    @staticmethod
    def validate_email(Email):
        from re import search   
        pattern = "[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|edu|net)"
        if search(pattern, Email):
            return True
        else:
            raise Exception ('invalid email')
    # validate phone number
    @property
    def phone_number(self):
        return self ._phone_number
    @phone_number .setter
    def phone_number(self , value):
        if self .veryfing_phone_num(value)   :
            self ._phone_number = value
        else :
            raise ValueError('invalid phone number')
    @staticmethod
    def veryfing_phone_num(phone_number):
       from re import match
       pattern = r'^\d{4}\d{3}\d{4}$'
       if match(pattern , phone_number) :
           return True
       else :
           raise Exception('invalid phone_number')
    

    # for new user connect to bo
    def change_password(username="" , new_password="") :
        from string import digits , ascii_letters
        from random import sample
        user_name= input('plese enter your username to change your password : ')
        if dataSQlite .name_info(user_name) == user_name :
            print('username exists✅')
            chars =  digits + ascii_letters #just be number and letter
            chars = list(chars)
            new_password = ""
            cipher_text=sample(chars , 8)
            for option in cipher_text :
                new_password+=option
                if len(new_password) == 8:
                    print('new password :', new_password)
                    print('now you can login with your new password')
                    dataSQlite .update_info(new_password , username)

        else :
            print('username dosent exist !')
        
# *********************************************main


