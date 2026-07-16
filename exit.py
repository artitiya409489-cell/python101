fruits = ["apple", "banana", "cherry"]

print("banana" in fruits) 
print("orang" in fruits) 

print("grape" not in fruits) 
print("apple" not in fruits) 

sentence = "the quick"
print("fox" in the sentence) 
print("cat" not in the sentence)


age = int(input("enter ur age"))
income = int(input("enter ur income"))

if age >= 18 and age <= 65 and income > 30000:
    print("you are eligible for the loan.")
else:
    print("you are nott eligible for the loan.")
    