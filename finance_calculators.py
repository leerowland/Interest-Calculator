
import math

# Option menu for user to determine which calculator to use
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
user_input = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()


# User input info for investment option
if user_input == "investment":
    invest_amount = float(input("\nPlease enter the amount you wish to deposit: £"))
    interest_rate = float(input("\nPlease enter your percentage interest rate: ")) / 100
    invest_years = int(input("\nPlease enter the number of years you plan on investing this for: "))
    interest = input("\nWould you like simple or compound interest?: ").lower()

# Variables assigned and calculated for both interest types
    simple_int = round(invest_amount * (1 + (interest_rate * invest_years)),2)
    compound_int = round(invest_amount * (math.pow((1 + interest_rate), invest_years)),2)

# User input for which interest type they would like displayed
    if interest == "simple":
        print(f"\nAfter {invest_years} years, you will have £" + str(simple_int))
    elif interest == "compound":
        print(f"\nAfter {invest_years} years, you will have £" + str(compound_int))
    else:
        print(f"You have entered your interest type as '{interest}', this is not a supported interest type, please restart the calculator and choose either 'simple' or 'compound'.")


# User input info for bond option
elif user_input == "bond":
    loan_value = int(input("\nPlease enter the present value of the house: £"))
    interest_rate = ((float(input("\nPlease enter your percentage interest rate: "))) / 100) / 12
    loan_term = int(input("\nPlease enter the number of months over which you plan to repay your loan: "))

# Monthly repayment calculated and displayed
    monthly_repayment = round((interest_rate * loan_value) / (1 - (math.pow((1+interest_rate),(- loan_term)))),2)

    print("\nYour monthly repayment will be £" + str(monthly_repayment) + f" per month for a period of {loan_term} months")


# Error message if user inputs incorrect menu option
else:
    print(f"The option '{user_input}' is not recognised, please restart the calculator and choose an item from the menu.")

 