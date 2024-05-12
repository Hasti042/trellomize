# ****************************************************** all of this for menu becouse wo havent got any web page or app and we working in cmd 
import loging as lo
while True :
    
    lo .clear()
    print('press L to login')
    print('press R to register')
    print('press C to change password or you forget your password')
    print('press Q to quite application')
    choice = input('Enter your choice :').upper()
    if choice == 'L':
        lo .users_pass()
    elif choice == 'R':
        lo .make_password()
    elif choice == 'C':
        lo .change_password()
    elif choice == 'Q':
        break
    else :
        print('Wrong choice !')


#  this is goingo to be complete soon ..