"""
This file is meant to be used to call the functions defined in the other files of this project.
This code is given to you in order for you to see how the functions in the other files could be called.
Feel free to comment/uncomment or otherwise modify any line of code in this file as you wish.
"""

#### VIRUS TRANSMISSION ####
# calculate how many people will be infected by a population of 10 infected people over 14 days, assuming a transmission rate of 1.2
from virus_transmission import calculate_infections

starting_infections = 2
reproduction_rate = 1.1
num_days = 62
total_infections = calculate_infections(
    starting_infections, reproduction_rate, num_days
)  # calculate total infections
print(
    "{} people will go on to create a total of {} infections over {} days, assuming a reproduction rate of {}".format(
        starting_infections, total_infections, num_days, reproduction_rate
    )
)


# #### NUMBER GUESSING ####
# ask the user to guess a number between 1 and 10... give them 5 attempts
from number_guessing import guess_number

if guess_number(1, 10, 5):
    print("You guessed correctly!")  # they guessed correctly!
else:
    print("Sorry, all your guesses were incorrect!")  # they guessed incorrectly!


# #### FOR LOOPING TURTLES ####
# draw four overlapping squares, and then a five-pointed star
from loopy_turtles import create_turtle, draw_square, draw_star

t = create_turtle("red", "yellow")  # create a turtle object
for x in range(-200, 0, 25):  # loop four times
    draw_square(t, x, x, 100, "left", "#F5DEB3")  # draw a square

draw_star(t, 200, 200, 100, 120, "right", "red")  # draw a five-pointed star
