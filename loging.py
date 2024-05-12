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
        self .email = email
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

    # for new user connect to bot
    
    
    
    def make_password(): 
        pass


    def change_password():
        pass
# *********************************************main
# obj1 = loging('123' , 'ali' , 'email' , 'phone_number')
# obj1 .logging()


