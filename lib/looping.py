#!/usr/bin/env python3

def happy_new_year():
    i = 11
    while i > 0:
        i -= 1
        if i == 0:
            print("Happy New Year!")
        else:
            print(i)


def square_integers(int_list):
    sqaure_integers = [int * int for int in int_list]
    return sqaure_integers

def fizzbuzz():
   for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
           print("FizzBuzz")
        elif i % 5 == 0:
           print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        i+=1

