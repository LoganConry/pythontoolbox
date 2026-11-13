#Scientific Calculator by Logan Conry

#The goal is to create a series of loops that ask for an input of numbers as well as the operator required
import math


#Give the user a list of usable operators
def choose_operator():
    valid = False
    while valid != True:
        print("List of Valid Operators:\nAdd, Subtract, Multiply, Divide,\nPower, NaturalLog, Logarithm, SquareRoot,\nSine, Cosine, Tangent, ASine,\nACosine, ATangent, Radians, Degrees.") 
        operator = input("\nWhich operation would you like to solve?:" )
        if operator == "Add" or operator == "Subtract" or operator == "Multiply" or operator == "Divide" or operator == "Power" or operator == "NaturalLog" or operator == "Logarithm" or operator == "SquareRoot" or operator == "Sine" or operator == "Cosine" or operator == "Tangent" or operator == "ASine" or operator == "ACosine" or operator == "ATangent" or operator == "Radians" or operator == "Degrees":
            valid = True
        else:
            valid = False
            print("Invalid operator, please choose a valid operator! (Case Sensitive)\n")
    return operator

        


#Ask the user to pick numbers to use in that operator
def choose_numbers(operator):
    num_one = None
    num_two = None
    if operator == "Add":
        print("Which two numbers would you like to add?:" )
        num_one = float(input("First Number: " ))
        num_two = float(input("Second Number: " ))
    elif operator == "Subtract":
        print("Which two numbers would you like to subtract? (First minus Second):" )
        num_one = float(input("First Number: " ))
        num_two = float(input("Second Number: " ))
    elif operator == "Multiply":
        print("Which two numbers would you like to multiply?:" )
        num_one = float(input("First Number: " ))
        num_two = float(input("Second Number: " ))
    elif operator == "Divide":
        print("Which two numbers would you like to divide? (First number divided by Second):" )
        num_one = float(input("First Number: " ))
        num_two = float(input("Second Number: " ))
        while num_two == 0:
            num_two = float(input("Second Number cant be 0, try again: " ))
    elif operator == "Power":
        print("Which two numbers would you like to use the power operator on? (First number to the power of the Second number):" )
        num_one = float(input("First Number: " ))
        num_two = float(input("Second Number: " ))
    elif operator == "NaturalLog":
        print("Which number would you like to use the Natural Log operator on?:" )
        num_one = float(input("First Number: " ))
        while num_one <= 0:
            num_one = float(input("Number can not be negative or 0 for this operation, try again: "))
    elif operator == "Logarithm":
        print("Which two numbers would you like to use the logarithm operator on? (Second number is the base of the logarithm):" )
        num_one = float(input("First Number: " ))
        num_two = float(input("Second Number: " ))
        while num_one < 1:
            num_one = float(input("First number can not be lower than 1 for this operation, try again: "))
        while num_two < 2:
            num_two = float(input("Second number can not be 1 or lower for this operation, try again: "))
    elif operator == "SquareRoot":
        print("Which number would you like to find the square root of?:" )
        num_one = float(input("First Number: " ))
        while num_one < 0:
            num_one = float(input("Number can not be negative for this operation, try again: "))
    elif operator == "Sine":
        print("Which number would you like to find the sine of?:" )
        num_one = float(input("First Number: " ))
    elif operator == "Cosine":
        print("Which number would you like to find the cosine of?:" )
        num_one = float(input("First Number: " ))
    elif operator == "Tangent":
        print("Which number would you like to find the tangent of?:" )
        num_one = float(input("First Number: " ))
    elif operator == "Degrees":
        print("Which number would you like to convert to degrees:" )
        num_one = float(input("First Number: " ))
    elif operator == "Radians":
        print("Which number would you like to convert to radians?:" )
        num_one = float(input("First Number: " ))
    elif operator == "ASine":
        print("Which number would you like to find the arcsine of?:" )
        num_one = float(input("First Number: " ))
        while num_one > 1 or num_one < -1:
            num_one = float(input("Number can not be greater than 1 or less than -1 for this operation, try again: "))
    elif operator == "ACosine":
        print("Which number would you like to find the arccosine of?:" )
        num_one = float(input("First Number: " ))
        while num_one > 1 or num_one < -1:
            num_one = float(input("Number can not be greater than 1 or less than -1 for this operation, try again: "))
    elif operator == "ATangent":
        print("Which number would you like to find the arctangent of?:" )
        num_one = float(input("First Number: " ))
    else:
        print("Invalid operator, please choose a valid operator!")
    return num_one, num_two

#Actually execute the operation

def run_operation(operator, first_number, second_number):
    if operator == "Add":
        solution = (first_number + second_number)
    elif operator == "Subtract":
        solution = (first_number - second_number)
    elif operator == "Multiply":
        solution = (first_number * second_number)
    elif operator == "Divide":
        solution = (first_number / second_number)
    elif operator == "Power":
        solution = (first_number ** second_number)
    elif operator == "NaturalLog":
        solution = math.log(first_number)
    elif operator == "Logarithm":
        solution = math.log(first_number, second_number)
    elif operator == "SquareRoot":
        solution = math.sqrt(first_number)
    elif operator == "Sine":
        solution = math.sin(first_number)
    elif operator == "Cosine":
        solution = math.cos(first_number)
    elif operator == "Tangent":
        solution = math.tan(first_number)
    elif operator == "Degrees":
        solution = math.degrees(first_number)
    elif operator == "Radians":
        solution = math.radians(first_number)
    elif operator == "ASine":
        solution = math.asin(first_number)
    elif operator == "ACosine":
        solution = math.acos(first_number)
    elif operator == "ATangent":
        solution = math.atan(first_number)
    else:
        print("You have errored at some point, please restart")
    print(solution)




def main():
    operator = choose_operator()
    first_number, second_number = choose_numbers(operator)
    run_operation(operator, first_number, second_number)

main()
