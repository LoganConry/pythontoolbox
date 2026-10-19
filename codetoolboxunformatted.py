###---------------------------------------------------------------Chapter 2---------------------------------------------------------------
##---------------------Basic print---------------------
#print('Hello World')

#print("2024", "03", "15", sep="-" \n)

##---------------------Assigning variable---------------------
#number_of_pizzas = (input("Enter the number of pizza"))
#qtypizza = int(number_of_pizzas)

#total_price = number_of_pizzas * price_of_a_pizza
#print(total_price)

##---------------------Inputs---------------------
#product_name = input("Product Name:")
#unit_price = float(input("Unit Price: <Any positive number>"))
#quantity = int(input("Units purchased: <Any WHOLE number>"))
#print("--- Inventory Record ---")
#print("Product:"     , product_name)
#print("Price:"     , unit_price)
#print("Stock:"     , quantity)

##---------------------Math 1---------------------
#Integer Division
#full_boxes = units // 12

#Modulo
#leftovers = units % 12
#
#Exponent
#interest = principle * rate**years

##---------------------Concatenation---------------------
#item = "Keyboard"
#price = 79.99
#sky = "KBD001"
#record = sky + " | " + item + " | " + str(price)
#print(record)

##---------------------F strings---------------------
#Precision and Floats and Spaces
#print(f"{3.14159:.2f}") # 3.14  (f means float and sig fig)
#
#print(f"{3.14159:.4g}")  #3100 4 characters
#
#print(f"{'Python':.2}") #py 2 letters
#
#Output layout
#print(f"{'hello':<6}") #left justified
#
#print(f"{'hello':>6}") #right justified
#
#print(f"{'hello':^6}") #center justified
#
#print(f"{'hi':*^7}") #center justified with an asterisk in blank spots
#
#print(f"{5:+}")
#
#print(f"{5:-}")
#print(f"{5: }")
#
#print(f"{10000000:,}") #Comma seperators
#
#print(f"{10000000:_}")
#
#output = f"{255:#x}" #hex
#print(output)
#
#print(f"{31141592681655218562:e}") #scientific not
#
##print(f"{0.25:%}") #percentages
#
#print(f"{3.14159=:.2f}") #the equals shows the step used to derive answer




###---------------------------------------------------------------Chapter 3---------------------------------------------------------------
##---------------------If statement---------------------
#def check_reorder_threshold(product_name, current_quantity, reorder_level):
#    if current_quantity <= reorder_level:
#        print(f"REORDER ALERT: {product_name}")
#        print(f"  Current stock: {current_quantity} units")
#        print(f"  Reorder level: {reorder_level} units")
#        print(f"  Action required: place purchase order")
#
#
#def main():
#    check_reorder_threshold("Printer Paper", 8, 25)
#    check_reorder_threshold("Ink Pens", 50, 20)
#
#main()

#---------------------#If else statement---------------------
#def calculate_commission_rate(monthly_sales, quota):
#    if monthly_sales>= quota:
#        commission_rate = 0.10
#    else:
#        commission_rate = 0.05
#    return commission_rate

##---------------------Comparing strings---------------------
#def calculate_commission_rate(monthly_sales, quota):       #Checks if sales are over the quota to calculate commission rate
#    if monthly_sales>= quota:
#        commission_rate = 0.10
#    else:
#        commission_rate = 0.05
#    return commission_rate

##---------------------Example if else usage case, calculating commission rate---------------------
#def calculate_commission_rate(monthly_sales, quota):
#    if monthly_sales>= quota:
#        commission_rate = 0.10
#    else:
#        commission_rate = 0.05
#    return commission_rate
#
#def display_commissions(employee_name, monthly_sales, quota):
#    rate = calculate_commission_rate(monthly_sales, quota)
#    commission = monthly_sales * rate
#    status = "Quota Met" if monthly_sales >= quota else "Below Quota"
#
#    print(f"Employee:  {employee_name}")
#    print(f"Sales:  ${monthly_sales:,.2f}")
#    print(f"Status:  {status}")
#    print(f"Rate:  {rate:.0%}")
#    print(f"Commission:  ${commission:,.2f}")
#
#display_commissions("Steve", 10000, 5000)
#display_commissions("Jerry", 2000, 5000)

##---------------------Example alphabetical sorter---------------------
#
#def sort_two_names_alphabetically(name_one, name_two):
#    if name_one.lower() <= name_two.lower():
#        print(name_one)
#        print(name_two)
#    else:
#        print(name_two)
#        print(name_one)
#
#sort_two_names_alphabetically("april","julie")

