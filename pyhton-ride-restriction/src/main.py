# File: /height-restriction-ride/height-restriction-ride/src/main.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.height_check import check_height

def main():
    ride_capacity = 8
    current_riders = 0

    print(f"Welcome to the ride! The ride can accommodate {ride_capacity} riders at a time.")

    while current_riders < ride_capacity:
        print(f"\nCurrent riders: {current_riders}/{ride_capacity}")
        name = input("Please enter your name (or type 'exit' to quit): ")

        if name.lower() == 'exit':
            print("Thank you for visiting the ride!")
            break

        height = input(f"Hello {name}, please enter your height in cm: ")

        try:
            height = int(height)
            result = check_height(height)
            print(result)

            if result == "You are allowed to ride alone.":
                current_riders += 1
                print(f"Welcome aboard, {name}!")
            elif result == "You are allowed to ride but must be accompanied by an adult.":
                current_riders += 2  # Increment by 2 for the rider and the accompanying adult
                print(f"Welcome aboard, {name}! Please ensure you are accompanied by an adult.")
            elif result == "You are not allowed to ride.":
                print(f"Sorry {name}, you are a very short person and you may die if you take this ride .... BYE!")
        except ValueError:
            print("Please enter a valid number for height.")

    if current_riders >= ride_capacity:
        print("\nThe ride is full. Please wait for the next round.")

if __name__ == "__main__":
    main()