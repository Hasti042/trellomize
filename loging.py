import dataSQlite
import logging
import time
from os import system
clear = lambda : system('cls')
# for old user

class loging :
    def __init__(self ,password , user_name , email , phone_number) :
        self . user_name = user_name
        self . password = password
        self . email = email
        self .phone_number = phone_number
        dataSQlite .insert_info(self .password , self .user_name , self .email , self .phone_number)



    def logging (*args):
            users = {'ali'  : ' ALi' , 'Donya' : ' DONya12' , 'reza' : 'REZA??' , 'sara' : 'sARA000'}    #connect databesa
            count = 0
            while True :
                print('which featuer woude you like to choose for logging ? email or phone number ?')
                user_name = input ('Enter your user name :')
                password = input ('Enter your pass :')
                if  users['ali'] == password or users['Donya']==password or users['reza']==password or users['sara'] == password :
                    print ('this level show us you complte your personal information ... your welcome to our company ....')
                    break
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
    
    
    # validation for passwoed
    @property
    def password(self) :
        return self ._password
    @password.setter
    def password(self , value) :
        if self.check_password(value) and len(value) >= 8 and value.split():
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
        return self ._validate_email
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
    # validation phone number
    @property
    def phone_number(self):
        return self ._phone_number
    @phone_number .setter
    def phone_number(self , value):
        if self .veryfing_phone_num(value)  :
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
    
    # for new user connect to bot
    def make_password(): 
        pass

    def change_password():
        pass
# *********************************************main
obj1 = loging('123Foppph' , 'ali' , 'foroozan@gmail.com' , '09124568795')
# obj1 .logging()

