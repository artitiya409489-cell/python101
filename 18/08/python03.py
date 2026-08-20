# เงื่อนไขและการเปรียบเทียบ
# score = float(input("enter your score"))
# print("คะแนนของคุณคือ","%.2f" %(score))
# if score >= 80:
#     print("gradA")
# elif score >= 70 and score <= 79:
#     print("gradB")
# elif score >= 60 and score <= 69:
#     print("gradC")
# elif score >= 50 and score <= 59:
#     print("gradD")
# else:
#     print("gradF")
# age = int(input("enter your age"))
# print("อายุของคุณคือ", age)
# if age >=18 and age <60:
#     print("อยู่ในวัยทำงาน")
# elif age < 18:
#     print("ยังไม่บรรลุนิติภาวะ")
# else:
#     print("อยู่ในวัยเกษียณ")
# สัญชาติ = input("กรอกสัญชาติของคุณ")
# ปีเกิด = int(input("กรอกปีเกิดของคุณ (พศ.)"))
# อายุ = (2569 - ปีเกิด )
# if สัญชาติ == "ไทย" and อายุ >=18:
#     print("คุณมีสิทธิ์เลือกตั้ง")
# else:
# #     print("คุณไม่มีสิทธ์เลือกตั้ง")
# number1 = int(input("กรุณากรอกเลขตัวที่1"))
# number2 = int(input("กรุณากรอกเลขตัวที่2"))
# number3 = int(input("กรุณากรอกเลขตัวที่3"))
# # print ("ค่าตัวเลขแต่ละตัวคือ",number1,number2,number3,"ตามลำดับ")
# if number1 > number2 and number1 > number3:
#     print("เลขตัวที่1 คือตัวเลขค่าที่มากที่สุด")
# elif number2 > number1 and number2 > number3:
#     print("เลขตัวที่2 คือตัวเลขค่าที่มากที่สุด")
# else:
#     print(f"เลขตัวที่3 {number3} คือตัวเลขค่าที่มากที่สุด")
# print ("ค่าตัวเลขแต่ละตัวคือ",number1,number2,number3,"ตามลำดับ")


# from math import pi
# print("%.3f" %(pi))
# print("-" * 30)
# for i in range(1,11):
#     for j in range(i):
#         print("*", end= "")
#     print()
# def new_func():
#     for i in range(1,101):
#         if i % 3 ==0:
#             print("หารเลข3ลงตัว",i)

# # new_func()
# total = 0
# numbers = int(input("enter nuber"))
# for i in range(1,numbers+1):
#     if i % 2 ==0:
#         total += i
# print("sum",numbers,total)
# print("กรอกข้อมูลหาค่าBMI")
# numbers = int(input("พนักงานมีทั้งหมดกี่คน"))
# คนที่น้ำหนักเกิน = 0
# for i in range(numbers):
#     น้ำหนัก =float(input(f"กรอกน้ำหนักของคนที่ {i+1} (กิโลกรัม.)"))
#     ส่วนสูง = float(input(f"กรอกส่วนสูงของคนที่ {i+1}  (เมตร.)"))
#     BMI = (น้ำหนัก / (ส่วนสูง**2))

#     if BMI <= 18.5:
#         result ="น้ำหนักน้อย"
#     elif BMI <= 22.9:
#          result ="น้ำหนักปกติ"
#     else:
#         result ="น้ำหนักเกิน"
#         คนที่น้ําหนักเกิน += 1
#     print(f"คนที่ {i+1} BMI ={BMI:.2f} {result} ")
# print("คนที่น้ำหนักเกิน",คนที่น้ําหนักเกิน)
def หาตัวที่คูณแล้วได้ค่าที่ต้องการ(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if (numbers[i] * numbers[j]) == target:
                return [numbers[i], numbers[j]]
    return []
print(หาตัวที่คูณแล้วได้ค่าที่ต้องการ([2,4,5,7],20))