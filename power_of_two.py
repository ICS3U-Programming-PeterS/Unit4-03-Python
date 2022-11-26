#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Nov 19, 2022
# This program gets a positive number from the user
# It then calculates and displays the squares up until that number, from 0.


def main():
    # initialize the counter
    loop_counter = 0

    # Get the positive number from the user
    user_number_string = input("Enter a positive number: ")
    print()

    # try catch for erroneous/invalid input
    try:
        # convert the users number to a integer
        user_number = int(user_number_string)
        # Make sure the user inputted a positive number
        if user_number > 0:
            # calculate the squares of all numbers from 0 to the users number
            for loop_counter in range(user_number + 1):
                power_of_two = loop_counter**2
                print("{}^2 = {}".format(loop_counter, power_of_two))
                loop_counter += 1

        else:
            # Tell the user they can't enter a negative number
            print("You entered a negative number, please try again.")
    except Exception:
        # Statement when an exception is encountered
        print("{} is not an integer.".format(user_number_string))
    finally:
        # Finally statement to thank the user fro playing
        print()
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
