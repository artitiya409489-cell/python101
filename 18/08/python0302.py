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
# for i in range(1,11):
#     for j in range(i):
#         print("*", end= "")
#     print()
# numbers = int(input("enter number"))
# is_prime = True 
# for i in range(2,numbers):
#       if numbers % i == 0:
#        is_prime = False
#       break
# if is_prime:
#     print(numbers,"เป็นเลขเฉพาะ")
# else:
#     print(numbers,"ไม่ใช่เลขจำเพาะ")
# numbers = int(input("enter number"))
# is_prime = True
# for i in range(2,numbers):
#     if  numbers % i== 0:
#         is_prime = False
#         break
# if is_prime:
#         print(numbers,"this is prime number")
# else:
#         print(numbers,"this is not prime number")
# for i in range(1,101):
#     print(i)

# for i in range(1,101):
#     if i % 2 ==0:
#         print(i)

# for i in range(1,101):
#     if i % 2 !=0:
#         print(i)

# # #sum while
# i = 1
# total = 0
# while i <= 100:
#     total += i
#     i += 1
# print("ผลรวมคือ",total)

# #sum for
# total = 0
# for i in range(1,101):
#     total += i
# print("ผลรวมคือ",total)

# for i in range(1,101):
#     if i % 3 ==0:
#         print("หารเลข3ลงตัว",i)

# numbers = int(input("enter number"))
# is_prime = True
# for i in range(2, numbers):
#     if numbers % i ==0:
#         is_prime = False
#         break
# if is_prime:
#     print(numbers,"คือเลขเฉพาะ")
# else:
#     print(numbers,"คือเลขไม่เฉพาะ")
# total = 0
# numbers = int(input("enter nuber"))
# for i in range(1,numbers+1):
#     if i % 2 ==0:
#         total += i
# print("sum",total)

# total = 0
# n = int(input("enter"))
# for i in range(1,n+1):
#     if i % 2 == 0:
#         total += i
# print("sum",total)

# password = int(input("enter your password"))
# while password != 1234:
#     password = int(input("enter your password cc"))
# print("wellcome")

# total = 0
# i =1 
# while i <= 100:
#     total += i
#     i += 1
# print("bb", total)

# total = 0
# num=int(input("en"))
# for i in range(1,num+1):
#     if i % 2 == 0:
#         total += i
# print("mm",total)

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
