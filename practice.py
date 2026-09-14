'''for i in range(5):
   a=int(input("enter a salary of employee:"))
   if a>60000:
      bonus=((a*5)/100)
      print("final salary:",bonus+a)
   elif a>=30000:
      bonus=((a*10)/100)
      print("final salary:",bonus+a)
   elif a<30000:
      bonus=((a*15)/100)
      print("final salary:",bonus+a)
sum=0
for j in range(10):
    b=int(input("enter a no "))
    if b%2==0:
       sum+=b 
       
print("The sum is:",sum)
even=[]
odd=[]
for k in range(10):
    c=int(input("enter a no:"))
    if c%2==0:
      even.append(c)
    else :
      odd.append(c)
print("The even list",even)
print("the odd list ",odd)'''
alphabet=0
num=0
special=0
str=input("Enter a string")
for char in str:
    if char.isalpha():
       alphabet+=1
    elif char.isdigit():
       num+=1
    else :
       special+=1 
print("the charaters are:",alphabet)
print("the digit are:",num)
print("the special character:",special)



   

   