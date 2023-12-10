from utils.groupby import *
from utils.extend import extendFunc
from utils.sort import sortMultiCols
from utils.select import *
import csv
import warnings
warnings.filterwarnings('ignore')
__all__ = ['Relation', 'GroupWrap']

# Mat:
# - Project - handle error
# - Rename - handle error
# - Union
# - join

# Bill:
# - Select
# - Groupby

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
                                self.filename.get(
                                    col_head[index]).append(int(val))
                            elif float(val):
                                self.filename.get(
                                    col_head[index]).append(float(val))
                        except:
                            self.filename.get(col_head[index]).append(val)

        elif isinstance(filename, dict):
            self.filename = filename
    # Singe-table operations:

    # project
    def project(self, cols):
        for col in cols:
            if col not in self.filename:
                raise KeyError(f"Column '{col}' not found in relation")

        new_data = {col: self.filename[col] for col in cols}
        return Relation(new_data)

    # rename
    def rename(self, old, new):
        if old not in self.filename:
            raise KeyError(f"Column '{old}' not found in relation")

        if new in self.filename:
            raise ValueError(f"Column '{new}' already exists in relation")

        self.filename[new] = self.filename.pop(old)
        return self

    def extend(self, name, operand0=None, operand1=None, operator=None):
        data = self.filename
        operatorList = ["+", "-", "/", "*"]
        if not self.verifyCols([name]):
            return {"Fail"}
        elif not operand0:
            data[name] = []  
        elif not operand1:
            data[name] = operand0
        elif not operator or operator not in operatorList:
            return {"Fail": "Wrong Operation"}

        else:
            try:            
                data[name] = extendFunc(operand0, operand1, operator)
            except: return {"Fail": f"{operand0 } and {operand1} not same type"}
        return Relation(data)

    #     select(query)

    def select(self, operand1, operand2, operator):
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
        return Relation(data)

    #     gropby(cols)

    def groupby(self, cols, operator=None):
        operation = [None, 'count', 'sum', 'mean', 'median', 'min', 'max']
        if self.verifyCols(cols):
            data = GroupByCols(self.filename, cols, operator)
            if operator in operation:
                pass
            else:
                return {"Fail": "No such operator"}

        return Relation(data)
    # def count (self, cols, operation):
    #     if operation == "groupby":

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
            res[h] = []
        for idx, row in enumerate(colData):
            for i in otherColHead:
                [res[i].append(otherRow) for otherRow in otherData[i]]
                [res[row].append(data[row][idx]) for row in data]
        return Relation(res)
    #     union(other)

    def union(self, other):
        if set(self.filename.keys()) != set(other.filename.keys()):
            print("Columns in Courses:", list(self.filename.keys()))
            print("Columns in Dept:", list(other.filename.keys()))
            raise ValueError(
                "Union can only be performed on relations with the same set of columns.")

        new_data = {col: self.filename[col] +
                    other.filename[col] for col in self.filename}
        return Relation(new_data)

    #     join(other, condition)
    def join(self, other, condition):
        # Condition should be a tuple specifying (left_col, right_col)
        left_col, right_col = condition

        # Construct new dictionary to hold join output
        join_dict = {}
        for col in set(self.filename.keys()) | set(other.filename.keys()):
            join_dict[col] = []

        # Go through rows and populate output
        for i in range(len(self.filename[left_col])):
            left_val = self.filename[left_col][i]

            # Find matching right val
            for j in range(len(other.filename[right_col])):
                right_val = other.filename[right_col][j]
                if left_val == right_val:
                    # Match found, populate output row
                    for col in join_dict:
                        if col in self.filename:
                            join_dict[col].append(self.filename[col][i])
                        elif col in other.filename:
                            join_dict[col].append(other.filename[col][j])

        return Relation(join_dict)
    #     semijoin(other)

    def semijoin(self, other, condition):
        data = self.filename
        dataHead = self.getTabelHead()
        colD = self.getColData(condition[0])
        otherColD = other.getColData(condition[1])
        res = dict()
        for i in dataHead:
            res[i] = []
        for idx, val in enumerate(colD):
            if val in otherColD:
                [res[h].append(data[h][idx]) for h in dataHead]
        return Relation(res)
    #     antijoin(other)

    def antijoin(self, other, condition):
        data = self.filename
        dataHead  = self.getTabelHead() 
        colD = self.getColData(condition[0])
        otherColD = other.getColData(condition[1])
        res = dict()
        for i in dataHead:
            res[i] = []
        for idx, val in enumerate(colD):
            if val not in otherColD:
                [res[h].append(data[h][idx]) for h in dataHead]
        return Relation(res)
    #     outerjoin(other)

    def outerjoin(self, other, condition):
        data = self.filename
        dataHead  = self.getTabelHead() 
        otherHead = other.getTableHead()
        colD = self.getColData(condition[0])
        otherColD = other.getColData(condition[1])
        res = dict()
        dataHead = dataHead + otherHead
        for i in dataHead:
            res[i] = []
        for idx, val in enumerate(colD):
            if val not in otherColD:
                [res[h].append(data[h][idx] | 'null') for h in dataHead]
        for idx, val in enumerate(otherColD):
            if val not in colD:
                [res[h].append(data[h][idx] | 'null') for h in dataHead]
        return Relation(res)
    
    def getColData (self, col): 
        try:
            return self.filename[col]
        except:
            return {"Fail": "No such column head in this table"}

    def getColsDataType(self, cols, data=None):
        if not data:
            data = self.filename
        return [type(data[col][0]) for col in cols]

    def verifyCols(self, cols):
        try:
            [self.filename[col] for col in cols]
            return True
        except:
            return {"Fail": "No such column head in this table"}

    def getTableData(self):
        return self.filename
    
    def getTabelHead (self):
        return [col for col in self.filename]


