import csv
import warnings
warnings.filterwarnings('ignore')

__all__ = ['Relation', 'GroupWrap']


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
resultDept = Dept.project(['DId', 'DName'])
print(resultDept.filename)
