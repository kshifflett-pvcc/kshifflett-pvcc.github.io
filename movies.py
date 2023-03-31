# Name: Kayla Shifflett
# Program Purpose: This program finds the cost of movie tickets.
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

######## define global variables #########
# define tax rate and prices
SALES_TAX_RATE = 0.55
PR_TICKET = 10.99

# define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

######## define program functions ########
def main():
    more_data = True
    while more_data:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nDo you want to process more data? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more_data = False
            print("Thank you for using this program!")
            print("To see my other programs, go to: \n\thttps://kshifflett-pvcc.github.io/")
            

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('-----------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('-----------------------------')
    print('Tickets     $ ' + format(subtotal, '8,.2f'))
    print('Sales Tax   $ ' + format(sales_tax,'8,.2f'))
    print('Total       $ ' + format(total,       '8,.2f'))
    print('-----------------------------')
    print(str(datetime.datetime.now()))
            
######### call on main program to execute ########
main()
