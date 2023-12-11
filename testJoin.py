from reframe import Relation


courses = Relation('./college/COURSE.csv')
depts = Relation('./college/DEPT.csv')

join_cond = ('DeptId', 'DId')
result = courses.join(depts, join_cond)
print(result.filename)
