'''
@author: oluiscabral
'''
from abc import ABC, abstractmethod

class ILoginUI(ABC):
    @abstractmethod
    def get_username(self)->str:
        pass
    @abstractmethod
    def get_password(self)->str:
        pass
    @abstractmethod
    def display_login_action_message(self):
        pass
    @abstractmethod
    def display_login_fail_message(self):
        pass
    @abstractmethod
    def display_login_success_message(self):
        pass