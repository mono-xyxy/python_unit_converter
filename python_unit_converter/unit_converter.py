choice = input("Convert (1) km to miles or (2) kg to lbs: ")
if choice=="1":
    km=float(input("Enter Kilometers: "))
    miles = km*0.621371
    print("Miles: ",miles)
elif choice =="2":
    kg=float(input("Enter kilograms: "))
    lbs = kg*2.20462
    print("Pounds",lbs)
else:
    print("Invalid Choice: ")
