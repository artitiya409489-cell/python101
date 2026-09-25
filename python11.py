# def apply_function(func,value):
#     return func(value)
# def square(x):
#     return x*x
# print(apply_function(square,5))



# def greet(name):
#     return f"hello,{name}!"
# say_hello = greet
# print(say_hello("alice"))



# lambda arguments: expression
# add = lambda x,y:x+y
# ,print(add(3,5))
# numbers = [1,2,3,4,5]
# squared_numbers = list(map(lambda x:x*x, numbers))
# print(squared_numbers)




# filter(function, iterable)
# numbers = [1,2,3,4,5]
# even_numberss = list(filter(lambda x:x%2 ==0,numbers))
# print(even_numberss)



# form functools import reduce
# reduce (function, iterabie)
# form functools import reduce




# from functools import reduce
# numbers = [1,2,3,4,5,6,8,9,10]
# squared_numbers = map(lambda x :x**2,numbers)
# even_squared_numbers = filter(lambda x:x%2 ==0,squared_numbers)
# sum_of_eveen_squared_numbers = reduce(lambda x,y:x+y,even_squared_numbers)
# print(sum_of_eveen_squared_numbers)



# def apply_twice(func,value):
#     return func(func(value))
# def increment(x):
#     return x+1
# print(apply_twice(increment,5))



def create_multiplier(n):
    return lambda x: x*n
double =create_multiplie
triple = create_multiplier(3)
print(double(5))
print(triple(3))
# **mai ook shobb***
