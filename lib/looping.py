#!/usr/bin/env python3

# def happy_new_year():
#     i = 10
#     while i > 0:
#         print(i)
#         i -= 1
# happy_new_year()
# print("hello world")



# def square_integers(int_list):
#     squared = []
#     for i in int_list:
#         squared.append(i ** 2)
#     return squared

# inputs = input("Enter the values : ")
# input_list = [int(x) for x in inputs.split(",")]
# result = square_integers(input_list)
# print(result)



def fizzbuzz():
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
fizzbuzz()
