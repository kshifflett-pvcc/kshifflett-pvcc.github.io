# Names: Kayla Shifflett
# Program Purpose: This program calculates the price of pizzas of differing sizes.
#   Small pizza = $9.99/each
#   Medium pizza = $12.99/each
#   Large pizza = $14.99/each
#   Extra large pizza = $17.99/each
#   Sales tax rate: 5.5%


import datetime

######## define global variables #########
# define prices based on size
SMALL = 9.99
MEDIUM = 12.99
LARGE = 14.99
X_LARGE = 17.99

SALES_TAX = 0.55

# define global variables
size = ""
quantity = 0
subtotal = 0
sales_tax = 0
total = 0
price = 0
size_name = ""


######## define program functions ########
def main():
    more_data = True
    while more_data:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to order more pizzas? (Y/N) : ")
        if yesno == "n" or yesno == "N":
            more_data = False
            print("Thank you for using this program!")
            print("To see my other programs, go to: \n\thttps://kshifflett-pvcc.github.io/")
            

def get_user_data():
    global size, quantity
    size =(input("Job category:\nEnter\n S for Small \n M for Medium \n L for Large \n X for Extra Large."))
    quantity = int(input("How many pizzas would you like?: "))

def perform_calculations():
    global size, quantity, subtotal, sales_tax, total, price, size_name
    if size == "S" or size == "s":
        size_name = 'Small'
        price = SMALL
        subtotal = SMALL * quantity
        sales_tax = SALES_TAX * subtotal
        total = sales_tax + subtotal

    if size == "M" or size == "m":
        size_name = 'Medium'
        price = MEDIUM
        subtotal = MEDIUM * quantity
        sales_tax = SALES_TAX * subtotal
        total = sales_tax + subtotal

    if size == "L" or size == "l":
        size_name = 'Large'
        price = LARGE
        subtotal = LARGE * quantity
        sales_tax = SALES_TAX * subtotal
        total = sales_tax + subtotal

    if size == "X" or size == "x":
        size_name = 'Extra Large'
        price = X_LARGE
        subtotal = X_LARGE * quantity
        sales_tax = SALES_TAX * subtotal
        total = sales_tax + subtotal

def display_results():
    line = '------------------------------------'
    print(line)
    print('****       Palermo Pizza        ****')
    print('**** Delicious Pizza Made Fresh ****')
    print(line)
    print('Order Summary:                           ')
    print(size_name      + '   ' '     $ '             + format(price, '8,.2f'))
    print('Quantity:      '   + format(quantity, '8,'))
    print('                                         ')
    print('Subtotal     $ ' + format(subtotal,  '8,.2f'))
    print('Sales Tax    $ ' + format(sales_tax, '8,.2f'))
    print('Total        $ ' + format(total,     '8,.2f'))
    print(line)
    print(str(datetime.datetime.now()))
            
######### call on main program to execute ########
main()
