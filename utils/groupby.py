def GroupByCols (data:dict, Cols:list, operator=None) -> dict:
    if len(Cols) == 0: return False
    traverse = traverseData(data)
    SortedData  = sortDict(getSortCols(traverse,colsIndex(data,Cols))) 
    groups = groupData(SortedData)
    operated = operate(groups, operator=operator)
    # print (operated)
    if operator: return generateGroup(Cols=Cols,groupData=groups,operateData=operated)
    if operator: print(generateGroup(Cols=Cols,groupData=groups,operateData=operated)) 
    else:
        return generateRes(Cols, SortedData)

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

def generateRes(Cols, groupData):
    res = {}
    for idx, val in enumerate(Cols):
        res[val] = [groupData[key][idx] for key in groupData]
    return  res

def generateGroup(Cols, groupData, operateData):
    for idx, val in enumerate(Cols):
        operateData[val] = [ list(i[0].values())[0][idx] for i in groupData]
    return operateData

def groupData(data):
    groups = []
    check = []
    group = []
    for key in data:
        if data[key] == check:
            group.append({key: data[key]})
        else: 
            check  = data[key]
            group = [{key: data[key]}]
            if group not in groups:
                groups.append(group)
    return groups

def operate(data, operator):
    switch_dict = {
        'count': [len(rec) for idx, rec in enumerate(data)],
        # "sum": [rec - operand1[idx] for idx, rec in enumerate(operand0)],
        # "mean": [rec * operand1[idx] for idx, rec in enumerate(operand0)],
        # "median": [rec * operand1[idx] for idx, rec in enumerate(operand0)],
        # "min": [rec * operand1[idx] for idx, rec in enumerate(operand0)],
        # "max": [rec / operand1[idx] for idx, rec in enumerate(operand0)]
    }
    # return {operator: [len(rec) for idx, rec in enumerate(data)]}
    return {operator: switch_dict[operator]}