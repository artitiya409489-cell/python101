with open("example.txt", "w") as file:
    file.write("hello,world! \n")
    file.write("this is a new line. \n")

with open ("example.txt","a") as file:
    file.write("this line is appended. \n")

with open ("example.txt","r") as file:
    contents = file.read()
    print(contents)#อย่าลืมเว้นวรรค คนชอบลืมกัน

with open("example.txt","r") as file:
    line = file.readline()
    while line:
        print(line.strip())#.
        line = file.readline()

with open("example.txt","r") as file:
    lines = file.readlines(
    )
    for line in lines:
        print(line.strip())


num_days = int(input("for how many days do u have sales?"))
with open("sales.txt","w") as sales_file:
    for count in range(1,num_days +1):
        sales = float(input(f"enter sales for day #{count}: "))
        sales_file.write(str(sales) + '\n')
print("data written to sales.txt")


with open("sales.txt","r") as sales_file:
    for line in sales_file:
        amount = float(line)
    print(format(amount, ".2f"))


num_emps = int(input("how many employee do u have"))
with open ("employees.txt","w") as emp_file:
    for count in range(1 , num_emps +1):
        print("enter data for employee #", count,sep="")
        name = input("name: ")
        id_num = input("id number:")
        dept = input("department:")
        emp_file.write("Name:" +name + "\n")
        emp_file.write("ID Number:" +id_num + "\n")
        emp_file.write("Department:" +dept + "\n\n")
        print()
print("employee records written to employees.txt")


import struct
record = (1, "john", 20,3.75)
with open("records.bin","wb") as file:
    data = struct.pack("i20sif", record[0], record[1].encode(), record[2], record[3])
    file.write(data)


# import struct
# with open("records.bin","rb") as file:
#     data = file.read(struct.calcsize("i20sif"))
#     record = struct.Struct("i20sif , data)")
#     record = (record.unpack("i20sif , data"))

# import struct
# record_format = "i20sif"

# def example_w_plus_mode():


def example_a_plus_mode():
    with open("example_a+.txt", "w+") as file:
        file.write("Hello, World!\n")
        file.write("This is a new line.\n")
        file.seek(0)  # Move the file pointer to the beginning
        contents = file.read()
        print(contents)