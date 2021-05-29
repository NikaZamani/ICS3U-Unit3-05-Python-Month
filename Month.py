#!/usr/bin/env python3

# Created by: Nika Zamani
# Created on: April 2021
# This program will display the month of the year that represents that number

def main():
    # this function displays the month of the year that represents that number

    # input
    Month = int(input("Enter the number of a month: "))

    # process & output
    if (Month == 1):
        print("It is January.")
    elif (Month == 2):
        print("It is February.")
    elif (Month == 3):
        print("It is March.")
    elif (Month == 4):
        print("It is April.")
    elif (Month == 5):
        print("It is May.")
    elif (Month == 6):
        print("It is June.")
    elif (Month == 7):
        print("It is July.")
    elif (Month == 8):
        print("It is August.")
    elif (Month == 9):
        print("It is September.")
    elif (Month == 10):
        print("It is October.")
    elif (Month == 11):
        print("It is November.")
    elif (Month == 12):
        print("It is December.")
    else:
        print("Invalid Month!")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