#def sort_three_names_alphabetically(name_one, name_two, name_three) :
#    a = name_one
#    b = name_two
#    c = name_three
#    
#    if a <= b:
#        if b <= c:
#            print(name_one)
#            print(name_two)
#            print(name_three)
#        else:
#            if a <= c:
#                print(name_one)
#                print(name_three)
#                print(name_two)
#            else:
#                print(name_three)
#                print(name_one)
#                print(name_two)
#    else:
#        if a <= c:
#            print(name_two)
#            print(name_one)
#            print(name_three)
#        else:
#            if b <= c:
#                print(name_two)
#                print(name_three)
#                print(name_one)
#            else:
#                print(name_three)
#                print(name_two)
#                print(name_one)
#
#sort_three_names_alphabetically("Julie", "April", "Bob")

##---------------------If, Elif, Else---------------------

#def determine_commission_tier(monthly_sales) :
    #PLATINUM_THRESHOLD = 100000
    #GOLD_THRESHOLD = 75000
    #SILVER_THRESHOLD = 50000
    #STANDARD_THRESHOLD = 25000

    #if monthly_sales >= PLATINUM_THRESHOLD:
        #commission_rate = 0.15
        #tier_name = "Platinum"
    #elif monthly_sales >= GOLD_THRESHOLD:
        #commission_rate = 0.12
        #tier_name = "Gold"
    #elif monthly_sales >= SILVER_THRESHOLD:
        #commission_rate = 0.09
        #tier_name = "Silver"
    #elif monthly_sales >= STANDARD_THRESHOLD:
        #commission_rate = 0.06
        #tier_name = "Standard"
   # else:
        #commission_rate = 0.03
        #tier_name = "Developing"

   # return tier_name, commission_rate

#tier_name, commission_rate = determine_commission_tier(78000)
#print(tier_name)
#print(commission_rate)
#print(commission_rate * 78000)

##---------------------Logical Operators--------------------
#And operator
#if temperature < 20 and minutes > 12:   
     #print('The temperature is in the danger zone.')
#
#Or operator
#if temperature < 20 or temperature > 100:   
     #print('The temperature is too extreme')
#
#And operator
#if not(temperature > 100):
    #print('This is below the maximum temperature.')

##---------------------Boolean Variables---------------------
#if sales >= 50000.0:
     #sales_quota_met = True
 #else:
     #sales_quota_met = False




###---------------------------------------------------------------Chapter 4---------------------------------------------------------------
##---------------------While Loops (condition-controlled)---------------------
#keep_going = "y"
#while keep_going == 'y':
#    sales = float(input("Enter the sales amoount please (in dollars and cents with no symbols")
#    comm_rate = float(input("What is the rate of commission:  "))
#    commission = sales * (comm_rate/100)
#    print(f'The commisssion is ${commission:,.2f}').
#    keep_going = input("Do i keep going? y or n only")
#
#MAX_TEMP = 102.5 #(Global Constant)
#temperature = (float(input("Enter the celcius: "))
#while temperature > Max_Temp:
#    print("Too high"
#    print("Turn it down and wait five minutees")
#    temperature = float(input("Enter the current celcius temperature")
#
#print('Temperature is fine.')
#
#def demonstrate_while_loop():
#    keep_going = 'y'
#    count = 0
#
#    while keep_going == 'y':
#        count = count + 1
#        print(f"{count}")
#        keep_going = input("Run again? (y/n)")
#
#    print("While loop exited gracefully.")



##---------------------For Loops (count-controlled)---------------------
#Prints values in a list
#for num in [1, 2, 3, 4, 5]:
#    print(num)
#
#for name in ['Ted',
#             'Will',
#             'Matt',]:
#    print(name)
#
#Prints values in a range
#for x in range(5):
#    print(f'Step: {x}')
#for x in range(1,5):
#    print(f'Step: {x}')
#for x in range(1,6):
#    print(f'Step: {x}')
#for x in range(1,10,2):
#    print(f'Step: {x}')
##for x in range(5, 0, -1):
#    print(f'Step: {x}')
#
#def demonstrate_for_range_single():
#    print("Starting Count:")
#    for value in range(10): #assumes start from 0
#        print(f"Value: {value}")
#
#    print("Starting Count:")
#    for value in range(10, 0, -1): #assumes start from 0
#        print(f"Value: {value}")
#
#def demonstrate_for_range_double():
#    print("Starting Doubles Count:")
#    for value in range (1, 11):
#        print(f"Value: {value}")
#
#def demonstrate_for_range_triple():
#    print("Starting Triple Count:")
#    for value in range(1, 11, 1):
#          print(f"Value: {value}")
#          
#    for value in range(10, 0, -1):
#          print(f"Value: {value}")
#
#    for value in range(0, 1100, 5):
#          print(f"Value: {value}")
#
#Calculates conversion from kph to mph in a set range
#START_SPEED = 60
#END_SPEED = 681
#INCREMENT = 10
#CONVERSION_FACTOR = 0.6214
#
#for kph in range(START_SPEED,END_SPEED,INCREMENT):
#                 mph = kph * CONVERSION_FACTOR
#                 print(f'{kph}\t{mph:.1f}')
#
#Prints numbers down from 5 to 1
#for num in range(5, 0, −1):
#   print(num)

