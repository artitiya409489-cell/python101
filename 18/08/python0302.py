# i = 1
# total = 0
# while i <= 100:
#     total += i
#     i += 1
# print("ผลรวมคือ" , total)

# total = 0
# for i in range(1,101):
#     if i <= 100:
#         total += i
# print("ผลรวมคือ1-100:" , total)

# i = 1
# total = 0
# while i <= 100:
#     total += i
#     i +=1
# print("ผลรวม1-100คือ:",total)
    
# i = 1
# total = 0
# while i <= 500:
#     total += i
#     i += 1
# print("ค่ารวม1-500คือ:" , total)

# total = 0
# for i in range(1,501):
#     total += i
# print("ค่ารวม1-500คือ:" , total)

# numbers = input("enter number")
# while numbers != "stop":
#       numbers=input("enter number ")
# print("หยุดทำงานแล้ว")
    
# name =input("enter your name:")
# while name != "arthitiya":
#     name = input("enter your name:")
# print("เข้าสู่ระบบเรียบร้อยแล้วคุณอาทิติยา")
# for i in range(5,6):
#     for j in range(1,13):
#         print(f"{i}x{j} =  {i*j}")
# for i in range(10,11):
#     for j in range(1,13):
#         print(f"{i}x{j} = {i*j}")
# i = 1
# total = 0
# while i <= 100:
#     total += i
#     i += 1
# print("ผลรวมคือ:" , total)
for i in range(1,11):
    for j in range(i):
        print("*", end= "")
    print()
numbers = int(input("enter number"))
is_prime = True 
for i in range(2,numbers):
      if numbers % i == 0:
       is_prime = False
      break
if is_prime:
    print(numbers,"เป็นเลขเฉพาะ")
else:
    print(numbers,"ไม่ใช่เลขจำเพาะ")
numbers = int(input("enter number"))
is_prime = True
for i in range(2,numbers):
    if  numbers % i== 0:
        is_prime = False
        break
if is_prime:
        print(numbers,"this is prime number")
else:
        print(numbers,"this is not prime number")
for i in range(1,101):
    print(i)

for i in range(1,101):
    if i % 2 ==0:
        print(i)

for i in range(1,101):
    if i % 2 !=0:
        print(i)

# #sum while
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
print("ผลรวมคือ",total)

#sum for
total = 0
for i in range(1,101):
    total += i
print("ผลรวมคือ",total)

for i in range(1,101):
    if i % 3 ==0:
        print("หารเลข3ลงตัว",i)

numbers = int(input("enter number"))
is_prime = True
for i in range(2, numbers):
    if numbers % i ==0:
        is_prime = False
        break
if is_prime:
    print(numbers,"คือเลขเฉพาะ")
else:
    print(numbers,"คือเลขไม่เฉพาะ")
total = 0
numbers = int(input("enter nuber"))
for i in range(1,numbers+1):
    if i % 2 ==0:
        total += i
print("sum",total)

total = 0
n = int(input("enter"))
for i in range(1,n+1):
    if i % 2 == 0:
        total += i
print("sum",total)

password = int(input("enter your password"))
while password != 1234:
    password = int(input("enter your password cc"))
print("wellcome")

total = 0
i =1 
while i <= 100:
    total += i
    i += 1
print("bb", total)

total = 0
num=int(input("en"))
for i in range(1,num+1):
    if i % 2 == 0:
        total += i
print("mm",total)

num = int(input("enter"))
is_prime = True
for i in range(2,num):
    if num % 2 ==0:
        is_prime = False
        break
if is_prime:
    print("numprime",num)
else:
     print("not numprime",num)
scores = []
score = int(input("score:"))
while score != -1:
    scores.append(score)
    score = int(input("score"))
total = 0
for s in scores:
    total += s
ค่าเฉลี่ย = total / len(scores)

print("",ค่าเฉลี่ย)

if ค่าเฉลี่ย >=80:
    print("A")
elif ค่าเฉลี่ย >=70:
    print("B")
elif ค่าเฉลี่ย >=60:
    print("C")
elif ค่าเฉลี่ย >=50:
    print("D")
else:
    print("F")
moneys =[]
money = int(input("money"))
while money != -5:
    moneys.append(money)
    money=int(input("money"))
total = 0
for m in moneys:
    total += m
ค่าเงินเฉลี่ย = total / len(moneys)
print("ค่าเฉลี่ย",ค่าเงินเฉลี่ย)

bfs =[]
bf = input("do u want any bf/gf?")
while bf != "no":
    bfs.append(bf)
    bf = input("do u want any bf/gf?")
total = 0
for b in bfs:
    total +=b
sumbf =(total / len(bfs))
print("ค่าเฉลี่ยแฟนที่ทุกคนอยากมี",sumbf)

scores = []
score =int(input("enter score"))
while score != -1:
    scores.append(score)
    score =int(input("enter score"))
total = 0
for s in scores:
    total += s
ค่าเฉลี่ยคะแนน = (total / len(scores))
print("มีนักเรียนทั้งหมด",len(scores))
print("ค่าเฉลี่ยคะแนน",ค่าเฉลี่ยคะแนน)

numbers = int(input("enter score"))
is_prime = True
for i in range(2,numbers):
    if numbers % i ==0:
        is_prime = False
        break
if is_prime:
    print(numbers,"this is prime number")
else:
    print(numbers,"this is not prime number")
for i in range(1,101):
    if i % 3 == 0 and i % 5==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print("กรอกข้อมูลหาค่าBMI")
