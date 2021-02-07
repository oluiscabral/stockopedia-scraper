import json
import platform
class Config:
    CONTENT = {
        "spreadsheet_url": None,
        "main_sheet_name": None,
        "compare_sheet_name": None,
        "email": None,
        "password": None,
    }
    platform = None
    
    @staticmethod
    def initialize_defaults():
        f = open('config.json','r')
        content = json.loads(f.read())
        for code in content:
            if code in Config.CONTENT:
                Config.CONTENT[code] = content[code]
        Config.platform = platform.system().upper()
    
    @staticmethod
    def get_email():
        return Config.CONTENT['email']
    
    @staticmethod
    def get_password():
        return Config.CONTENT['password']
    
    @staticmethod
    def get_spreadsheet_url():
        return Config.CONTENT['spreadsheet_url']
    
    @staticmethod
    def get_main_sheet_name():
        return Config.CONTENT['main_sheet_name']
    
    @staticmethod
    def get_compare_sheet_name():
        return Config.CONTENT['compare_sheet_name']

