import DataCrawler.gooDoc.googleSheetLoader as sheet


def load_sheet():
    sheetIDS = [
        '1O0HIYGDQLK4rwEpFg7R_zXOxgKyjjz6F7l26y0QzlxU',
        #'1-gYXBmGQLaTxSFnLtWfKTR79hqLMuVydBJM9sWuo6_4',
        #'1nptEZV6zrO-mpHOwa8jEz2lFHA1cbW8yZfPApAXCxgw',
        #'1VJL9eFe_34pjTLM0RGUSm1nUaa0hCArlvruJ_0bDTE4'  # week 21
        #'1mV_hjBS4qVtDaxlzZMVe8Wf8nkPu6euhiL_LBI-SMDk'  # week 22
        #'1wTwbVzHt6PoCNUWw7vJpVH9l5J9S2Dcf6R2HkBoxfks' #supplement
    ]
    sheetNames = ['Work sheet', 'Work sheet', 'Work sheet']
    credit = sheet.get_credentials()
    sheet.load(credit, sheetIDS, sheetNames)

load_sheet()