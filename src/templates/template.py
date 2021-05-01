'''
@author: oluiscabral
'''
from typing import Dict, Tuple
from data_structure.data import Data

class Template:
    def __init__(self, definition:Dict[Tuple,Tuple[int,int]]):
        self.definition = definition
        
    def get_pos(self, data:Data):
        data_ref = data.get_ref()
        owners = tuple(data_ref.get_owners())
        if owners in self.definition:
            return self.definition[owners]
        return None
