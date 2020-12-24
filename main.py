import math
weapon = int (input("Enter a weapon 1-Pazmar,2-Roket,3-Baloon, 4-Equal alarm: "))
xP = int (input("Enter  x value of threat: "))
Yp = int (input("Enter y value of threat: "))
if(weapon==4):
    print("Equal alarm ")
elif(xP<0 or xP>20or Yp<0 or xP>20 or Yp>20 or xP<10 ):
    print("Fall in open space")
elif(xP==10 and Yp==10):
    print("all eras")
    if weapon==1:
        print("You have 30 seconds to enter a protected space")
    elif weapon==2:
        print("You have 60 seconds to enter a protected space")
    else:
        print("You have 120 seconds to enter a protected space")
    if(math.sqrt((0 - xP) ** 2 + (0 - Yp) ** 2) > 13 or weapon==3) :
        print("Cannot intercept")
    else:
        print("The missile is intercepted")
elif(Yp==10 and xP>10):
    print(" eras a and b")
    if weapon == 1:
        print("You have 30 seconds to enter a protected space")
    elif weapon == 2:
        print("You have 60 seconds to enter a protected space")
    else:
        print("You have 120 seconds to enter a protected space")
    if (math.sqrt((0 - xP) ** 2 + (0 - Yp) ** 2) > 13 or weapon == 3):
        print("Cannot intercept")
    else:
        print("The missile is intercepted")
elif(Yp==10 and xP<10):
    print(" Aera c")
    if weapon == 1:
        print("You have 30 seconds to enter a protected space")
    elif weapon == 2:
        print("You have 60 seconds to enter a protected space")
    else:
        print("You have 120 seconds to enter a protected space")
    if (math.sqrt((0 - xP) ** 2 + (0 - Yp) ** 2) > 13 or weapon == 3):
        print("Cannot intercept")
    else:
        print("The missile is intercepted")
else:
    if(xP>10 and Yp<10):
        print("Aera b")
    elif xP>10 and Yp>10:
        print("Area A")
    elif xP<10 and Yp>10:
        print("Aera c")

    if weapon == 1:
        print("You have 30 seconds to enter a protected space")
    elif weapon == 2:
        print("You have 60 seconds to enter a protected space")
    else:
        print("You have 120 seconds to enter a protected space")
    if (math.sqrt((0 - xP) ** 2 + (0 - Yp) ** 2) > 13 or weapon == 3):
        print("Cannot intercept")
    else:
        print("The missile is intercepted")

