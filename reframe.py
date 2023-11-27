import csv
import warnings
warnings.filterwarnings('ignore')

__all__ = ['Relation', 'GroupWrap']

class Relation():
    def __init__(self,filename:str):
        self.data = {}
        with open(filename) as csvFile:
            col_head = next(csvFile).replace("\n", "").split(",")
            for i in col_head:   
                self.data[i] = []
            read_file = csv.reader(csvFile)
            for row in read_file:
                for index, val in enumerate(row):
                    self.data.get(col_head[index]).append(val)
    # Singe-table operations:

    #     project(cols)
    def project (self,cols):
        pass
    #     rename(old, new)
    def rename (self,old,new):
        pass
    #     extend(name, formula)
    def extend(self, name, formula):
        pass
    #     select(query)
    def select(self, query):
        pass
    #     sort(cols, order)
    def sort(self, cols, order):
        pass
    #     gropby(cols)
    def groupby(self, cols):
        pass
    # Multi-table operations:

    #     product(other)
    def product (self, other):
        pass
    #     union(other)
    def union(self, other):
        pass
    #     join(other, condition)
    def join (self, other, condition):
        pass
    #     semijoin(other)
    def semijoin(self, other):
        pass
    #     antijoin(other)
    def antijoin(self, other):
        pass
    #     outerjoin(other)
    def outerjoin (self, other):
        pass

Dept = Relation('./college/COURSE.csv')