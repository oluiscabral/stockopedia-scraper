'''
@author: oluiscabral
'''

import json

class Config:
    CONTENT = {
        "spreadsheet_url": None,
    }
    platform = None
    
    @staticmethod
    def initialize_defaults():
        f = open('config.json','r')
        content = json.loads(f.read())
        for code in content:
            if code in Config.CONTENT:
                Config.CONTENT[code] = content[code]
    
    @staticmethod
    def get_spreadsheet_url():
        return Config.CONTENT['spreadsheet_url']
