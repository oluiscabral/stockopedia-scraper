'''
@author: oluiscabral
'''
from data_structure.data import Data
from typing import Set
from data_structure.data_ref import DataRef

class DataSet:
    def __init__(self, storage:Set[Data]):
        self.storage:Set[Data] = storage
    
    def get_data(self, ref:DataRef):
        for data in self.storage:
            if ref == data.get_ref():
                return data
        return None
