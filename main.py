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
        self.used_emails = set()
        self.used_passwords = set()
   
   def registeration(self,email,username,password):
       if email in self.used_emails or password in self.used_passwords:
           console.print("the eamil or password have been used before",style="bold red")
       
       else:
        self.users[username]=user(email,username,password)
        self.used_emails.add(email)
        self.used_passwords.add(password)
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
 
       
       
