age = int(input("enter age: "))
temp = float(input("enter temp: "))
oxygen = float(input("Enter oxygen level: "))
if age > 60 and (temp >101 or oxygen < 93):
    print("High")
elif temp > 102 and oxygen < 90:
    print("high risk")
elif 99 <= temp <=102 and 90 <= oxygen <= 94:
    print("moderate")
else:
    print("low")