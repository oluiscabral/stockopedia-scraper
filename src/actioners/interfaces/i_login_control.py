'''
@author: oluiscabral
'''
from abc import ABC, abstractmethod

class ILoginControl(ABC):
    @abstractmethod
    def force_login(self):
        pass