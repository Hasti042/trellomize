from rich.console import Console
console = Console()
class user:
    def __init__(self,email,username,password):
        self.email=email
        self.username=username
        self.password=password
        self.active=True

class Account:
   def __init__(self):
        self.users={}
   
   def registeration(self,email,username,password):
       if email in self.users or password in self.users:
           console.print("username or password have been used before",style="bold red")
       self.users[username]=user(email,username,password)
       console.print("you have successfully registered:smiling_face_with_smiling_eyes",style="bold green")
    
   def login(self,username,password):
       if username not in self.users:
           console.print("the username does not exist",style="bold red")
           return
       if  self.users[username].password !=password:
           console.print("the password is wrong",style="bold red")
           return
       if not self.users[username].active:
           console.print("your account is deactive :warning:",style="bold red")
           return
   
   def inactive(self,username):
       if username not in self.users:
           console.print("the username does not exist",style="bold red")
           return
       self.users[username].active=False
 
       
       
