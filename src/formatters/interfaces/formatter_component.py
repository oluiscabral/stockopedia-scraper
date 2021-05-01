'''
@author: oluiscabral
'''
from abc import ABC, abstractmethod
from data_structure.formatted import Formatted

class FormatterComponent(ABC):
    @abstractmethod
    def format(self)->Formatted:
        pass