#---------------------ACCUMULATORS---------------------
#MAX = 5
#total = 0.0
#
#for counter in range(MAX):
#    number = float(input('Enter a number: '))
#    total = total + number
#    print(number)
#
#print(f'Total is {total}')

#---------------------Advanced Operators ---------------------
#total = total + new_value
#Total += new_value
#
#x = (x + 5)
#x += 5
#
#y = (y - 2)
#y -= 2
#          
#z = (z * 10)
#z *= 10
#          
## = (a / b)
#a /= b
#          
#c = (c % 3)
#c %= 3
#          
#x = (x // 3)
#x //= 3
#          
#y = (y ** 2)
#y ++= 2

##---------------------Sentinel---------------------
#def demonstrate_sentinel():
#    print("enter weight in lbs. (number)")
#    total_weight = 0.0
#    total_number = 0
#
#    weight = float(input("First Weight please: ")) #priming the loop
#    while weight >0:
#        total_weight += weight
#        total_number += 1
#        weight = float(input("Next weight please: "))
#
#    if total_number > 0:
#        avg_weight = total_weight / total_number
#        print(f"{total_weight} / {total_number} = {avg_weight}")
#    else:
#        print("You didnt do anything")

##---------------------Input Validation Loops---------------------
#
#def get_validated_score():
#    score = float(input("Enter exam score (0-100): "))
#    while score < 0 or score > 100:
#        print("Score outside of range, must be between 0 and 100")
#        score = float(input("Re enter the score: "))

##---------------------Nested Loops---------------------
#Nested Matrix
#def demonstrate_nested_matrix():
#    print("Rendering a 3x4")
#    for row in range (1, 4):
#        print(f"Row! {row}: ", end="")
#        for column in range (1,5) :
#            print(f"[{row}, {column}]", end="")
#        print()
#    print()
#
#Simulated Clock
# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#            print(hours, ':', minutes, ':', seconds)




###---------------------------------------------------------------Chapter 5---------------------------------------------------------------
##---------------------Functions---------------------
# def message():
#     print('I am Arthur,')
#     print('King of the Britons.')
#
# message()  #Executes the two prints

##---------------------Functions---------------------
#def main():
#     get_name()
#     print(f'Hello {name}.')      # Local Variable
#def get_name():
#     name = input('Enter your name: ')  
#main()

##---------------------Passing Arguments to Functions---------------------
# This program demonstrates an argument being passed to a function.
#def main():
#    value = 5
#    show_double(value)
# The show_double function accepts an argument and displays double its value.
#def show_double(number):
#    result = number * 2
#    print(result)
#
#main()
#
#Passing Multiple Arguments
# This program demonstrates a function that accepts two arguments.
#def main():
#    print('The sum of 12 and 45 is')
#    show_sum(12, 45)
# The show_sum function accepts two arguments and displays their sum.
#def show_sum(num1, num2):
#    result = num1 + num2
#     print(result)
#     
#main()
#

##---------------------Generating Random Numbers (Value-Returning Functions)---------------------
#Randomness functions
#import math
#import random
#
#import random
#
#def roll_die():
#    return random.randint(1,6)
#
#def choose_multiple_of_ten():
#    return random.randrange(10,51,10)
#
#def get_probability_number():
#    return random.random()
#
#def choose_measurement():
#    return random.uniform(1.0, 5.0)
#
#def display_results(die, multiple, probability, measurement):
#    print(f"Die roll: {die}")
#    print(f"Multiple of ten: {multiple}")
#    print(f"Number from 0 to below 1: {probability:.4f}")
#    print(f"Measurement: {measurement:.2f}")
#
#def main():
#    die = roll_die()
#    multiple = choose_multiple_of_ten()
#    probability = get_probability_number()
#    measurement = choose_measurement()
#    display_results(die, multiple, probability, measurement)
#
#main()
#
#
#Deck of Cards
#import random
#random.seed(50)
#
#def cards():
#    draw = random.randint(1,13)
#    if draw == 1:
#        card = "Ace of"
#    elif draw == 2:
#        card = "Two of"
#    elif draw == 3:
#        card = "Three of"
#    elif draw == 4:
#        card = "Four of"
#    elif draw == 5:
#        card = "Five of"
#    elif draw == 6:
#        card = "Six of"
#    elif draw == 7:
#        card = "Seven of"
#    elif draw == 8:
#        card = "Eight of"
#    elif draw == 9:
#        card = "Nine of"
#    elif draw == 10:
#        card = "Ten of"
#    elif draw == 11:
#        card = "Jack of"
#    elif draw == 12:
#        card = "Queen of"
#    else:
#        card = "King of"
#
#    suit = random.randint(1,4)
#    if suit == 1:
#        card_suit = "Spades"
#    elif suit == 2:
#        card_suit = "Clubs"
#    elif suit == 3:
#        card_suit = "Hearts"
#    else:
#        card_suit = "Diamonds"
#
#    print(card,card_suit)
#
#def main():
#    cards()
#
#main()

