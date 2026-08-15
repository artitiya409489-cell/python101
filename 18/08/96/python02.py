name = ("arthitiya")
age = (18)
height = (152.5)


num1 = (int(input("Enter number")))
num2 = (int(input("Enter number")))

print("ผลบวกคือ",num1 + num2)
print("ผลลบคือ",num1 - num2)
print("ผลคูณคือ",num1 * num2)
print("ผลหารคือ",num1 / num2)
print("ผลส่วนคือ",num1 // num2)
print("ผลเศษคือ",num1 % num2)

numbers = (int(input("enter number")))
if numbers % 2 ==0:
    print("นี่คือตัวเลขคู่")
else:
    print("นี่คือเลขคี่")

#โจทย์รวมบท1+2
หน่วยกิต= int(input())
ค่าหน่วยกิต= float(input())
print("ค่าเทอมรวมคือ","%.2f" % (หน่วยกิต * ค่าหน่วยกิต))

number = int(input("พิมพ์ตัวเลข1ตัว"))
if number % 2 == 0 and number % 3 ==0:
   print("หารลงตัวทั้งคู่")
elif number % 2 ==0:
   print("เลขคู่")
else:
    print("เลขคี่")

อุณหภูมิองศาเซลเซียล =float(input("ํ พิมพ์อุณหภูมิ " " ํC"))
อุณหภูมิองศษฟาเรนไฮต์ =float((อุณหภูมิองศาเซลเซียล * 9/5) + 32)
print  ("อุณหภูมิองศาฟาเรนไฮต์: "  "%.2f" %(อุณหภูมิองศษฟาเรนไฮต์))
print(type(อุณหภูมิองศาเซลเซียล))

น้ำหนัก = float(input("พิมพ์น้ำหนักของคุณ กิโลกรัม"))
ส่วนสูง = float(input("พิมพ์ส่วนสูงของคุณ เมตร"))
BMI = (น้ำหนัก/(ส่วนสูง**2))
print(f"ค่าBMIของคุณคือ:","%.2f" %(BMI))
if BMI < 18.5:
   print("น้ำหนักน้อย")
elif BMI >= 18.5 and BMI <22.9:
   print("น้ำหนักสมส่วน")
else:
   print("น้ำหนักเกิน")



