# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.
#Programmer: Devin Goshaw
# Date:9/25/2025
# Title: budget calculator program 

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         
    total = 0.0

    ######################
    budget=float(input('enter monthly budget: '))
    while spent>0:
        spent=float(input('enter expense:'))
        total = total + spent
    
    difference=budget-total
    if difference>=0:
        print('nice job you are',difference,'under budget',)
    else:
        print('better luck next month you are',-difference,'dollars over budget')
    ######################


if __name__ == '__main__':
    main()