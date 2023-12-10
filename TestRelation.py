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