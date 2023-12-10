import csv
import warnings
warnings.filterwarnings('ignore')
from utils.sort import sortMultiCols
from utils.extend import extendFunc
from utils.select import select_aux
__all__ = ['Relation', 'GroupWrap']

# Mat:
# - Project - handle error
# - Rename - handle error
# - Union
# - join

# Bill:
# - Select
# - Groupby
# - antijoin
# - outerjoin

# Kevin:
# - Sort - handle error
# - Extend - handle error
# - Product 
# - Semi 


class Relation():
    
    def __init__(self, filename):
        if isinstance(filename, str):
            self.filename = {}
            
            with open(filename) as csvFile:
                col_head = next(csvFile).replace("\n", "").split(",")
                for i in col_head:
                    self.filename[i] = []
                read_file = csv.reader(csvFile)
                for row in read_file:
                    for index, val in enumerate(row):
                        try:
                            if int(val):
                                self.filename.get(col_head[index]).append(int(val))
                            elif float(val):
                                self.filename.get(col_head[index]).append(float(val))
                        except:
                            self.filename.get(col_head[index]).append(val)
                          
                            
        elif isinstance(filename, dict):
            self.filename = filename
    # Singe-table operations:

    #     project(cols)
    def project(self, cols):
        # no duplicates
        new_filename = {col: self.filename[col]
                        for col in cols if col in self.filename}
        return Relation(new_filename)
    #     rename(old, new)

    def rename(self, old, new):
        if old in self.filename:
            self.filename[new] = self.filename.pop(old)
        return self

    def extend(self, name, operand0 = None, operand1 = None, operator= None):
        data = self.filename
        operatorList = ["+", "-", "/", "*"]
        if data.get(name):
            return {"Fail"}
        if not operand0:
            data[name] = []  
            return data          
        if not operand1:
            data[name] = operand0
            return data
        if not operator or operator not in operatorList:
            return {"Fail": "Wrong Operation"}
        try:            
            data[name] = extendFunc(operand0, operand1, operator)
            return data
        except: return {"Fail": f"{operand0 } and {operand1} not same type"}
    #     select(query)

    def select(self, operand2, operator, operand2):
        operator_list = ["=", ">", "<", ">=", "<="]
        if operand1 in self.filename and operator in operator_list:
            db = self.filename
            return select_aux(db, operand1, operator, operand2)
        else:
            return []
        
    #     sort(cols, order)

    def sort(self, cols, order=False):
        if self.verifyCols(cols):
            data = sortMultiCols(self.filename, cols, order)
        return data
        
    #     gropby(cols)

    def groupby(self, cols):
        pass
    # Multi-table operations:

    #     product(other)
    def product(self, other):
        data = self.filename
        colHead = self.getTabelHead()
        otherColHead = other.getTabelHead()
        otherData = other.getTableData()
        colData = self.getColData(colHead[0])
        res = {}
        for otherH in otherColHead:
            res[otherH] = []
        for h in colHead:
            res[h] =[]
        for idx, row in enumerate(colData):
            for i in otherColHead:
                [res[i].append(otherRow) for  otherRow in otherData[i]]
                [res[row].append(data[row][idx]) for row in data]
        return res
    #     union(other)

    def union(self, other):
        pass
    #     join(other, condition)

    def join(self, other, condition):
        pass
    #     semijoin(other)

    def semijoin(self, other):
        pass
    #     antijoin(other)

    def antijoin(self, other):
        pass
    #     outerjoin(other)

    def outerjoin(self, other):
        pass