numbers = int(input("พนักงานมีทั้งหมดกี่คน"))
คนที่น้ำหนักเกิน = 0
for i in range(numbers):
    น้ำหนัก =float(input(f"กรอกน้ำหนักของคนที่ {i+1} (กิโลกรัม.)"))
    ส่วนสูง = float(input(f"กรอกส่วนสูงของคนที่ {i+1}  (เมตร.)"))
    BMI = (น้ำหนัก / (ส่วนสูง**2))

    if BMI <= 18.5:
        result ="น้ำหนักน้อย"
    elif BMI <= 22.9:
         result ="น้ำหนักปกติ"
    else:
        result ="น้ำหนักเกิน"
        คนที่น้ําหนักเกิน += 1
    print(f"คนที่ {i+1} BMI ={BMI:.2f} {result} ")
print("คนที่น้ำหนักเกิน",คนที่น้ําหนักเกิน)

numbers = int(input("จำนวนคนที่บริษัท"))
คนที่น้ำหนักเกิน  = 0
total = 0
for i in range(numbers):
     น้ำหนัก  = float(input(f"น้ำหนักคนที่ {i+1} (kg.)"))
     ส่วนสูง  = float(input(f"ส่วนสูงคนที่ {i+1} (m.)"))
     BMI = (น้ําหนัก / (ส่วนสูง**2))
     total += i
    
     if BMI <= 18.5:
          result ="น้ำหนักน้อย"
     elif BMI <= 22.9:
         result ="น้ำหนักสมส่วน"
     else:
         result = "น้ำหนักเกิน"
         คนที่น้ําหนักเกิน += 1
     ค่าเฉลี่ย = (total / คนที่น้ําหนักเกิน)
          print(f"คนที่น้ำหนักเกินมีทั้งหมด {คนที่น้ําหนักเกิน}" )
prin

numbers = int(input("จำนวนคนในห้อง"))
คนที่น้ำหนักเกิน = 0
for i in range(numbers):
    น้ำหนัก =float(input(f"กรุณากรอกน้ำหนักคนที่ {i+1} (kg.)"))
    ส่วนสูง =float(input(f"กรุณากรอกส่วนสูงคนที่ {i+1} (m.)"))
    BMI = (น้ําหนัก / (ส่วนสูง**2))

    if BMI <= 18.5:
        result ="น้ำหนักน้อย"
    elif BMI <= 22.9:
        result ="น้ำหนักน้อย"
    else:
        result="น้ำหนักเกิน"
        คนที่น้ําหนักเกิน += 1
    print(f"ค่าBMIของคนที่ {i+1} BMI = {BMI:.2f} {result} ")
print(f"คนที่น้ำหนักเกินมีทั้งหมด {คนที่น้ําหนักเกิน} คน")
numbers = []
for i in range(10):
    number = float(input(f"enter number {i+1}:"))
    numbers.append(number)

max_num =numbers[0]
min_num =numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number
print(f"ค่าที่มีมากที่สุดคือ {max_num:.2f}")
print(f"ค่าที่มีน้อยที่สุดคือ {min_num:.2f}")
x

numbers =[]
for i in range(5):
    number = float(input(f"enter number {i+1}"))
    numbers.append(number)

max_num = numbers[0]
min_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number
print(f"ค่าที่มากที่สุดคือ {max_num:.2f}")
print(f"ค่าที่น้อยที่สุดคือ {min_num:.2f}")

numbers = []
for i in range(3):
    number=float(input(f"enter number {i+1}"))
    numbers.append(number)

max_num =numbers[0]
min_num =numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number

print(f"ค่ามากที่สุดคือ {max_num:.2f}")
print(f"ค่าน้อยที่สุดคือ {min_num:.2f}")
numbers=[]
for i in range(5):
    number= float(input(f"enter number {i+1}"))
    numbers.append(number)

max_num = numbers[0]
min_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number
print(f"ค่าที่มากที่สุดคือ {max_num:.2f}")
print(f"ค่าที่มากที่สุดคือ {min_num:.2f}")
numbers = []
is_prime_num = True
number = int(input("enter number"))
for i in range(2,number):
    if number % i == 0 :
        numbers.append(number)
        is_prime_num = False

if is_prime_num:
    print(f"เลข {number}คือเลขเฉพาะ")
else:
    print(f"เลข {number}ไม่ใช่เลขเฉพาะ")

supjects =[]
scores =[]
for i in range(6):
    supject =input(f"enter supject {i+1}")
    score = float(input(f"enter score {i+1}"))
    supjects.append(supject)
    scores.append(score)

credit = 3
total_credit = 0
total_point = 0
for i in range(6):
    score = scores[i]
    if score >= 80:
        grade = "A"
        level = 4
    elif score >=70:
        grade = "B"
        level = 3
    elif score >=60:
         grade = "C"
         level = 2
    elif score >=50:
            grade = "D"
            level = 1
    else:
         grade = "F"
         level = 0
numbers = [2,4,5,7]
target = 14
def หาตัวที่คูณแล้วได้ค่าที่ต้องการ(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if (numbers[i] * numbers[j]) == target:
                return [numbers[i], numbers[j]]
    return []
print(หาตัวที่คูณแล้วได้ค่าที่ต้องการ([2,4,5,7],20))

start =int(input("enter start C:"))
end =int(input("enter end C:"))
step = int(input("enter step:"))
while step <= 0:
    print("! step must be 0.")



