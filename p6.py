students = [{"name":"Rohit","age":20,"weight":60.0},{"name":"rahul","age":22,"weight":70.0},{"name":"vimal","age":29,"weight":80.0}]
# for student in students:
#     print(student)

# for student in students:
#     if student["weight"] >= 70:
#         print(student)

def add_patient(name , age,weight):
    patient = {"name":name,"age":age,"weight":weight}
    students.append(patient)
    print(f"{patient['name']} is added")



def view_patients():
    for student in students:
        print(f" Name: {student['name']}, age: {student['age']}, weight: {student['weight']}")



def update_patient(name,new_weight):
    for p in students:
        if p["name"] == name:
            p["weight"] = new_weight
            print(f"{p['name']}'s weight is {p['weight']}")
            return




def delete_patient(name):
    for p in students:
        if p["name"] == name:
            students.remove(p)
            print(f"{p['name']} is removed")
            return





def main():
    view_patients()
    add_patient("gill",26,78)
    update_patient('Rohit',62.5)
    delete_patient("Rohit")
    view_patients()

main()