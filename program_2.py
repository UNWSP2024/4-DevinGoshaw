# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.
#programmer: Devin Goshaw 
#Date: 9/26/2025
#program: Ticket program
def main():
    ######################
    totalTickets = 0
    ticket=4
    while ticket != 0:
        movie = input('What movie do you want to see: ')
        ticket = int(input('How many tickets do you want: '))


        print('Movie:', movie)
        print('Tickets:', ticket)
        

        totalTickets += ticket

    print('Total tickets:', totalTickets)

    ######################


if __name__ == '__main__':
    main()