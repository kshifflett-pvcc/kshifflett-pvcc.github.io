# Name: Kayla Shifflett
# Program Purpose: This program finds the cost for PVCC Tuition and Fees for In-State and Out-of-State students.
#   In-State Tuition and Fees:
#       Tuition: $155.00 per credit
#       Institutional fee: $1.75 per credit
#       Student activity fee: $2.90 per credit
#   Out-of-State Tuition and Fees:
#       Tuition: $331.60 per credit
#       Capital fee: $23.50 per credit
#       Institutional fee : $1.75 per credit
#       Student activity fee: $2.90 per credit

import datetime

######## define global variables #########
# define tuition rate and fees
TUITION_IN = 155.00
TUITION_OUT = 331.60
INST_FEE = 1.75
STU_ACT_FEE = 2.90
CAP_FEE = 23.50

# define global variables
residency = 1
num_cred = 0
scholar_amt = 0
total = 0
balance = 0

######## define program functions ########
def main():
    more_data = True
    while more_data:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nDo you want to calculate more tuition costs? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more_data = False
            print("Thank you for using this program!")
            print("To see my other programs, go to: \n\thttps://kshifflett-pvcc.github.io/")
            

def get_user_data():
    global residency, num_cred, scholar_amt
    residency = int(input("Residency status:\nEnter\n 1 for In-State \n 2 for Out-of-State"))
    num_cred = int(input("Number of credits: "))
    scholar_amt = int(input("Amount of scholarship awarded: "))

def perform_calculations():
    global tuition_amt, inst_amt, stu_act_amt, cap_amt, total, balance
    if residency == 1:
        tuition_amt = num_cred * TUITION_IN
        cap_amt = 0
        
    else:
        tuition_amt = num_cred * TUITION_OUT
        cap_amt = num_cred * CAP_FEE

    inst_amt = num_cred * INST_FEE
    stu_act_amt = num_cred * STU_ACT_FEE
    total = tuition_amt + inst_amt + stu_act_amt + cap_amt
    balance = total - scholar_amt

def display_results():
    line = '----------------------------------------------'
    print(line)
    print('**** Piedmont Virgninia Community College ****')
    print('****       Tuition and Fees Report        ****')
    print(line)
    print('Tuition                    $ ' + format(tuition_amt, '8,.2f'))
    print('Capital fee                $ ' + format(cap_amt,     '8,.2f')) 
    print('Institution fee            $ ' + format(inst_amt,    '8,.2f'))
    print('Student activity fee       $ ' + format(stu_act_amt, '8,.2f'))
    print('Total                      $ ' + format(total,       '8,.2f'))
    print('Balance                    $ ' + format(balance,     '8,.2f'))
    print(line)
    print(str(datetime.datetime.now()))
            
######### call on main program to execute ########
main()
