import asyncJob.textAnalyzer.SylToCharParser as sylToChar
import asyncJob.textAnalyzer.diffCharacter as diffChars
import asyncJob.textAnalyzer.matrixConverter as matConv
import asyncJob.gooDocUtil.SheetLoader as sheet

def load_sheet():
    sheetIDS = [
        '1VJL9eFe_34pjTLM0RGUSm1nUaa0hCArlvruJ_0bDTE4',
    ]
    sheetNames = ['Work sheet']
    credit = sheet.get_credentials()
    sheet.load(credit, sheetIDS, sheetNames)

def load_typo_volume_cnt(volumeCntPath, writePath = "",smoothingCount = 1):
    #여아원피스,리아원피스,3,201803
    import csv
    volumeTable = dict()
    with open(volumeCntPath, 'r', encoding='UTF-8') as rfp:
        rcsv = csv.reader(rfp)
        next(rcsv)
        for row in rcsv:
            query = row[0]
            typo = row[1]
            search_volume = int(row[2])
            if typo not in volumeTable:
                volumeTable[typo] = smoothingCount
            volumeTable[typo] += search_volume
    return volumeTable

def readJASOTable(path):
    table = dict()
    with open(path, 'r', encoding='UTF-8') as fp:
        import csv
        rcsv = csv.reader(fp)
        for row in rcsv:
            table[row[0]] = row[1:]#table[row[1]]
    return table

def generateJASOTable(querySet, writePath = ""):
    # when write Path is existing, then write table file
    table = dict()
    for query in querySet:
        if query not in table:
            table[query] = sylToChar.parseSyllable(query)[0]
    if len(writePath) is not 0:
        with open(writePath, 'w') as fp:
            import csv
            wcsv = csv.writer(fp)
            for query in table:
                wcsv.writerow([query] + table[query])
    return table

def calcTypoFreq(intended, typo):
    a = [n for n in typo if n not in intended]
    return a


TriGramFreqModelPath = '../../model/typoTrigramFreq2'
TypoJasoCondiProbPath = '../../model/typoCondiProbMap2'
TypoFrequencyModelPath = '../../model/typoFreq2'
TypoBiGramFreqModelPath = '../../model/typoBigramFreq2'