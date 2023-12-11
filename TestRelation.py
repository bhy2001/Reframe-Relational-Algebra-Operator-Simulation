import pytest

from reframe import Relation
class TestRelation:
    # def __init__(self) -> None:
        # self.Courses = Relation('./college/COURSE.csv')
        # self.
        # Enroll = Relation('./college/ENROLL.csv')
        # Section = Relation('./college/SECTION.csv')
        # Student = Relation('./college/STUDENT.csv')
    def test_project(self):
        test = Relation('./college/DEPT.csv')
        expectRes = {'DId':[10,20,30],'DName': ['compsci','math','drama']}
        assert test.project(['DId','DName']).filename == expectRes
    
    def test_rename(self):
        test = Relation('./college/DEPT.csv')
        expectRes = {'DId':[10,20,30],'DeptName': ['compsci','math','drama']}
        assert test.rename('DName', 'DeptName').filename == expectRes
        
    def test_extend(self):
        test = Relation('./college/DEPT.csv')
        expectRes = {'DId': [10, 20, 30], 'DName': ['compsci', 'math', 'drama'], 'TEST': [10, 20, 30]}
        assert test.extend('TEST', [10,20,30]).filename == expectRes
    
    def test_sort(self):
        test = Relation('./college/ENROLL.csv')
        expectRes = {'EId': [54, 64, 24, 34, 44, 14], 'StudentId': [4, 6, 1, 2, 4, 1], 'SectionId': [53, 53, 43, 43, 33, 13], 'Grade': ['A', 'A', 'C', 'B+', 'B', 'A']}
        assert test.sort(['SectionId','Grade'],order=True).filename == expectRes
    
    def test_groupby(self):
        test = Relation('./college/ENROLL.csv')
        expectRes = {'count': [3, 1, 1, 1], 'Grade': ['A', 'B', 'B+', 'C']}
        assert test.groupby(['Grade'],'count').filename == expectRes
    
    def test_product(self):
        test = Relation('./college/DEPT.csv')
        test0 = Relation('./college/COURSE.csv')
        expectRes =  {'CId': [12, 22, 32, 42, 52, 62, 12, 22, 32, 42, 52, 62, 12, 22, 32, 42, 52, 62], 'Title': ['db systems', 'compilers', 'calculus', 'algebra', 'acting', 'elocution', 'db systems', 'compilers', 'calculus', 'algebra', 'acting', 'elocution', 'db systems', 'compilers', 'calculus', 'algebra', 'acting', 'elocution'], 'DeptId': [10, 10, 20, 20, 30, 30, 10, 10, 20, 20, 30, 30, 10, 10, 20, 20, 30, 30], 'DId': [10, 10, 10, 20, 20, 20, 30, 30, 30], 'DName': ['compsci', 'compsci', 'compsci', 'math', 'math', 'math', 'drama', 'drama', 'drama']}
        # print(test.product(test0).filename)
        assert test.product(test0).filename == expectRes

    def test_semijoin (self):
        pass
    
    def test_antijoin(self):
        course_table = Relation('./college/COURSE.csv')
        section_table = Relation('./college/SECTION.csv')
        expectedRes = {
            'CId': [22, 42, 52],
            'Title': ['compilers', 'algebra', 'acting'],
            'DeptId': [10, 20, 30],
        }
        cond = ('CId', 'CourseId')
        assert course_table.antijoin(section_table, cond).filename == expectedRes