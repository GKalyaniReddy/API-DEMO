student=[]
while True:
	mark=[]
name=input("enter name")
if name in ["stop"]:
   break
else:
    student.append(name)m
    for i in range(1,4):
     m=int(input("enter marks"))
     mark.append(m)
 student.extend(mark)
 print(student)
  
