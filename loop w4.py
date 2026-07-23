#print("i will display the numbers 1 tgrough 50" )
#for num in[1,2,3,4,5]:
 #   print("the a number is",num+2)

#ในกล่องใส่อะไรก้ได้มันจะแสดงผลทีละตัว 

#มันจะได้ชาตามอักษรมีกี่ตัว 
for char in "hello":
    print("char")

#ตรงนี้งงอย่าลืมกลับมาทำความเข้าใจ
input_string = input("enter a string: ")  
modified_string = ""
vowels = "aeiouAEIOU" #ใหย่และเล้กถึงจะครอบคลุม
for char in input_string:
    upper_char = char.upper()
    if upper_char in vowels:
       modified_string = "*"
    else:
     modified_string = upper_char
print("modified sting:",modified_string)
#*****

for i in range(5): #ที่ได้จะเริื่มจาก0** ใส่ตัวเดียวคือหยุดดสต้อป มันจะไม่นับตัวมันเอง**
   print(i)

for i in range(3,10):#start stop
    print(i)

for i in range(1,11,2):
    print(i)

#ปริ้นได้ตารางงน่าจะออกสอบอย่าลืมฝึก
#print the tabl headings.
print("number\tsquare")
print("_______________")

#print thee numbers 1 through 10
#and their squares
for number in range(1,11):
   square = number**2
   print(number, "\t" , square)

print("KPH\tMPH")
print("_______________")
  
for KPH in range(60,131,10):  #***stopมันจะไม่เอาค่าตัวเองต้อง+1เสมอ***
   MPH = KPH*0.6214
   print(KPH, "\t" , MPH ) #.2f
#ออกสอบบบบบบ*********************

count = 0
while count < 5:
   print("hello : ",count)
   count += 1 #ห้ามลืมไม่งั้นจะิอนฟินิตี้


#while 
keep_going = "y Y"
while keep_going == "y":#.upper = pP oO hH fF
   sales = float(input("enter the amount of sales: "))
   comm_rate = float(input("enter the commission rate :"))
   commission = sales * comm_rate
   print(f"the commission is ${commission:.2f}")
   keep_going = input("do you want to calculate anothre" +\
                        "commission (enter y for yes): ")
   

#wrong

rows=int(input("hoe many rows?"))
columns=int(input("hoe many columns?"))
for i in range(rows):
   for j in range(columns):
      print("*", end=" ")
      print()


score = int(input("enter a test score" ))
while score < 0 or score > 100:
   print("ERROR: the score cannot ne negative")
   print("or greater than 100.")
   score = int(input("enter the correct score: " ))

for letter in "anirach mingkwan":
   if letter == "a" or letter =="k":
      continue
   print ("current letter :",letter)

for letter in "anirach mingkwan":
   if letter == "a" or letter =="k":
      break
   print ("current letter :",letter)

for letter in "anirach mingkwan":
   if letter == "a" or letter =="k":
      pass
   print ("current letter :",letter)

   numbers = [6,5,4,3,8,4,2,5,4,11]
   sum = 0
   for val in numbers:
      sum += val
      print(sum)

print("the sum is",sum)#ปรับให้รวมแค่เลขคู่หรือเลขคี่ใช้อีฟ

max = 5
toyal = 0.0
print("this program calculates the sum of")
print(max, "numbers you will enter.")
for counter in range(max):
   number = int(input("enter a number: "))
   total = total + number
print("the total is",total)


#nested loop
for i in range(1,3):
   for j in range(2,5):
      print(i,j)
#ระวังข้อนี้ออกสอบช่อกาว่าปริ้นมาได้อะไร
for i in range(4):
   for j in range(i):
      print(i,j)


for hours in range(24):
   for minutes in range(60):
      for seconds in range(60):
         print(hours, ":", minutes, ":",seconds)
         