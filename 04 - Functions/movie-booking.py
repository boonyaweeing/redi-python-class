"""
For this exercise, we want a Python program that will let us book movie tickets!

The final part of the exercise will need the program to do the following:
- Display the available movies.
- Prompt the user to select a movie.
- Ask the user for the number of tickets and seat type (optional).
- Book the tickets and display the total cost.

Let's break down each part:

1. Displaying available movies

Define a function that displays a predefined list of movies, and asks the user to enter the movie they want to watch.

```
Available movies:
Inception
The Matrix
Interstellar
The Dark Knight
```

2. Ask the user for which movie they want to watch, how many tickets they want to book, and the type of seat they want. Make the type of seat optional (default to a Regular seat).

```
Enter the movie you want to watch: Inception
Enter the number of tickets: 2
Enter the seat type (Regular/VIP):
Booking 2 Regular ticket(s) for Inception
```

3. Calculate the ticket costs depending on the tickets and type of seats booked, and show this to the user

```
Total cost: $24 (2 x $12 Regular Seats)
```

4. Try to organize the above features each as its own function. If you feel like some parts need its own function, e.g. calculating costs should be separate from displaying it, then try to organize it that way!

5. Put it together in a function called `main` (this is conventionally how a lot of programmers called the entry point of their program), and you can run it by adding the following bit at the end of your script, like so

```py
def main():
    display_movies()
    book_tickets()
    # ...

if __name__ == "__main__":
    main()
```
"""



"""
Problem Statement for a simple and modular movie ticket booking program is as below.

Favourite movies (good choices, guys :) ):
1. Terminator 2 
2. Interstellar
3. Blacklist
4. Home Alone
5. The Pursuit of Happiness

Showtimes:
M, A, E (M - Morning, A - Afternoon, E - Evening)

Features:
1. Available movies & showtimes
2. Seats - number of tickets, regular/vip/ dbox
3. Ticket price - 18 EUR, 25 EUR
4. Show the booking confirmation

Here's the code we came up with for a simple and modular movie ticket booking program 
"""
# Dictionary of movies and their showtimes 
# Note: This dictionary is declared outside of functions so that it can be accessed globally
# Feel free to experiment with declaring it inside a function, or passing it as a parameter to functions (will be covered in the 2nd class)

movies = {
        "Terminator 2": ["M", "E"],
        "Interstellar" : ["M", "A"],
        "Blacklist": ["M", "A", "E"],
        "Home Alone": ["E"],
        "The Pursuit of Happiness": ["M", "A"]
    }
# Remember the names are case-sensitive! The input should match exactly with the keys in this dictionary

# Function to display available movies and their showtimes to the user
def movie_program():
    print("This is today's movie program:")

    for movie in movies:
        print(f"{movie} at show slot {movies[movie]}");

# Function to ask user for chosen movie and showtime, and validate the input
def ask():
    title = input(f"What movie?"); # User input for movie title
    # After the user enters a movie title in the terminal, we check if it's valid
    # Don't forget to enter an input in the terminal :)

    if title in movies:
        print("Movie is valid");
        # TODO: This message could be improved by showing the available showtimes for the chosen movie.
        
        show_time = input(f"What time?");
        if show_time in movies[title]:
            print("Time is valid!");
            # I forgot to add this line during the live coding, but return the chosen title and show_time
            return title, show_time # return both title and show_time as a tuple
                  
        else:
            print("Time is invalid :( Try Again")
            return None # break out of the function

    else:
        print("Invalid :( Try Again")
        return None # break out of the function
    
# Main program execution 
movie_program()
movie_info = ask() # Call the ask function and store the returned value

#------------------------------------------------------------------------------
# This is where we reached at the end of class   
#------------------------------------------------------------------------------

# This is an idea of how I would continue the program in the first way that comes to my mind
# Future steps:
# 1. Ask for number of tickets  
# 2. Ask for seat type (1st class/ vip/ dbox)
# 3. Calculate ticket price based on seat type and number of tickets
# 4. Show the booking confirmation

# Dictionary of seat types and their prices (again, declared outside of functions)
seat_types = {
    "regular": 15,
    "vip": 18,
    "dbox": 20
}

# Function to ask user for number of tickets and seat type, and validate the input
def get_seat_info():
    seat_number = input("How many tickets?");
    if not seat_number.isdigit() or int(seat_number) <= 0:
        print("Invalid number of tickets! Try Again")
        return None # break out of the function if invalid seat number
    else:
        seat_type = input(f"What type of seat? {list(seat_types.keys())}"); # show available seat types to the user
        if seat_type not in seat_types:
            print("Invalid seat type! Try Again")
            return None # break out of the function if invalid seat type
        else:
            #return seat_number, seat_type # return info as strings (default)
            return int(seat_number), seat_type # return seat_number as specified integer  

seat_info = get_seat_info() # Call the get_seat_info function and store the returned value
# You can add an if condition to check if movie_info is valid (not None) before proceeding to get seat info
# This is left out for simplicity, but feel free to experiment and implement it

# Function to calculate total price based on number of tickets and seat type
def calculate_total_price(seat_info):
    return seat_info[0] * seat_types[seat_info[1]]
    # seat_info is a tuple (seat_number, seat_type)
    # if seat_info[0] is not an integer (like if you use the code in line 99), 
    # this will raise an error! You can convert it to int using int(seat_info[0]) in this function if needed.

def show_booking_confirmation(movie_info, seat_info, total_price):
    print("\nBooking Confirmation:")
    print(f"Movie: {movie_info[0]}")
    print(f"Showtime: {movie_info[1]}")
    print(f"Number of tickets: {seat_info[0]}")
    print(f"Seat type: {seat_info[1]}")
    print(f"Total price: {total_price} EUR")
    print(f"Enjoy your movie :)")
    # You can also call the calculate_total_price function here instead of passing total_price as a parameter


if movie_info and seat_info: 
    # Proceed only if both movie_info and seat_info are valid (that is, their return value is not None)    
    
    # Calculate total price
    total_price = calculate_total_price(seat_info) # Call the function to calculate total price
    
    # Optional: Unpack the tuples for easier access using the line below
    # title, show_time = movie_info # unpack the movie_info tuple into title and show_time
    # Else, you can access the same using movie_info[0] and movie_info[1] like below

    # Show booking confirmation manually
    #print("\nSucess! Your booking is confirmed!")
    #print(f"Movie: {movie_info}")
    #print(f"Showtime: {movie_info[1]}")
    #print(f"Number of tickets: {seat_info[0]}")
    #print(f"Seat type: {seat_info[1]}")
    #print(f"Total price: {total_price} EUR")
    #print(f"Enjpoy your movie :)")

    # Or, call the function to show booking confirmation
    show_booking_confirmation(movie_info, seat_info, total_price)

# NOTE: The program currently does not loop back to ask for inputs again if the user enters invalid data.
# This can be implemented using while loops, which we briefly discussed in the class.   
# Feel free to experiment and let us know how it goes!  
 