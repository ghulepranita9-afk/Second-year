'''a=int(input("Enter a no for a Table:"))
k=int(input("Enter a no till where you want a table:"))
i=1
#print a table
for i in range(1 ,k+1):
    print(a,"*",i,"=",a*i)



    # for counting apositive no in t5he list
list=[3,6,8,-1,-4,9,12]
b=int(len(list))
j=0
for i in  list:
     if i>0:
           j= j+1
print("found a positive no is: ",j)




# to add a movie name in the list
movies=[]
print(movies)
for i in range(1 , 6):
      i=input(("Enter a element which you want to add in list:"))
      movies.append(i)
print(movies)  
a=int(input("enter a mark for SE:"))
b=int(input("enter a mark for python:"))
c=int(input("enter a mark for DSA:"))
total =a+b+c
percent=float((total*100)/300)
if percent >90:
    print("A+ GRADE",percent)
elif percent >80:
    print("A GRADE",percent)
elif percent >70:
    print("B+ GRADE",percent)
elif percent >60:
    print("B GRADE",percent)
elif percent >50:
    print("c GRADE",percent)
else :
    print("fail",percent)




print("hello", end=" ")
print("world")




i=5
j=4
for i in range(5):
   for j in range(4):
      print("*", end=" ")
   print() 
a=6

for i in  range(1,a+1):
    for j in range(1,i):
      print(j, end="")
    print()'''







student={}
name=input("enter a student name:")
div=input("enter a student div:")
student[" name"]=name
student["sa6 div"]=div
print(student)
student.update({
"enrollmwnt no":"12346",
"age":20
})
print(student)
print(student.keys())