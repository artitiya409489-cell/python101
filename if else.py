score1 = int(input("enter your score for test 1:"))
score2 = int(input("enter your score for test 2:"))
score3 = int(input("enter your score for test 3:"))
average = (score1 + score2 + score3) / 3
print("the average is:", "{:.1f}".format(average))

num_employees = int(input("enter the number of employees:"))
if num_employees < 50:
    print("this is a small company.")
elif num_employees < 250:
    print("this is a medium-sized company.") 
elif num_employees >= 250:
    print("this is a large company.")

score = int(input("enter your score:"))
if score >= 90:
    print("grade:a")
elif score >= 80:
    print("grade:b")
elif score >= 70:
    print("grade:c")
else:
    print("grade:f:")


inchar = input("input one chacter:")
if inchar >= "A" and inchar <="Z":
    print("you in put upper case letteer ", inchar)
elif inchar >= "a" and inchar <="z":
    print("you in put lower case letteer ", inchar)
elif inchar >= "0" and inchar <="9":
    print("you in put a number ", inchar)
else:
    print("it's not a letter or number.")


num = float(input("enter a number:"))
if num > 0:
    print("positive number")
elif num == 0:
    print("zero")
else:
    print("negative number")


num = float(input("enter a number:"))
if num>= 0:
   if num == 0:
    print("zero")
   else:
    print("positive number")
else:
    print("negative number")


x=10
y=20

print(x == y) #false
print(x != y) #true
print(x > y) #false
print(x < y) #true
print(x >= y) #false
print(x <= y) #true