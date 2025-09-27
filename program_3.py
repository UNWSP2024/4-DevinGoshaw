# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.
# programmer: Devin Goshaw
# date: 9/25/2025
# program: rainfall calculator program 

def main():
    ######################
    years = int(input('Enter the number of years you want to track: '))

    total_rainfall = 0
    total_months = years * 12

    for year in range(1, years + 1):
        print("\nYear" ,year)

        for month in range(1, 13):
            rainfall=float(input('enter how much rainfall for month '+str(month)+':' ))
            month=month+1
            total_rainfall += rainfall

    average_rainfall = total_rainfall / total_months

    print("\nRainfall information")
    print("Total months:",total_months)
    print("Total rainfall: ",round(total_rainfall,2), "inches")
    print("Average rainfall per month:",round(average_rainfall,2),"inches")
    ######################    

if __name__ == '__main__':
    main()