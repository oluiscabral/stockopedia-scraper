'''
@author: oluiscabral
'''
from ui.interfaces.i_login_ui import ILoginUI

class LoginUI(ILoginUI):
    def __init__(self):
        pass
    
    def get_username(self)->str:
        print("Insert your stockopedia username (email).")
        return input("username: ")
    
    def get_password(self)->str:
        print("Insert your stockopedia password.")
        return input("password: ")
    
    def display_login_action_message(self):
        print("Trying to login...")
        
    def display_login_fail_message(self):
        print("Something went wrong trying to login.")
        print("Check your username and password inputs and try again.")
        print("-"*50)
    
    def display_login_success_message(self):
        print("Succesfully logged in Stockopedia")
        print("-"*50)
        
        