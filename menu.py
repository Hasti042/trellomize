# .8.0
# ****************************************************** all of this for menu becouse wo havent got any web page or app and we working in cmd 
import log_in as lo
import maneger as m
while True :
    lo .clear()
    print('havent you got any account ? you have to regester at first Press R to Register ')
    print('Press L to login')
    print('Press C to change password or you forget your password')
    print('Press S to set super user or create admin account')
    print('Press M to make project')
    print('Press G to give some responsobilite for your project')
    print('Press Q to quite application')
    print('Press T to be able to see telegram support bot')

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
     elif choice == 'P':
        project_choice = input('Press M to make a project.\nPress A to add a member to a project.\nPress R to remove a member from a project.\nPress D to delete a project.\nEnter your choice: ').upper()
        if project_choice == 'M':
            id = input('Please enter the project ID: ')
            title = input('Please enter the project title: ')
            leader = current_user
            project = pr(id, title, leader)
            projects[id] = project
            print(f'Project {title} created.')
        
    else :
        print('Wrong choice !')
    
    input('press any key to continue ....')  

