try:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Second number cannot be zero")
except ValueError:
    print("enter only numbers")
except Exception as e:
    print(e)
finally:
    print("task done")

