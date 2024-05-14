# 0.5.0
# ****************************************************** all of this for menu becouse wo havent got any web page or app and we working in cmd 
import log_in as lo
while True :
    
    lo .clear()
    print('havent you got any account ? you have to regester at first press R to Register ')
    print('press L to login')
    print('press C to change password or you forget your password')
    print('press Q to quite application')

    choice = input('Enter your choice :').upper()
    if choice == 'L':
        lo .Loging_System.logging()
    elif choice == 'R':
        lo .Register()
    elif choice == 'C':
        lo .Loging_System .change_password()
    elif choice == 'Q':
        break
    else :
        print('Wrong choice !')
    
    input('press any key to continue ....')  


#  this is goingo to be complete soon ..
