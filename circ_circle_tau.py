#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: September 28, 2023
# This program Calculates the circumference of a circle with
# the imputed dimensions in cm.

import constants


def main():
    # Input - radius.
    # defining the variable "radius"
    radius = int(input("What is the radius of the circle in centimeters? "))

    # process - Calculating circumference
    circumference = radius * constants.TAU

    # output - displays the circumference
    print("")
    print(
        "The circumference of the circle the circle is {:.2f}cm".format(circumference)
    )


if __name__ == "__main__":
    main()
