for i in range(1,51):
    print(i)
for i in range(1,51):
    if i  % 2 == 0:
        print(i)
count = 0

while True:
    temp = int(input("Enter temp: "))
    if temp < 105:
        count+=1
    else:
        print("crictical")
        print("count",count)
        break

patients = ["rohit","rahul","kohli"]
for patient in patients:
    for i in range(1,4):
        print(f"patient {patient} - Day {i} vitals recored")