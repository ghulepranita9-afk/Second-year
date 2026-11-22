
def calculate_area (shape , x,y=0):
    if shape=="circle":
        print("Aera of circle is: ",float(3.14*x*x))
    elif shape=="Rectangle":
        print("Area of rectangle is:",float(x*y))
    elif shape=="Traingle":
        print("Area of Traingle is :",float(0.5*x*y))
    
while(True):
    shape=input("Enter a shape name to calculate the area(Traingle, Reactangle, circle):")
    if shape=="circle":
       a=float(input("Enter a radius of a circle:"))
       calculate_area(shape,a)
    elif shape=="Rectangle":
        l=float(input("Enter a length of reactangle:"))
        w=float(input("Enter a width of reactangle:"))
        calculate_area(shape,l,w)
    elif shape=="Traingle":
        b=float(input("Enter the base of traingle:"))
        h=float(input("Enter the height of traingle:"))
        calculate_area(shape,b,h)
    elif shape=="stop":
        print("End of the program")
        break
    else:
        print("invlid choice")
