#TASK1

student_marks={'alice':80,'bobby':85,'anna':79,'mike':82}
student_name=input('Enter your name: ')
if student_name in student_marks:
    mark=student_marks[student_name]
    print('the marks of {student_name} are: {mark} '.format(student_name=student_name,mark=mark))
else:
    print('{student_name} not found.'.format(student_name=student_name))

#TASK2
l1=[1,2,3,4,5,6,7,8,9,10]
print(l1)
first_five=(l1[0:5])
print('extracted first five elements are: {}'.format(first_five))
first_five.reverse()
print('reverse first five elements are: {}'.format(first_five))
