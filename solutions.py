"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    total_sales= int(input("enter the amount of total sales: "))
    profit=float((total_sales*23)/100)
    print("\"profit: ", profit, "\" for sales of " , total_sales)



def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    # Asking the user to input two integers
    number1 = int(input("Enter number #1: "))
    number2 = int(input("Enter number #2: "))

    # Calculating quotient and remainder
    quotient = int( number1 // number2)
    remainder = (number1 % number2)

    # Output
    print(f"{number2} goes into {number1} a total of {quotient} times with a remainder of {remainder}")


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    # Asking the user to input the number of miles driven
    miles_driven = float(input("Miles driven: "))
    
    # Asking the user to input the gallons of gas used
    gas_used = float(input("Gas used (gallons): "))
    
    # Calculating the car's MPG
    mpg = miles_driven / gas_used
    
    # Result
    print(f"Miles per gallon: {mpg }")

def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    # Asking the user to input 3 price values as floating point numbers
    price1 = float(input("Enter price #1: "))
    price2 = float(input("Enter price #2: "))
    price3 = float(input("Enter price #3: "))

    # Formatting the prices to two decimal places and aligning them
    formatted_price1 = f"${price1:10.2f}"
    formatted_price2 = f"${price2:10.2f}"
    formatted_price3 = f"${price3:10.2f}"

    # Printing the formatted prices
    print("\nHere are formatted prices!\n")
    print(f"Price #1: {formatted_price1}")
    print(f"Price #2: {formatted_price2}")
    print(f"Price #3: {formatted_price3}")
