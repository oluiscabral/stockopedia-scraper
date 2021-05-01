'''
@author: oluiscabral
'''
from typing import List

class DataRef(object):
    def __init__(self, stock_ticker:str, owners:List[str]=[]):
        self.stock_ticker = stock_ticker
        self.owners = owners.copy()
        self.url_ref = None
    
    def add_owner(self, name:str):
        self.owners.append(name)
    
    def get_owners(self)->List[str]:
        return self.owners.copy()
    
    def get_stock_ticker(self)->str:
        return self.stock_ticker
    
    def get_url_ref(self)->str:
        if self.url_ref is None:
            return self.stock_ticker
        return self.url_ref
    
    def set_url_ref(self, v:str)->str:
        self.url_ref = v

    def get(self)->str:
        return '.'.join(self.owners) + ':' + self.stock_ticker
    
    def clone(self)->'DataRef':
        clone = DataRef(self.stock_ticker, self.owners)
        clone.set_url_ref(self.get_url_ref())
        return clone
    
    def reset(self):
        self.set_url_ref(None)
    
    def __eq__(self, other:'DataRef'):
        if other == None:
            return False
        return self.get() == other.get()
    
    def __str__(self):
        return self.get()
    
    def __repr__(self):
        return self.get()
    
    def __hash__(self):
        h = hash(self.stock_ticker)
        for owner in self.owners:
            h += hash(owner)
        return h
        
        
        
        
        
        