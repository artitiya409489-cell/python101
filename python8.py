# x=1/0

# try:
#     x=10/0
#     print(f"value of x:{x}")
# except ZeroDivisionError as e:
#     print(f"error:{e}")

# print("end of program.")


# filename = input("enter a filename")
# tey:
#     infile = open(filename,"r")
#     contents = infile.read()
#     print(contents)
#     infile.close()
# except IOeror:
#       print("an error occurred t



# try:
#     value = int(input("enter a number: "))
#     result = 10 / value
# except ValueError:
#     print("invalid input! plese enter a number.")
# except ZeroDivisionError:
#     print("cannot divice by zero!")
# print("end of program")


# try:
#     value = int(input("enter a number:"))
#     result = 10 / value
#     print(f"esult of division:{result}")
# except Exception as e:
#    print(f"an error occurred: {e}")
# print("end of program")


# try:
#     value = int(input("enter a number: "))
#     result = 10 / value
# except ZeroDivisionError:
#     print("cannot divice by zero!")
# else:
#     print(f"the result is {result}")
# print("end of program")


# def divide (a,b):
#     return a/b
# a,b = map(int,input().split())
# print(divide(a,b))
# print("end of program")

# def divide(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError as e:
#         print("exception:",e)
#     else:
#         return result

# a,b =map(int,input().split())


# try:
#     a = int(input("enter a number"))
#     b = int(input("enter another number"))
#     result = a/b
#     print(f"the re sult of {a} diveided by {b} is:{result}")
# except ValueError:
#     print("invalid input. pleae enter vaild integer.")
# except ZeroDivisionError:
#     print("division by zero is not allowed. please enter a non-zero")
# finally:
#     print("complet")
# print("end of program")



# try:
# alue=int(input("enter a number"))
# result = 10/ValueError
# except ValueError:
#      print("invalid inout please enter a number.")
# except ZeroDivisionError:
#       print("cannot divide by zero!)

class NegativeNumberError(Exception):
    def __init__(self, value):
       self.value = value
       super(). __init__(f"invalid input:{value} is a negative number")

def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError(num)
    else:
        print(f"{num} is a valid positive number")

try:
    number = int(input("enter a number"))