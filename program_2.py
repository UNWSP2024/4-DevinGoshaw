# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    
    while True:
        movie=input('what movie do you want to see: ')
        ticket=int(input('how many tickest do you want: '))
        print('movie:',movie)
        print('Tickets:',ticket)

    ######################


if __name__ == '__main__':
    main()