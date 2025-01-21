students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students.sort()


for student in range(len(students)): 
   if students[student][1] == 37.21:
     print(students[student][0])
   