'''
@author: oluiscabral
'''

class URL:
    def __init__(self, base:str):
        self.base = base
    
    def get(self, rep:str):
        return self.base.replace("${}", rep)