import csv
import warnings
warnings.filterwarnings('ignore')

__all__ = ['Relation', 'GroupWrap']

# Mat:
# - Project - handle error
# - Rename - hanndle error

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

    def semijoin(self, other):
        pass
    #     antijoin(other)

    def antijoin(self, other):
        pass
    #     outerjoin(other)

    def outerjoin(self, other):
        pass


# Courses table
# CId,Title,DeptId
# 12,db systems,10
# 22,compilers,10
# 32,calculus,20
# 42,algebra,20
# 52,acting,30
# 62,elocution,30


# Enroll table
# EId,StudentId,SectionId,Grade
# 14,1,13,A
# 24,1,43,C
# 34,2,43,B+
# 44,4,33,B
# 54,4,53,A
# 64,6,53,A


# Dept table
# DId,DName
# 10,compsci
# 20,math
# 30,drama


# Section table
# SectId,CourseId,Prof,YearOffered
# 13,12,turing,2018
# 23,12,turing,2016
# 33,32,newton,2017
# 43,32,einstein,2018
# 53,62,brando,2017
# 13,12,turing,1988
# 33,32,newton,2017


# Student table
# SId,SName,GradYear,MajorId
# 1,joe,2021,10
# 2,amy,2020,20
# 3,max,2022,10
# 4,sue,2022,20
# 5,bob,2020,30
# 6,kim,2020,20
# 7,art,2021,30
# 8,pat,2019,20
# 9,lee,2021,10

Courses = Relation('./college/COURSE.csv')
Enroll = Relation('./college/ENROLL.csv')
Section = Relation('./college/SECTION.csv')
Student = Relation('./college/STUDENT.csv')
Dept = Relation('./college/Dept.csv')


