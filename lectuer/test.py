print("I'm hungry!")
print("She asks me, 'Are you hungry?'")
print("I'm good and\"I will do my best\"")
print("/\\")
print("\ta\na\ta\ta\n\ta")
print("""\ta
      a\ta\ta
      \ta""")

print("100.00")
print("%d" % 100)
print("%f" %100.58)
print("%f" %100.89)
print("%.3f" %100.89)

from math import pi
from unittest import result
print("%F" %pi)
print("%.4F" %pi)
print("%.50F" %pi)
print("%.100F" %pi)
print("%.1000F" %pi)


print("my age is",18,"i have",120.50,"bath.")
print("my age is %d i have %.2f bath." %(18,120.50))
print("my age is " + str(18) + " i have " +str(120.50) + " bath.")
print("my age is {0} i have {1:.2f} bath.".format(18, 120.50))

print("5+4 =",5+4)
print("5+4 = %.2f" %(5+4))
print("5+4 = "+str(5+4))
print("5+4 = " +str(5+4))
print("5+4 = {0:.2f}".format(5+4))


print("I'm anirach","I'll keep practicing!")
print("I'm anirach "+ "I'll keep practicing!")

print(1,1,2,3,5,8,13,21,34,55)
print("%d %d %d %d %d %d %d %d %d %d " %(1,1,2,3,5,8,13,21,34,55))


#converting int to float
age = 25
height = float(age)
print(height)

#float to int
height = 5.6
age = int(height)
print(age)

#string to int
num_str = "123"
num = int(num_str)
print(num)

x= 17
y = 4
print("x+y =",x+y) #21
print("x-y =",x-y) #13
print("x*y =",x*y) #68
print("x/y =",x/y) #4.25
print("x%y =",x%y) #1
print("x//y =",x//y) #4
print("x**y =",x**y) #83521

first_name = input('enter your first name:')
last_name = input("enter your last name:")
print('hello' , first_name, last_name)

number = input('enter ur number:')
result = int(number) + 10
print( result)

name = input('what is ur name? ')
age = int(input('how old are you? '))
income = float(input('what is ur income? '))

print('here is the data you entered:')
print('name:', name)
print('age:', age)
print('income:', format(income, "12,.2f"))


weight = float(input('enter ur weight in kg:'))
height = float(input('enter ur height in meter:'))#cm/100
bmi = weight /(height * height)
print("your bmi is:", format(bmi, ".2f")) #.2f=เอาทศนิยม2ตัว


อุณหภูมิ = float(input('enter ur temperature in celsius:'))
ฟาเรนไฮ = (อุณหภูมิ *9/5) +32
print('temperature in fahrenheit is:', format(ฟาเรนไฮ, ".2f"),"ํF")
