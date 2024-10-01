import os
import random
os.system('cls' if os.name == 'nt' else 'clear') # Recommended by poke on stack overflow: (https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python)

console_screenHeader = """
Python Refresher App by Cameron Godwin (2024) v1.0


============================================="""
console_screenMainMenu = """Welcome to the Python Refresher App!
=============================================


   What would you like to do?

   [1] Name tricks: Some cool string and array tricks with your inputted name
   [2] BMI Calculator: Calculate your BMI based on your height and weight
   [3] The Five Number Report: A report of the five numbers inputted
   [4] The Anogram Finder: Check if two words are anograms of each other
   [5] Leap Year Checker: Check if a year is a leap year
   [6] Basic Calculator: Perform basic calculations
   [7] First 10 Fibonacci Numbers: Generate the first 10 Fibonacci numbers
   [8] Prime Number Checker: Check if a number is prime using a loop
   [9] Multiplication Table: Generate a multiplication table for numbers 1 - 10

   [0] Exit app.
"""
console_screenTemplate = """=============================================




   [0] Exit app.
"""

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        print(console_screenHeader)
        print(console_screenMainMenu)
        menuOption = input("Enter the corresponding number: ")
        if menuOption == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(console_screenHeader)
            print("Name Tricks")
            print(console_screenTemplate)
            Firstname = input("Enter your name (first): ")
            if Firstname == "0":
                print("Exiting app...")
                exit()
            elif Firstname == "":
                print("Please enter a name.")
                Firstname = input("")
            else:
                print("Great! Now enter your last name or just hit enter to continue.")
                Lastname = input("Enter your name (last): ")
                if Lastname == "":
                    Lastname = " "
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(console_screenHeader)
                    print("Name Tricks - Results")
                    print(console_screenTemplate)
                    print("Here's what I was able to do with the name(s) you gave me: " + Firstname + " " + Lastname)
                    print("1. Your name in uppercase: " + Firstname.upper() + " " + Lastname.upper())
                    print("2. Your name in lowercase: " + Firstname.lower() + " " + Lastname.lower())
                    print("3. Your name reversed: " + Firstname[::-1] + " " + Lastname[::-1])
                    shuffled_firstname = ''.join(random.sample(Firstname, len(Firstname)))
                    shuffled_lastname = ''.join(random.sample(Lastname, len(Lastname)))
                    print("4. Your name with letters in random order: " + shuffled_firstname + " " + shuffled_lastname)
                    input("Press enter to continue...")
                    main()
       
        if menuOption == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(console_screenHeader)
            print("BMI Calculator")
            print(console_screenTemplate)
            height = float(input("Enter your height in centimeters: "))
            if height == 0:
                print("Exiting app...")
                exit()
            weight = float(input("Enter your weight in kilograms: "))
            if weight == 0:
                print("Exiting app...")
                exit()
            bmi = weight / ((height/100) ** 2)
            print("Your BMI is: ", round(bmi, 2))
            if bmi < 18.5:
                print("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                print("You are normal weight.")
            elif 25 <= bmi < 29.9:
                print("You are overweight.")
            elif 30 <= bmi < 34.9:
                print("You are obese.")
            elif bmi >= 35:
                print("You are extremely obese.")
            input("Press enter to continue...")
            main()

        if menuOption == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(console_screenHeader)
            print("The Five Number Report")
            print(console_screenTemplate)
            number1 = int(input("Enter the first number: "))
            number2 = int(input("Enter the second number: "))
            number3 = int(input("Enter the third number: "))
            number4 = int(input("Enter the fourth number: "))
            number5 = int(input("Enter the fifth number: "))
            numbers = [number1, number2, number3, number4, number5]
            print("The numbers you entered are: ", numbers)
            print("The smallest number is: ", min(numbers))
            print("The largest number is: ", max(numbers))
            print("The range of the numbers is: ", max(numbers) - min(numbers))
            print("The sum of the numbers is: ", sum(numbers))
            print("The product of all the numbers is: ", number1 * number2 * number3 * number4 * number5)
            print("The mean of the numbers is: ", sum(numbers) / len(numbers))
            print("The numbers in ascending order are: ", sorted(numbers))
            print("The numbers in descending order are: ", sorted(numbers, reverse=True))
            input("Press enter to continue...")
            main()

        if menuOption == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(console_screenHeader)
            print("The Anogram Finder")
            print(console_screenTemplate)
            word1 = input("Enter the first word: ")
            if word1 == "0":
                print("Exiting app...")
                exit()
            word2 = input("Enter the second word: ")
            if word2 == "0":
                print("Exiting app...")
                exit()
            if sorted(word1) == sorted(word2):
                print("")
                print("")
                print("The words are anagrams of each other.")
                print("")
                print("Here's a sorted view: Word one - ",sorted(word1), " Word two - ", sorted(word2))
                
            else:
                print("")
                print("")
                print("The words are not anagrams of each other.")
                print("")
                print("Here's a sorted view: Word one - ",sorted(word1), " Word two - ", sorted(word2))
            input("Press enter to continue...")
            main()

        if menuOption == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(console_screenHeader)
            print("Leap Year Checker")
            print(console_screenTemplate)
            year = int(input("Enter the year you want to check: "))
            if year == 0:
                print("Exiting app...")
                exit()
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print("The year", year, "is a leap year.")
                    else:
                        print("The year", year, "is not a leap year.")
                else:
                    print("The year", year, "is a leap year.")
            else:
                print("The year", year, "is not a leap year.")
            input("Press enter to continue...")
            main()

        if menuOption == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(console_screenHeader)
            print("Basic Calculator")
            print(console_screenTemplate)
            num1 = float(input("Enter the first number: "))
            if num1 == 0:
                print("Exiting app...")
                exit()
            operator = input("Enter the operator (+, -, *, /): ")
            if operator == "0":
                print("Exiting app...")
                exit()
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                print("Exiting app...")
                exit()
            if operator == "+":
                print(num1, "+", num2, "=", num1 + num2)
            elif operator == "-":
                print(num1, "-", num2, "=", num1 - num2)
            elif operator == "*":
                print(num1, "*", num2, "=", num1 * num2)
            elif operator == "/":
                if num2 == 0:
                    print("You cannot divide by zero.")
                else:
                    print(num1, "/", num2, "=", num1 / num2)
            else:
                print("Invalid operator. Please try again.")
            input("Press enter to continue...")
            main()
        
        if menuOption == "7":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(console_screenHeader)
            print("First 10 Fibonacci Numbers")
            print(console_screenTemplate)
            n1 = 0
            n2 = 1
            count = 0
            while count < 10:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
            input("Press enter to continue...")

        if menuOption == "8":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(console_screenHeader)
            print("Prime Number Checker")
            print(console_screenTemplate)
            number = int(input("Enter the number you want to check: "))
            if number == 0:
                print("Exiting app...")
                exit()
            if number > 1:
                for i in range(2, number):
                    if (number % i) == 0:
                        print(number, "is not a prime number.")
                        break
                else:
                    print(number, "is a prime number.")
            else:
                print(number, "is not a prime number.")
            input("Press enter to continue...")
            main()
        
        if menuOption == "9":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(console_screenHeader)
            print("Multiplication Table")
            print(console_screenTemplate)
            print("   [1] Generated table (less neat)")
            print("")
            print("")
            print("       |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |   10  ")
            print("----------------------------------------------------------------------------------------")
            print("   1  ||   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |   10  ")
            print("   2  ||   2   |   4   |   6   |   8   |  10   |  12   |  14   |  16   |  18   |   20  ")
            print("   3  ||   3   |   6   |   9   |  12   |  15   |  18   |  21   |  24   |  27   |   30  ")
            print("   4  ||   4   |   8   |  12   |  16   |  20   |  24   |  28   |  32   |  36   |   40  ")
            print("   5  ||   5   |  10   |  15   |  20   |  25   |  30   |  35   |  40   |  45   |   50  ")
            print("   6  ||   6   |  12   |  18   |  24   |  30   |  36   |  42   |  48   |  54   |   60  ")
            print("   7  ||   7   |  14   |  21   |  28   |  35   |  42   |  49   |  56   |  63   |   70  ")
            print("   8  ||   8   |  16   |  24   |  32   |  40   |  48   |  56   |  64   |  72   |   80  ")
            print("   9  ||   9   |  18   |  27   |  36   |  45   |  54   |  63   |  72   |  81   |   90  ")
            print("  10  ||  10   |  20   |  30   |  40   |  50   |  60   |  70   |  80   |  90   |  100  ")
            print("")
            print("")
            choice = input("Press enter to continue...")
            if choice == "0":
                print("Exiting app...")
                exit()
            elif choice == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(console_screenHeader)
                print("Multiplication Table")
                print(console_screenTemplate)
                for i in range(1, 11):
                    for j in range(1, 11):
                        print(i * j, end="\t")
                    print()
                input("Select an option:")
            else :
                main()
        
        elif menuOption == "0":
            print("Exiting app...")
            exit()
        else:
            print("Invalid input. Please try again.")
            print("If you wish to exit the app, press 'CTRL + C' on your keyboard or select exit from the main menu.")
            input("Press enter to continue...")
            main()



    except Exception as e:
        print("An error occurred: ", e)
        print("If you wish to exit the app, press 'CTRL + C' on your keyboard or select exit from the main menu.")
        input("Press enter to continue...")
        main()



main()

def exit():
    print("Exiting app...")


