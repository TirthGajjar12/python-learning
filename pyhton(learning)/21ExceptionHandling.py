special_character = "!@#$%^&*"
class PasswordNotStrong(Exception):
    "raised when the passwword is not to strong"
    pass

class Signup:
    
    def __init__(self,fn,ln,username,password):
        self.fn = fn
        self.ln = ln
        self.username = username
        self.password = password

    

fn = input("Enter your first name: ")
ln = input("Enter your last name: ")
username = input("type your username: ")

while True:
    password = input("Enter your password: ")

    if  8 <= len(password) <= 16 and any(character.islower() for character in password ) and any(character.isupper() for character in password) and any(char.isdigit() for char in password) and any(char in special_character for char in password):
        print("Your information is saved...")
        break
    else:
        try:
            raise PasswordNotStrong("Password is not strong enough")
        except PasswordNotStrong as error:
            print(error) 
        continue

    
class InvalidCredential(Exception):
    "username or password is wrong"
    pass
    

user = Signup(fn,ln,username,password)

class Login:

    def __init__(self,un,password):
        self.un = un
        self.password = password

    def logincheck(self,user):
                if self.un == user.username and self.password == user.password:
                    print(f"welcome {user.fn} {user.ln}")
                else:
                    try:
                        raise InvalidCredential("invalid username or password")
                    except InvalidCredential as error:
                        print(error)
                

un = input("Enter username here: ")
password = input("Enter your password: ")

login = Login(un,password)

login.logincheck(user)
