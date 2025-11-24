# Expence tracker Project

expences = []  # List of expences in form of dictionary
print("Welcome to Expence Tracker")

while True:
    print("===MENU===")
    print("1. Add Expences")
    print("2. View All Expences")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice :"))

# ADD Expence
    if(choice == 1):
        date = input("Enter Date? :")
        category = input("Enter Category? :")
        description = input("Aur deatil dedo :")
        amount = float(input("Enter Amount :"))

        expence = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expences.append(expence)
        print("\n Expences added successfully!")

#2. View All expences
    elif(choice == 2):
        if(len(expences) == 0):
            print("No Expences Added.")
        else:
            print("==== Your ALL Expneces ====")
            count = 1
            for eachKharcha in expences:
                print(f"Kharcha Number {count} -> {eachKharcha["date"]}, {eachKharcha["category"]}, {eachKharcha["description"]}, {eachKharcha["amount"]} ")
                count = count + 1

#3 View Total Spneding
    elif(choice == 3):
        total = 0
        for eachKharcha in expences:
            total = total + eachKharcha["amount"]   

        print("\n TOTAL KHARCHA = ", total)     

#4. EXIT
    elif(choice == 4):
        print("\n Thank You for Choosing our Tracker...")
        break
    else:
        print("INVALID CHOICE. Try Again..")