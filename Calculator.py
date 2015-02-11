import sys #Used to exit the program in function 6.

StoredAnswer = 0 #A global variable
check = 0
position = 0

def add():
    print("\nYou chose to perform addition with option #", option)
    if position == 1:
        num1 = StoredAnswer
        print("The first number is: ", num1)
        num2 = int(input("Enter the second number: "))
        answer = num1 + num2
        return answer
    if position == 2:
        num1 = int(input("\nEnter the first number: "))
        num2 = StoredAnswer
        print("The second number is: ",num2)
        answer = num1 + num2
        return answer
    else:
        num1 = int(input("\nEnter the first number: "))
        num2 = int(input("Enter the second number: "))
        answer = num1 + num2
        return answer

def sub():
    print("\nYou chose to perform subtraction with option #", option)
    if position == 1:
        num1 = StoredAnswer
        print("The first number is: ", num1)
        num2 = int(input("Enter the second number: "))
        answer = num1 - num2
        return answer
    if position == 2:
        num1 = int(input("\nEnter the first number: "))
        num2 = StoredAnswer
        print("The second number is: ",num2)
        answer = num1 - num2
        return answer
    else:
        num1 = int(input("\nEnter the first number: "))
        num2 = int(input("Enter the second number: "))
        answer = num1 - num2
        return answer

def mul():
    print("\nYou chose to perform multiplication with option #", option)
    if position == 1:
        num1 = StoredAnswer
        print("The first number is: ", num1)
        num2 = int(input("Enter the second number: "))
        answer = num1 * num2
        return answer
    if position == 2:
        num1 = int(input("\nEnter the first number: "))
        num2 = StoredAnswer
        print("The second number is: ",num2)
        answer = num1 * num2
        return answer
    else:
        num1 = int(input("\nEnter the first number: "))
        num2 = int(input("Enter the second number: "))
        answer = num1 * num2
        return answer

def div():
    print("\nYou chose to perform division with option #", option)
    if position == 1:
        num1 = StoredAnswer
        print("The first number is: ", num1)
        num2 = int(input("Enter the second number: "))
        answer = num1 / num2
        return answer
    if position == 2:
        num1 = int(input("\nEnter the first number: "))
        num2 = StoredAnswer
        print("The second number is: ",num2)
        answer = num1 / num2
        return answer
    else:
        num1 = int(input("\nEnter the first number: "))
        num2 = int(input("Enter the second number: "))
        answer = num1 / num2
        return answer

def mod():
    print("\nYou chose to perform modulo with option #", option)
    if position == 1:
        num1 = StoredAnswer
        print("The first number is: ", num1)
        num2 = int(input("Enter the second number: "))
        answer = num1 % num2
        return answer
    if position == 2:
        num1 = int(input("\nEnter the first number: "))
        num2 = StoredAnswer
        print("The second number is: ",num2)
        answer = num1 % num2
        return answer
    else:
        num1 = int(input("\nEnter the first number: "))
        num2 = int(input("Enter the second number: "))
        answer = num1 % num2
        return answer

def storedanswer():
    print(StoredAnswer)

def exit():
    print("\nExiting the program.\n")
    sys.exit(0)

while(1):
    try:
        print("Welcome to the calculator. Please enter your choice:\n")
        print("1. Addition\t2. Subtraction\t3. Multiplication\t4. Division\t5. Modulo")
        print("6. Show answer of previous question\t7. Use answer\t8. Clear values\t9. Exit")

        option = int(input("\nEnter you choice here: "))

        if option == 1:
            check = 1
            answer = add()
            StoredAnswer = answer
            print("\nThe answer is ",answer)

        if option == 2:
            check = 1
            answer = sub()
            StoredAnswer = answer
            print("\nThe answer is ",answer)

        if option == 3:
            check = 1
            answer = mul()
            StoredAnswer = answer
            print("\nThe answer is ",answer)

        if option == 4:
            check = 1
            answer = div()
            StoredAnswer = answer
            print("\nThe answer is ",answer)

        if option == 5:
            check = 1
            answer = mod()
            StoredAnswer = answer
            print("\nThe answer is ",answer)

        if option == 6:
            if check == 1:
                storedanswer()
            else:
                print("\nYou have not performed an equation yet.\n")

        if option == 7:
            if check == 1:
                occupy = int(input("\nWhich position would you like the answer to occupy? \n"))
                if occupy == 1:
                    position = 1
                elif occupy == 2:
                    position = 2
                else:
                    print("\nInsufficient character entered.\n")
            else:
                print("\nYou have not performed an equation yet.\n")

        if option == 8:
            reset = int(input("\nThis will reset values to zero. Continue? (Press 1 and enter.)\n"))
            if reset == 1:
                StoredAnswer = 0
                check = 0
                position = 0
            else:
                print("Returning to menu.\n")

        if option == 9:
            exit()

        elif (option < 1) or (option > 9):
            print("\nOops! Not a valid option. Please try again.\n")

        input("\n")
        print("\n" * 10)

    except ValueError:
        print("\nOops! Not a valid option. Please try again.\n")
