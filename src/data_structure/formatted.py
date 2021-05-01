'''
@author: oluiscabral
'''
from data_structure.data import Data

class Formatted(Data):
    def __init__(self, name:str, lines:int, cols:int, ref=None):
        super().__init__(name, ref)
        self.__init_table(lines, cols)
    
    def __init_table(self, lines, cols):
        line = [' ' for i in range(cols)]  # @UnusedVariable
        for i in range(lines):  # @UnusedVariable
            self.table.append(line.copy())
    
    def insert(self, c:str, line:int, col:int):
        self.__handle_table_size(line, col)
        self.table[line][col] = c
    
    def __handle_table_size(self, line, col):
        self.__handle_lines(line, col)
        self.__handle_cols(line, col)

    def __handle_lines(self, line, col):
        lines = len(self.table)
        if line >= lines:
            base = [' ' for i in range(col)] # @UnusedVariable
            for i in range(line+20-lines): # @UnusedVariable
                self.table.append(base.copy())

    def __handle_cols(self, line, col):
        cols = len(self.table[line])
        if col >= cols:
            for i in range(col+20-cols): # @UnusedVariable
                self.table[line].append(' ')

