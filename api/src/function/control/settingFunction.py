import pygame as pg
import os

HASH_TAG = '#'
COLON = ':'
COMA = ','
SPACE = ' '
NEW_LINE = '\n'

def getSettings(path,settingKey) :
    settings = {}
    with open(path,'r',encoding='utf-8') as settingsFile :
        allSettingLines = settingsFile.readlines()
    for line, settingLine in enumerate(allSettingLines) :
        # print(f'\n--    settingLine = {settingLine[:-1]}, line = {line}    --')
        depth = getDepth(settingLine)
        setingKeyLine = getKey(settingLine)
        # print(f'      -- setingKeyLine = {setingKeyLine}')
        if settingKey == setingKeyLine :
            # print(f'      -- settingValueLine = {getValueFromAttribute(settingLine)}')
            settingValue = getValueFromAttribute(settingLine)
            print(f'''key : value --> {settingKey} : {settingValue}''')
            return settingValue

def getDepth(settingLine):
    characterIndex = 0
    depthNotFount = True
    depth = 0
    while not settingLine[characterIndex] == NEW_LINE :
        if depthNotFount and settingLine[characterIndex] == SPACE:
            depth += 1
        characterIndex += 1
    return depth

def getKey(settingLine):
    possibleKey = filterString(settingLine)
    # print(f'      getKey({possibleKey}) = {possibleKey.strip().split(HASH_TAG)[0].split(COLON)[0].strip()}')
    return settingLine.strip().split(HASH_TAG)[0].split(COLON)[0].strip()

def getValueFromAttribute(settingLine):
    possibleValue = filterString(settingLine)
    # print(f'''      getValueFromAttribute({possibleValue}) = {getValue(':'.join(possibleValue.strip().split(HASH_TAG)[0].split(COLON)[1:]).strip())}''')
    return getValue(COLON.join(possibleValue.strip().split(HASH_TAG)[0].split(COLON)[1:]).strip())

def filterString(string) :
    # print(f'''filterString({string}) = string[-1] = -->{string[-1]}<--, string[-1] == {NEW_LINE} = {string[-1] == NEW_LINE}''')
    if string[-1] == NEW_LINE :
        string = string[:-1]
    string = string.strip()
    # print(f'filteredString = -->{string}<--')
    return string

def getValue(value) :
    # print(f'        getValue(): value = {value}')
    if value :
        if '[' == value[0] :
            # print(f'      getValue({value}) = {getList(value)}')
            return getList(value)
        elif '(' == value[0] :
            # print(f'      getValue({value}) = {getTuple(value)}')
            return getTuple(value)
        elif '{' == value[0] :
            # print(f'      getValue({value}) = {getDictionary(value)}')
            return getDictionary(value)
        try :
            # print(f'      getValue({value}) = {int(value)}')
            return int(value)
        except :
            try :
                # print(f'      getValue({value}) = {float(value)}')
                return float(value)
            except :
                # print(f'      getValue({value}) = {value}')
                return value

def getList(value):
    roughtValues = value[1:-1].split(COMA)
    values = []
    for value in roughtValues :
        values.append(getValue(value))
    # print(f'      getList({value}) = {values}')
    return values

def getTuple(value):
    roughtValues = value[1:-1].split(COMA)
    values = []
    for value in roughtValues :
        values.append(getValue(value))
    # print(f'        tupleValues = {values}')
    return tuple(values)

def getDictionary(value) :
    # print(f'         value = {value}')
    splitedValue = value[1:-1].split(COLON)
    # print(f'         splitedValue = {splitedValue}')

    keyList = []
    for index in range(len(splitedValue) -1) :
        keyList.append(splitedValue[index].split(COMA)[-1].strip())
    # print(f'         keyList = {keyList}')

    valueList = []
    valueListSize = len(splitedValue) -1
    for index in range(valueListSize) :
        if index == valueListSize -1 :
            correctValue = splitedValue[index+1].strip()
        else :
            correctValue = COMA.join(splitedValue[index+1].split(COMA)[:-1]).strip()
        # print(f'        correctValue = {correctValue}')
        valueList.append(getValue(correctValue))
    # print(f'         valueList = {valueList}')

    resultantDictionary = {}
    for index in range(len(keyList)) :
        resultantDictionary[keyList[index]] = valueList[index]

    return resultantDictionary

def getFileNames(path,fileExtension) :
    fileNames = []
    names = os.listdir(path)
    for name in names :
        splitedName = name.split('.')
        if fileExtension == splitedName[-1] :
            fileNames.append(''.join(splitedName[:-1]))
    return sortItNumerically(fileNames)

def sortItNumerically(fileNames) :
    sortedFileNamesWhichAreNumbers = sorted(numberfyIt(fileNames))
    return stringfyIt(sortedFileNamesWhichAreNumbers,fileNames)

def numberfyIt(numbersAsStrings) :
    numbers = []
    for string in numbersAsStrings :
        numberAsString = string
        ###- '4'
        ###- '4_1'
        ###- '4_2'
        floatNumber = None
        if 'i' not in numberAsString :
            floatNumber = getFloatNumberSplitingNumberAsTringBySeparatorList(numberAsString,['_','-','.'])
            if str(floatNumber) :
                numbers.append(floatNumber)
    return numbers

def getFloatNumberSplitingNumberAsTringBySeparatorList(numberAsString,separatorList) :
    if separatorList :
        splitedNumberAsString = numberAsString.split(separatorList[0])
        if len(splitedNumberAsString) == 1 :
            try :
                return float(f'{splitedNumberAsString[0]}.0')
            except : pass
        elif len(splitedNumberAsString) == 2 :
            try :
                return float(f'{splitedNumberAsString[0]}.{splitedNumberAsString[1]}')
            except : pass
        return getFloatNumberSplitingNumberAsTringBySeparatorList(splitedNumberAsString[0],separatorList[1:])
    else :
        return numberAsString

def stringfyIt(sortedNumbers,numbersAsStrings) :
    sortedNumbersAsStrings = []
    for floatNumber in sortedNumbers :
        ###- 4
        ###- 4.1
        ###- 4.2
        sortedNumberAsString = str(floatNumber)
        if int(sortedNumberAsString.split('.')[1]) != 0 :
            sortedNumberAsString.replace('.','_')
        else :
            sortedNumberAsString = sortedNumberAsString.split('.')[0]
        sortedNumbersAsStrings.append(sortedNumberAsString)
    for numberAsString in numbersAsStrings :
        if numberAsString not in sortedNumbersAsStrings :
            sortedNumbersAsStrings.append(numberAsString)
    return sortedNumbersAsStrings
