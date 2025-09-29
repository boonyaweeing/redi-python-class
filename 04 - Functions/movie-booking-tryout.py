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

is_valid =  True


def display_movies():
    for movie in movies:
        print(f"{movie} with available showtime {movies[movie]}")

def check_movie(movie_to_check):
    if movie_to_check in movies:
        print("The movie you chose is valid")
        is_valid = True
    else:
        #print("The movie you chose is invalid")
        raise Exception("The movie you chose is invalid")
        is_valid = False

    
def check_time(movie, time_to_check):
    if time_to_check in movies[movie]:
        print("The time you chose is valid")
        is_valid = True
    else:
        #print("The time you chose is invalid")
        raise Exception("The movie you chose is invalid")
        is_valid = False
    
def cal_price(amount, seat_type):
    total = 0
    if seat_type.lower() == "r":
        total = int(amount) * 18
    elif seat_type.lower() == "vip":
        total = int(amount) * 25
    return total

def check_type(type):
    if type == "r":
        return "regular"
        is_valid = True
    elif type == "vip":
        return "VIP"
        is_valid = True
    else:
        raise Exception("The type you chose is invalid")
        is_valid = False
    
def confirm(movie, time, amount, type):
    print("---Booking confirmed---")
    print(f"{amount} {type} tickets for {movie} | showtime: {time} | total price: {cal_price(amount, type)}")
    print("Enjoy the show!")


def ask_and_comfirm():
    selected_movie  = input("Enter the movie you want to watch: ")
    check_movie(selected_movie)
    selected_time = input("Enter the time you want to watch: ")
    check_time(selected_movie, selected_time)
    amount_of_tickets = input("Enter the number of tickets: ")
    type_of_tickets = input("Enter the type of tickets ('R' for Regular/'V' for VIP): ")
    print(f"Booking {amount_of_tickets} {check_type(type_of_tickets)} ticket(s) for {selected_movie}")
    if is_valid:
        confirm(selected_movie, selected_time, amount_of_tickets, type_of_tickets)
    else:
        print("Some information  is invalid. Please try again.")
        return None






def main():
    while True:
        display_movies()
        ask_and_comfirm()


main()


