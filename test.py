from reframe import Relation
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