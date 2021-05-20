#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: May 2021
# This program using a loop and an if statement


def main():
    # this program using a loop and an if statement
    for counter in range(1000, 2000 + 1):
        if counter % 5 != 4:
            print(counter, " ", end = "")
        else:
            print(counter)


if __name__ == "__main__":
    main()
