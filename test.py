from reframe import Relation

Courses = Relation('./college/COURSE.csv')
"""
CId,Title,DeptId
12,db systems,10
22,compilers,10
32,calculus,20
42,algebra,20
52,acting,30
62,elocution,30
"""
Enroll = Relation('./college/ENROLL.csv')
"""
EId,StudentId,SectionId,Grade
14,1,13,A
24,1,43,C
34,2,43,B+
44,4,33,B
54,4,53,A
64,6,53,A

"""
Section = Relation('./college/SECTION.csv')
"""
SectId,CourseId,Prof,YearOffered
13,12,turing,2018
23,12,turing,2016
33,32,newton,2017
43,32,einstein,2018
53,62,brando,2017
13,12,turing,1988
33,32,newton,2017

"""
Student = Relation('./college/STUDENT.csv')
"""
SId,SName,GradYear,MajorId
1,joe,2021,10
2,amy,2020,20
3,max,2022,10
4,sue,2022,20
5,bob,2020,30
6,kim,2020,20
7,art,2021,30
8,pat,2019,20
9,lee,2021,10

"""
Dept = Relation('./college/Dept.csv')
"""
DId,DName
10,compsci
20,math
30,drama

"""

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


# TESTING FOR UNION METHOD
# resultUnion = Courses.union(Dept)
# print("Union Result:")
# print(resultUnion.filename)


# TESTING FOR JOIN METHOD
join_cond = ('DeptId', 'DId')
result = Courses.join(Dept, join_cond)
print(result.filename)
print("================================================")
