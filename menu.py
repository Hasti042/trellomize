# .8.0
# ****************************************************** all of this for menu becouse wo havent got any web page or app and we working in cmd 
import log_in as lo
import maneger as m
while True :
    lo .clear()
    print('havent you got any account ? you have to regester at first press R to Register ')
    print('press L to login')
    print('press C to change password or you forget your password')
    print('press S to set super user or create admin account')
    print('press M to make project')
    print('press G to give some responsobilite for your project')
    print('press Q to quite application')
    print('press T to be able to see telegram support bot')

    choice = input('Enter your choice :').upper()
    lo.clear()
    if choice == 'L':
        lo .Loging_System.logging()
    elif choice == 'R':
        lo . Loging_System.Register()
    elif choice == 'C':
        lo .Loging_System .change_password()
    elif choice == 'T':
        print('''if you want our compony more support or connect to our admin please use this link please copy this link in your browser and follow instructions(https://t.me/iust_BOT_bot)'''   )
    elif choice == 'S':
        m .create_admin()
    elif choice == 'Q':
        break
    else :
        print('Wrong choice !')
    
    input('press any key to continue ....')  

