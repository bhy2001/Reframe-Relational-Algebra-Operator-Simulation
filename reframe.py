import csv
import warnings
warnings.filterwarnings('ignore')
from utils.sort import sortMultiCols
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
        if old in self.filename:
            self.filename[new] = self.filename.pop(old)
        return self

    def extend(self, name, formula):
        pass
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
