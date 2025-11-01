age = int(input("Enter age"))
weight = float(input("Enter Weight"))
Temp = float(input("Enter Temperature"))

health_Index = (weight/age)+ (Temp/100)
print(f"Your health Index is {health_Index}")

if health_Index >= 5:
    print ("Excellent")
elif health_Index >= 3 and health_Index <= 5:
    print ("Moderate")
else:
    print ("Needs attention")
