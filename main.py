from rich.console import Console
import re
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
        self.used_emails = set()
        self.used_username = set()
   
   def registeration(self,email,username,password):
       pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
       if email in self.used_emails or password in self.used_username:
           console.print("the eamil or username have been used before",style="bold red")
       if not re.match(pat,email):
            console.print("the email is invalid!",style="bold red")
       else:
        self.users[username]=user(email,username,password)
        self.used_emails.add(email)
        self.used_username.add(username)
        console.print("you have successfully registered:smiling_face_with_smiling_eyes:",style="bold green")
    
   def login(self,username,password):
       if username not in self.users or self.users[username].password !=password :
           console.print("the username or password does not exist",style="bold red")
           return

       if not self.users[username].active:
           console.print("your account is deactive :warning:",style="bold red")
           return
   
   def inactive(self,username):
       if username not in self.users:
           console.print("the username does not exist",style="bold red")
           return
       self.users[username].active=False
 
       
       
