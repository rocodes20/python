from operations import add_data,view_data,update_data,delete_data

def main():
    while True:
        print("---Health Tracker---")
        print("1. Add Data")
        print("2. View Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")

        choice = int(input("Enter your choice"))

        if choice == 1:
            name = input("Enter name: ")
            date = input("Enter Date")
            weight = float(input("Enter Weight"))
            calories = int(input("Enter calories"))
            mood = input("Enter mood")
            add_data(name,date,weight,calories,mood)

        elif choice == 2:
            view_data()

        elif choice == 3:
            name = input("Enter name: ")
            weight = float(input("Enter Weight"))
            calories = int(input("Enter calories"))
            mood = input("Enter mood")
            
            update_data(name,weight,calories,mood)

        elif choice == 4:
            name = input("Enter name")
            delete_data(name)

        elif choice == 5:
            break

main()