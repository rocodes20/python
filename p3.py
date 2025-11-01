income = int(input("Enter income"))
credit = int(input("Enter credit"))
loan_amt = int(input("Enter loan_amt"))
if income >= 30000 and credit >= 700:
    print("eligible")
elif income >= 20000 and credit >= 650:
    print("partially eligible")
else:
    print("not eligible")