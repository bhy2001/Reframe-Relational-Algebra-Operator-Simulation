import csv
import warnings
warnings.filterwarnings('ignore')
from utils.sort import sortMultiCols
from utils.extend import extendFunc
__all__ = ['Relation', 'GroupWrap']

# Mat: 
# - Project
# - Rename

# Bill:
# - Select
# - Groupby

# Kevin:
# - Sort
# - Extend

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
                            self.filename.get(col_head[index]).append(int(val))
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
        pass
    #     extend(name, formula)

    def extend(self, name, formula= None):
        data = self.filename
        # data[name] = extendFunc()
        return data
    #     select(query)

    def select(self, query):
        pass
    #     sort(cols, order)

    def sort(self, cols, order=False):
        data = sortMultiCols(self.filename, cols, order)
        return data
        
    #     gropby(cols)

    def groupby(self, cols):
        pass
    # Multi-table operations:

    #     product(other)
    def product(self, other):
        pass
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

Courses = Relation('./college/COURSE.csv')
Dept = Relation('./college/DEPT.csv')

# TESTING FOR PROJECT METHOD
resultCourses = Courses.project(['CId', 'Title'])
print(resultCourses.filename)
print("================================================")
# resultDept = Dept.project(['DId', 'DName'])
# print(resultDept.filename)
# print (resultCourses.filename.CId)
print(resultCourses.sort(['CId'],True))