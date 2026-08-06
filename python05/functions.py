def greet():
    print("hello, world!")

greet() 
greet()

def message():
    print("i am arthur")
    print("king of the britons")

print("i have a message for you.")
message()
print("good bye!")

def main():
   message()
print("good bye!")

def message():
    print("i am anirach")
    print("I love python")
main()

def green(name):
    print(f"hello, {name}!")

green("face") 

def add(a,b):
    return a + b

result = add(3,5)
print(result)


def find_max(*args):  #flowchart****ออกสอบแน่นอนลองเขียนดู
    if not args:
        return None
    max_value = args[0]
    for number in args:
        if number > max_value:
            max_value = number
    return max_value

result = find_max(3,5,7,2,8)
print(f"the maximum value is {result}")

def print_all (*args):
    for index, arg in enumerate(args):
        print(f"argument {index+1}: {arg}")

print_all ("python",3.8,True,[1,2,3],{"key": "value"})


def display_info (**kwargs):#**=มีค่า2ตัวมาเป็นคู่กัน
    for key,value in kwargs.items():
        print(f"{key}: {value}")
display_info (name="face" ,age=18,city="bangkok")



def calculate_stats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)#lenใช้บ่อยมากกๆๆๆๆควรฝึกบ่อยๆ
    maximum = max(numbers)
    minimum = min (numbers)
    return total_sum , average , maximum ,minimum

numbers = [5,10,15,20,25]
total , avg, max_num, mini_num = calculate_stats(numbers)

print(f"Total Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_num}")
print(f"Minimum: {mini_num}")


#def is_armstrong(numbers):#ไปฝึกทำแบบที่มีโฟลชารจให้กับแบบที่ไม่มีให้ในข้อสอบไม่มีให้ฝึกทำเยอะๆ
#    for number in numbers:
#        total = total(numbers)
#        if total == 
#ฝึกหน่อยอย่าขี้เกียดดดนะะะ ห้ามๆๆๆๆๆ gfuJp;d^0tc:',yo.shf^ 


def my_function():
    local_variable = "I'm inside the function"
    print (local_variable)

my_function()


global_variable = "I'm outside the function"

def my_function():
    print(global_variable)

my_function()

print(global_variable)


import random

HEAD = 1#ใหญ่หมดคือค่าคงที่ ค่าที่ไม่เปลี่ยนแปลง
TAILS = 2
TOSSES = 10

def tosses_coin():
    for toss in range(TOSSES):
        if random.randint(HEAD, TAILS) == HEAD:
            print("Heads")
        else:
            print("Tails")
tosses_coin()


counter = 0
def increment():
    global counter
    counter +=1

increment()
increment()

print(counter)



def add(a,b):
    return a+b


def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a/b
#import math_operations.add (10,5)

#result_add = math_operations.add(10,5)
#result_subtract = math_operations.subtract(10,5)
#result_multiply = math_operations.multiply(10,5)
#result_divide = math_operations.divide(10,5)




def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


def fibonacci(n):
    if n == 0:
            return 0
    elif n ==1:
            return 1
    else:
             return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))


def factorial_iter(n):
    result = 1
    for i in range(2,n+1):
        result *= i
        return result


prime=str(generate_prime(10))#ทำไงให้หาเลขที่เป็นจำนวนเฉพาะได้
if prime  :
    print(f"{prime} is a prime number"):
else:
    print(f"{prime} is not a prime number")