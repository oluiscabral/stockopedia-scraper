'''
@author: oluiscabral
'''
from typing import List
from abc import ABC
from data_structure.data_ref import DataRef

class Data(ABC):
    def __init__(self, name:str, ref:DataRef):
        self.name = name
        if ref != None:
            self.ref = ref.clone()
            self.ref.add_owner(name)
        self.table = []
        
    def get(self)->List[List[str]]:
        ret = []
        for line in self.table:
            ret.append(line.copy())
        return ret
    
    def get_ref(self)->DataRef:
        return self.ref.clone()
    
    def __iter__(self):
        return iter(self.get())
    