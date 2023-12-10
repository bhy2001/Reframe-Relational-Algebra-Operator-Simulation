testData = {
    'col1': ['A', 'A', 'B', 'E', 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
}

def sortMultiCols (data:dict, Cols:list, order:bool = False) -> dict:
    if len(Cols) == 0: return False
    # dataByCol = []
    traverse = traverseData(data)
    SortData  = getSortCols(traverse,colsIndex(data,Cols)) 
    # print("dd",traverse)
    # print("dd",data)
    # sortedData = generateRes(data, traverse, sortDict(SortData, order=order))
    return generateRes(data,traverse, sortDict(SortData, order=order))

# def sortListBySequence (data, sortDataList, Cols):
#     if len(sortDataList) == 1:
#         traverse = traverseData(data)
#         for i, val in enumerate(traverse):
#             if val[] in sortDataList[i]:
#                 sortDataList[i] = tra     
#     pass

def colsIndex(data, cols):
    res = []
    for search_key in cols:
        [res.append(idx) for idx, key in enumerate(data) if key == search_key]
    return res
    
def getSortCols (data, cols):
    sortData = {}
    for idx, key in enumerate (data):
        sortData[idx] = [data[key][col] for col in cols]
    return sortData
def sortDict (data, order=False):
    return dict(sorted(data.items(), key=lambda item: item[1],reverse=order))
    
def traverseData(data):
    dataList  = [data[i] for i in data]
    sortData = {}
    for idx, val in enumerate(dataList[0]):
        row = [col[idx] for col in dataList]
        sortData[idx] =row
    return sortData

def generateRes(orData, data, SortData):
    res = []
    for key in SortData:
        res.append(data[key])
    for idx, key in enumerate(orData):
        orData[key] = [row[idx] for row in res ]
    return orData 