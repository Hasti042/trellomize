import dataSQlite
class SystemAdmin:
    clAtt = 'superuser'

    def __init__(self  , username , password) :
       self .username = username 
       self .password =  password
       dataSQlite .insert_admin_data(self .username , self .password)
    
    
    def create_admin():
        while True:
            username = input('Enter your user ID for admins name :')
            if username.strip() == '':
                print('User ID is required. Please try again.')
                continue
            password = input('Enter your password:')
            if password.strip() == '':
                print('Password is required. Please try again.')
                continue
            return SystemAdmin(username, password)
    
    


