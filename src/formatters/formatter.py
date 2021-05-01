'''
@author: oluiscabral
'''
from data_structure.formatted import Formatted
from data_structure.data import Data
from templates.template import Template
from typing import Set

class Formatter:
    def __init__(self, name:str, lines, cols, template:Template):
        self.name = name
        self.lines = lines
        self.cols = cols
        self.template = template
    
    def fill_formatted(self, formatted, data, tup):
        l, c = tup
        for i, line in enumerate(data.get()):
            for j, item in enumerate(line):
                formatted.insert(item, l + i, c + j)

    def format_data(self, formatted, data):
        tup = self.template.get_pos(data)
        if tup is not None:
            self.fill_formatted(formatted, data, tup)

    def format(self, dataset:Set[Data])->Formatted:
        formatted = Formatted(self.name, self.lines, self.cols)
        for data in dataset:
            self.format_data(formatted, data)
        return formatted
