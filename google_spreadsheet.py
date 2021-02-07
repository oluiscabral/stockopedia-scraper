from __future__ import print_function
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import gspread
from gspread.client import Client
from gspread.models import Spreadsheet, Worksheet
from config import Config
import typing
from formatted_data import FormattedData

class GoogleSpreadsheet:
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.readonly']
    CREDS = None
    
    @staticmethod
    def login():
        creds = GoogleSpreadsheet.CREDS
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', GoogleSpreadsheet.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        GoogleSpreadsheet.CREDS = creds
    
    @staticmethod
    def fill(formatted_datas:typing.List[FormattedData]):
        client:Client = gspread.authorize(GoogleSpreadsheet.CREDS)
        spreadsheet:Spreadsheet = client.open_by_url(Config.get_spreadsheet_url())
        for formatted_data in formatted_datas:
            sheet = GoogleSpreadsheet.get_sheet(spreadsheet, formatted_data.name)
            GoogleSpreadsheet.fill_sheet(sheet, formatted_data)
    
    @staticmethod
    def get_sheet(spreadsheet:Spreadsheet, title:str) -> Worksheet:
        try:
            return spreadsheet.worksheet(title)
        except Exception:
            return spreadsheet.add_worksheet(title, 1, 1)

    @staticmethod 
    def fill_sheet(sheet:Worksheet, formatted_data: FormattedData):
        sheet.clear()
        sheet.append_rows(formatted_data.content)
    

    