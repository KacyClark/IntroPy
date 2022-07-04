# imports


#globals




#functions



def print_menu():
    print("---------------")
    print("     PyCal    ")
    print("---------------")

    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Division")

    print("[x] Exit")
    
#plain instructions
option = ""
while option != "x":
    print_menu
    option = input("Please select an option: ")
    if option == "x":
        break # break = end the loop
    num1 = float(input("Please provide num1: "))
    num2 = float(input("Please provide num2: "))


    if option == "1":   
        result = num1 + num2
   

    elif option == "2":
        result = num1 - num2
       

    elif option == "3":
        result = num1 * num2

    elif option == "4":
        if num2 == 0:
            print("NOT ALLOWED")
            result = "Error - cannot divide by zero"
    else: 
        result = num1/num2

    print("The result is: " + str(result))
    input("Press Enter to continue...")
    print("")
    print("")
    print("")



print("Thank you, Good Bye!")     
