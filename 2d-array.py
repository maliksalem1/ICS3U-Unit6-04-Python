#!/usr/bin/env python3

# Created by: maliksalem1
# Created on: Dec 2022
# This program generates a 2d array

import random


def average_of_numbers(rows, columns, passed_list):
    # This function gets the average

    total = 0
    for row_value in passed_list:
        for single_number in row_value:
            total += single_number
    total = total / (rows * columns)

    return total


def main():
    # This function uses the list

    a_2d_list = []

    # input
    rows = input("How many rows would you like: ")
    columns = input("How many columns would you like: ")

    try:
        rows_integer = int(rows)
        columns_integer = int(columns)

        for counter in range(0, rows_integer):
            temp_column = []
            for counter in range(0, columns_integer):
                random_number = random.randint(0, 50)
                temp_column.append(random_number)
                print("{0} ".format(random_number), end="")
            a_2d_list.append(temp_column)
            print("")

        # calls function
        average = average_of_numbers(rows_integer, columns_integer, a_2d_list)
        print("\nThe average of the numbers is: {0}".format(average))
    except Exception:
        print("\nInvalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
