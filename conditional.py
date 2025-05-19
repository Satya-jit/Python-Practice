day_of_week = input("Enter the day of the week: ").lower()
print("Its", day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("Time to relax!")
else:
    print("It's a weekday, time to work!")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    choice = input("Enter your operation (+, -, *, /, %): ")

    if choice == "+":
        sum_of_numbers = num1 + num2
        print("addition ", sum_of_numbers)
    elif choice == "-":
        diff_of_numbers = num1 - num2
        print("subtraction ", diff_of_numbers)
    elif choice == "*":
        product_of_numbers = num1 * num2
        print("multiplication ", product_of_numbers)
    elif choice == "/":
        div_of_numbers = num1 / num2
        print("division ", div_of_numbers)
    elif choice == "%": 
        remainder_of_numbers = num1 % num2
        print("remainder ", remainder_of_numbers)
    else:
        print("Invalid operation")
# This code takes a day of the week as input and checks if it's a weekend or a weekday.