from reframe import Relation

Courses = Relation('./college/COURSE.csv')
Dept = Relation('./college/DEPT.csv')

# TESTING FOR PROJECT METHOD
resultCourses = Courses.project(['CId', 'Title'])
print(resultCourses.filename)
resultDept = Dept.project(['DId', 'DName'])
print(resultDept.filename)
print("================================================")

# TESTING FOR RENAME METHOD
resultCourses = Courses.project(['CId', 'Title'])
print("Before Rename:")
print(resultCourses.filename)
# Rename the 'Title' column to 'TitleCourse'
resultCourses.rename('Title', 'TitleCourse')

print("After Rename:")
print(resultCourses.filename)
print("================================================")
