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
        