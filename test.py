from reframe import Relation
Courses = Relation('./college/COURSE.csv')
Dept = Relation('./college/DEPT.csv')
Enroll = Relation('./college/ENROLL.csv')
# TESTING FOR PROJECT METHOD
resultCourses = Courses.project(['CId', 'Title'])
# print(resultCourses.filename)
print("================================================")
print(Dept.project(['DId', 'DName']).filename)
# print(resultDept.filename)
# print (resultCourses.filename.CId)
# print(resultCourses.sort(['CId'],True))

# print(resultCourses.extend('Test', resultCourses.getColData('CId'), resultCourses.getColData('CId'), "-"))

# print(Courses.product(Dept).filename)
# print(Courses.semijoin(Dept,['DeptId','DId']).filename)
# print(Enroll.groupby(['SectionId','Grade'], 'count').filename)
