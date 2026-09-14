def sum():
    print("Enter a detail for registration slip")
    s=input("enter a student name:")
    b=input("enter a registreation no: ")
    c=input("enter a subject name: ")

    print("The registration slip is")
    print("Student name is=",s)
    print("Student register no  =",b)
    print("Student eazamination  subject =",c)
sum()




def bill():
    a=input("enter a bill amount:")
    d=float(a)
    h=((10*d)/100)
    print("The 10 percent discount is:",h)
    print("The total bill after a discount is:",d-h)
bill()

city=["saee","ghule"]
def lists(list):
    for item in city:
        print(item,end=" ")
        print(len(city))
lists(city)
n=5
def fact(n):
         fact=1
         for i in range(1,n+1):
              fact=fact*i
         print(fact)

def calculate_calories(carbs,facts,proteins):
    c=carbs*4
    d=facts*9
    f=proteins*4
    print("The carbs contain ", c ,"calories")
    print("The Facts contain ", d ,"calories")
    print("The Protein contain ", c,"calories")
    print("The total calories intake :",c+d+f)
carbs=float(input("Enter the carbs in gram:"))    
facts=float(input("Enter the facts in gram:"))    
proteins=float(input("Enter the protein in gram:"))    
calculate_calories(carbs,facts,proteins)