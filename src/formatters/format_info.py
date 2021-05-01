'''
@author: oluiscabral
'''
from data_structure.data_ref import DataRef

class FormatInfo(object):
    def __init__(self, name:str, lines:int, cols:int, ref:DataRef):
        self.name = name
        self.lines = lines
        self.cols = cols
        self.ref = ref