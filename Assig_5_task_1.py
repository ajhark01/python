result = {"Alice's": 85, 'Rahul': 60, 'Ramesh' : 80, 'Rohit' : 45}
student_name = str(input("Enter student's name: "))
if student_name in result:
    print (student_name + 'marks :' + str(result[student_name]) )
else:
    print ('Student not found')