prime_numbers = [2,3,5,7,11,13,17,19,23,29]
print (f"Prime numbers : {prime_numbers}")
fifth_prime = prime_numbers[4]
print (f"Prime numbers : {fifth_prime}")


colors = ["red","blue","green","yellow","purple"]
second_to_last_color = colors[-2]
print(f"second to last color : {second_to_last_color}")
last_color = colors[len(colors)-1] #len=ไว้หาสมาชิก
print(f" last color : {last_color}")


shapes = ["circle","square","triangle","rectangle","hexagon"]
shapes[1]= "ellipse"
shapes[3]= "pentagon"
print(f"Modified shapes : {shapes}")


fruits = ["apple" ,"banana","cherry"]#ต่อท้ายยกัน
more_fruitts = ["mango","pineapple"]
for fruit in more_fruitts:
    fruits.append(fruit)
print(f"Fruits after append: {fruits}")


berries = ["raspberry","blackberry"]#จะลงไปแทนตำแหน่งไหนน 
berries.insert(1, "strawberry")
berries.insert(2, "blueberry")
print(f"berries after insert : {berries}")


fruits_with_duplicates = ["apple","banana","apple","cherry","apple","kiwi"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")#whileจะทำจนกว่าจะออกหมดถ้าไม่ลูปไวจะเอาออกแค่ตัวแรกตัวเดียว
print(f"fruits after remove: {fruits_with_duplicates}")


grades = [85,90,78,92,88]
third_grade = grades.pop(2)#ต้องมีค่ามารับเวลาเอาออก
#grades.append(third_grade)
print(f"grades after pop: {grades}")


animls =["cat","dog","rapbit","hamter","dog","parrot"]
first_dog_index = animls.index("dog") #เอาอันแรกมาทดอันที่2
print(f"the first occurrence of 'dog' is at index : {first_dog_index}")
#ดหลืออีก2บรรทัด


nested_list = [[1,2,3],[4,5,6],[7,8,9]]
for sublist in nested_list:
    sublist.clear()
print(f"nested list after clrar : {nested_list}")



# heroes = ['ironman','thor','hulk','superman','spiderman']
# h2 = ['dr.strange','cpt.america','black panther','ant man']

# heroes.insert(0,h2[0])
# print(heroes.index('thor'))
# heroes.insert(heroes.index('thor'),h2[1])
# print(heroes)
# heroes.remove('spiderman')
# heroes.append('ant man')
# print(heroes)
# heroes.sort()
# print(heroes)
# heroes.reverse()
# print(heroes)
# newheroes = heroes
# newheroes[0] = 'wanderwoman'
# print(heroes)
# copyheroes =[]+ heroes
# print(copyheroes)
# copyheroes[0]='hanaman'
# print(heroes)
# print(copyheroes)


data= list(range(100))
slited_data = data[10:51:5]
print(f"sliced data: {slited_data}")


numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers[2:6])
print(numbers[1:8:2])
print(numbers[:4])
print(numbers[6:])
print(numbers[-5:-1])
print(numbers[::-1])


ss="sammy shark!"
print(ss[4])
print(ss[6:11])
print(ss[:5])
print(ss[7:])
print(ss[-4:-11])
print(ss[6:11])
print(ss[6:11:1])
print(ss[0:12:2])
print(ss[0:12:4])
print(ss[::4])
print(ss[::-1])
print(ss[::-2])#ชื่อนศ.มา อยากให้ชื่อตัวแรกมาต่อ กับรหัสนส.4ตัวท้ายไรงี้


even_number=[2,4,6,8,10]
heroes= ['ironmam','thor','hulk','spiderman']
numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[-5:])
numbers[8] =99
print(numbers)

pluslist = heroes + even_number
print(pluslist)
print(len(numbers))


numbers = [4,2,9,1,5,6]
length = len(numbers)
print(f"lenght of the list : {length}")

total_sum = sum(numbers)
print(f"sum of the list : {total_sum}")

max_value = max(numbers)
print(f"maximum value : {max_value}")

min_value = min(numbers)
print(f"minimum value : {min_value}")

sorted_numbers = sorted(numbers)
print(f"sorted list : {sorted_numbers}")

# bool_list = [false,true,false]
# any_ture = any(bool_list)
# print(f"is element ture? : {any_ture}")

# all_true = min(numbers)#เหลืออีกก
# print(f"minimum value : {min_value}")


num_employees =6

def main():
    hours = [0] *num_employees

    for index in range(num_employees):
        print('enter the hours worked',\
              index + 1, ':',sep='',end='')
        hours[index] = float(input())

    pay_rate = float(input('enter pay rate'))

    for inde in range(num_employees):
        gross_pay = hours[index] * pay_rate
        print('gross',index +1 ,':$',\
        format(gross_pay,'.2f'),sep='')
main()

#การบ้านนน แอพเพน ถ้าเลือก6คือออก

matrix[0][1]=10
print(matrix)
for row in matrix:
    for element in row:
        print(element,end="")
    print()
import random
rows = 3
cols = 4

def main():
    values = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

    for r in range(rows):
        for c in ranre(cols):
            values[r][c] = random.randint(1,100)

        print(values)
main()


#tople
my_tuple = 1,2,3
print(my_tuple)

a,b,c = my_tuple
print(a)#1
print(b)#2
print(c)#3
#exercise 1อัพเดตว่าการซื้อขาย หาว่าอะไรแพงสุด อัพเดตข้อมูล สินค้าคงคลัง สินค้าขึ้นราคามั้ย เรียกใช้ฟังชันที่1บานาน่าหายไป20ล฿ก แอดอีก1ไอเทม ใช้คำสั่งที่เรียนไปแล้วว ทำได้ สาธุ99