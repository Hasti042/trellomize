import dataSQlite
class SystemAdmin:
    clAtt = 'superuser'

    def __init__(self  , username , password) :
       self .username = username 
       self .password =  password
       dataSQlite .insert_admin_data(self .username , self .password)
    
    
    @staticmethod
    def deactive_user(password):
         dataSQlite .deactive_users(password)
         
    
#main*****************************************************
def create_admin():
    while True:
        username = input('Enter your user ID: ')
        if username.strip() == '':
            print('User ID is required. Please try again.')
            continue
        
        password = input('Enter your password: ')
        if password.strip() == '':
            print('Password is required. Please try again.')
            continue
        
        print('Super user has been created successfully.')
        return SystemAdmin(username, password)


admins = create_admin()