##---------------------Returning Boolean Values---------------------
# number = int(input('Enter a number: '))
# if (number % 2) == 0:
#     print('The number is even.')
# else:
#     print('The number is odd.')

##---------------------Math Module---------------------
#import math
#
#def demonstrate_basic_arithmetic():
#    #round up
#    ceil_result = math.ceil(4.15)
#    print(ceil_result)
#    
#    #Round down
#    floor_result = math.floor(4.89)
#    print(floor_result)
#    
#    #Truncation
#    trunc_result = math.trunc(-3.78)
#    print(trunc_result)
#
#    #absolute value
#    abs_result = math.fabs(-25.5)
#    print(abs_result)
#
#    #greatest common demoninator 
#    gcd_result = math.gcd(48, 18)
#    print(gcd_result)
#
#    #least common multiple
#    lcm_result = math.lcm(4, 6)
#    print(lcm_result)
#
#    fmod_result = math.fmod(10.5, 3.0)
#    print(fmod_result)
#
#
#def demonstrate_powers_and_logs():
#    power_result = math.pow(2, 5)
#    print(pow_result)
#
#    sqrt_result = math.sqrt(64)
#    print(sqrt_result)
#
#    isqrt_result = math.isqrt(10)
#    print(isqrt_result)
#
#    ln_result = math.log(7.3891)
#    print(ln_result)
#
#    log2_custom = math.log(16, 2)
#    print(log2_custom)
#
#    log10_result = math.log10(1000)
#    print(log10_result)
#
#    
#
#demonstrate_basic_arithmetic()
#
#Additional Functions
#test = math.hypot(a,b)
#test = math.acos(x)
#test = math.asin(x)
#test = math.atan(x)
#test = math.degrees(x)
#test = math.cos(x)
#test = math.exp(x)
#test = math.radians(x)
#test = math.sin(x)
#test = math.tan(x)
#
#Base Package Variables
#print(math.pi)
#print(math.e)
#
#
###---------------------------------------------------------------Scientific Calculator---------------------------------------------------------------
##The goal is to create a series of loops that ask for an input of numbers as well as the operator required
#import math
#
#
##Give the user a list of usable operators
#def choose_operator():
#    valid = False
#    while valid != True:
#        print("List of Valid Operators:\nAdd, Subtract, Multiply, Divide,\nPower, NaturalLog, Logarithm, SquareRoot,\nSine, Cosine, Tangent, ASine,\nACosine, ATangent, Radians, Degrees.") 
#        operator = input("\nWhich operation would you like to solve?:" )
#        if operator == "Add" or operator == "Subtract" or operator == "Multiply" or operator == "Divide" or operator == "Power" or operator == "NaturalLog" or operator == "Logarithm" or operator == "SquareRoot" or operator == "Sine" or operator == "Cosine" or operator == "Tangent" or operator == "ASine" or operator == "ACosine" or operator == "ATangent" or operator == "Radians" or operator == "Degrees":
#            valid = True
#        else:
#            valid = False
#            print("Invalid operator, please choose a valid operator! (Case Sensitive)\n")
#    return operator
#
#        
#
#
##Ask the user to pick numbers to use in that operator
#def choose_numbers(operator):
#    num_one = None
#    num_two = None
#    if operator == "Add":
#        print("Which two numbers would you like to add?:" )
#        num_one = float(input("First Number: " ))
#        num_two = float(input("Second Number: " ))
#    elif operator == "Subtract":
#        print("Which two numbers would you like to subtract? (First minus Second):" )
#        num_one = float(input("First Number: " ))
#        num_two = float(input("Second Number: " ))
#    elif operator == "Multiply":
#        print("Which two numbers would you like to multiply?:" )
#        num_one = float(input("First Number: " ))
#        num_two = float(input("Second Number: " ))
#    elif operator == "Divide":
#        print("Which two numbers would you like to divide? (First number divided by Second):" )
#        num_one = float(input("First Number: " ))
#        num_two = float(input("Second Number: " ))
#        while num_two == 0:
#            num_two = float(input("Second Number cant be 0, try again: " ))
#    elif operator == "Power":
#        print("Which two numbers would you like to use the power operator on? (First number to the power of the Second number):" )
#        num_one = float(input("First Number: " ))
#        num_two = float(input("Second Number: " ))
#    elif operator == "NaturalLog":
#        print("Which number would you like to use the Natural Log operator on?:" )
#        num_one = float(input("First Number: " ))
#        while num_one <= 0:
#            num_one = float(input("Number can not be negative or 0 for this operation, try again: "))
#    elif operator == "Logarithm":
#        print("Which two numbers would you like to use the logarithm operator on? (Second number is the base of the logarithm):" )
#        num_one = float(input("First Number: " ))
#        num_two = float(input("Second Number: " ))
#        while num_one < 1:
#            num_one = float(input("First number can not be lower than 1 for this operation, try again: "))
#        while num_two < 2:
#            num_two = float(input("Second number can not be 1 or lower for this operation, try again: "))
#    elif operator == "SquareRoot":
#        print("Which number would you like to find the square root of?:" )
#        num_one = float(input("First Number: " ))
#        while num_one < 0:
#            num_one = float(input("Number can not be negative for this operation, try again: "))
#    elif operator == "Sine":
#        print("Which number would you like to find the sine of?:" )
#        num_one = float(input("First Number: " ))
#    elif operator == "Cosine":
#        print("Which number would you like to find the cosine of?:" )
#        num_one = float(input("First Number: " ))
#    elif operator == "Tangent":
#        print("Which number would you like to find the tangent of?:" )
#        num_one = float(input("First Number: " ))
#    elif operator == "Degrees":
#        print("Which number would you like to convert to degrees:" )
#        num_one = float(input("First Number: " ))
#    elif operator == "Radians":
#        print("Which number would you like to convert to radians?:" )
#        num_one = float(input("First Number: " ))
#    elif operator == "ASine":
#        print("Which number would you like to find the arcsine of?:" )
#        num_one = float(input("First Number: " ))
#        while num_one > 1 or num_one < -1:
#            num_one = float(input("Number can not be greater than 1 or less than -1 for this operation, try again: "))
#    elif operator == "ACosine":
#        print("Which number would you like to find the arccosine of?:" )
#        num_one = float(input("First Number: " ))
#        while num_one > 1 or num_one < -1:
#            num_one = float(input("Number can not be greater than 1 or less than -1 for this operation, try again: "))
#    elif operator == "ATangent":
#        print("Which number would you like to find the arctangent of?:" )
#        num_one = float(input("First Number: " ))
#    else:
#        print("Invalid operator, please choose a valid operator!")
#    return num_one, num_two
#
##Actually execute the operation
#
#def run_operation(operator, first_number, second_number):
#    if operator == "Add":
#        solution = (first_number + second_number)
#    elif operator == "Subtract":
#        solution = (first_number - second_number)
#    elif operator == "Multiply":
#        solution = (first_number * second_number)
#    elif operator == "Divide":
#        solution = (first_number / second_number)
#    elif operator == "Power":
#        solution = (first_number ** second_number)
#    elif operator == "NaturalLog":
#        solution = math.log(first_number)
#    elif operator == "Logarithm":
#        solution = math.log(first_number, second_number)
#    elif operator == "SquareRoot":
#        solution = math.sqrt(first_number)
#    elif operator == "Sine":
#        solution = math.sin(first_number)
#    elif operator == "Cosine":
#        solution = math.cos(first_number)
#    elif operator == "Tangent":
#        solution = math.tan(first_number)
#    elif operator == "Degrees":
#        solution = math.degrees(first_number)
#    elif operator == "Radians":
#        solution = math.radians(first_number)
#    elif operator == "ASine":
#        solution = math.asin(first_number)
#    elif operator == "ACosine":
#        solution = math.acos(first_number)
#    elif operator == "ATangent":
#        solution = math.atan(first_number)
#    else:
#        print("You have errored at some point, please restart")
#    print(solution)
#
#
#
#
#def main():
#    operator = choose_operator()
#    first_number, second_number = choose_numbers(operator)
#    run_operation(operator, first_number, second_number)
#
#main()
