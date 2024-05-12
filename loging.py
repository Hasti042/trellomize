import logging
import time
from os import system
clear = lambda : system('cls')

# for old user
def users_pass(function) :
    clear()
    users = {'ali'  : ' ALi' , 'Donya' : ' DONya12' , 'reza' : 'REZA??' , 'sara' : 'sARA000'}    #connect databesa
    def wrapper (*args):
        count = 0
        while True :
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
                print ('you are blocked! if you forget your pass plese call to our maneger to set new password for you. ')   
                break
            function(*args)
        return function
    input ('this is just for our system press any key to continue.....')
    return wrapper

# for new user connect to bot
def make_password(): 
    pass


def change_password():
    pass


