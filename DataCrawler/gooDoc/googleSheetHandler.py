from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


class SheetHandler(object):

    def __init__(self):
        self.spreadSheet = None
        self.typoScheme = None
        self.credentials = None

    def generate(self, credentials, sheetID, sheetName, range="A:Z"):
        self.credentials = credentials
        http = self.credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)

        spreadsheetId = sheetID # '1q9bCo9zGgLLf1sLdjR0H2yeALTid4UTQX6CTzMZoJnI'
        rangeName = sheetName # 'Work sheet'
        if len(range) != 0:
            rangeName = rangeName+"!"+range # "B#:F#", "B:F" for all from B to F, "B3:F100" from B3 to F100
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=rangeName).execute()
        values = result.get('values', [])

        self.spreadSheet = values


    def generateScheme(self, IDX=0, startRowNum=1):
        if self.spreadSheet is None:
            raise ValueError("spreadsheet has not yet assigned")
        if len(self.spreadSheet) is 0:
            raise ValueError("spreadsheet has no data")
        self.typoScheme = self.spreadSheet[0]
        self.spreadSheet.pop(0)
        startRowNum = startRowNum - 1
        for i in range(startRowNum+1):
            self.spreadSheet.pop(0)




