def vitals():
        age = int(input("Enter age"))
        weight = int(input("enter weight"))
        temp = float(input("Enter temp"))
        oxygen = float(input("Enter oxygen level"))
        return age,weight,temp,oxygen

def index(age,temp,weight):
        index_value = (weight / age) + (temp / 100)
        return index_value

def risk_level(age,temp,oxygen):
        if age > 60 and (temp > 101 or oxygen < 93):
            return "High"
        elif temp > 102 and oxygen < 90:
            return "High Risk"
        elif 99 <= temp <= 102 and 90 <= oxygen <= 94:
            return "Moderate"
        else:
            return "Low"
        
def report(age,weight,temp,oxygen):
      index_Cal = index(age,temp,weight)
      risk_cal = risk_level(age,temp,oxygen)
      print("----Patient Report----")
      print(f"Age is {age},temp is {temp} and oxygen level is {oxygen}")
      print(f"health index is {index_Cal}")
      print(f"risk is {risk_cal}")

def main():
      age,weight,temp,oxygen = vitals()
      report(age,weight,temp,oxygen)
        
main()