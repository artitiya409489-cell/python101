# fruits= {"apple","banana","cherry"}

# fruits.add("orange")
# print(fruits)

# fruits.remove("banana")
# print(fruits)


# # setttttt
# set1 ={1,2,3}
# set2 = {3,4,5}

# print(set1.union(set2))
# # รวมกัน

# print(set1.intersection(set2))
# # หารายการที่เหมือนกัน

# print(set1.difference(set2))
# # หาสมาชิกที่อยู่ใน set1 แต่ไม่อยู่ใน set2

# print(set1.symmetric_difference(set2))
# # หาสมาชิกที่อยู่ใน set1 หรือ set2 แต่ไม่อยู่ในทั้งสอง set


# set1 ={1,2,3,4}
# set2 = {3,4,5,6}

# union_set = set1 | set2
# print("Union set:", union_set)

# intersection_set = set1 & set2
# print("Intersection set:", intersection_set)

# difference_set = set1 - set2
# print("Difference set:", difference_set)

# symmetric_difference_set = set1 ^ set2
# print("Symmetric Difference set:", symmetric_difference_set)


# setA = {1,2,3,4}
# setB = set([8,9,10])

# setA.add(5)
# setB.update([6,7])
# union_set = setA | setB
# print("Union set:", union_set)
# print("Length of union set:", len(union_set))

# setB.update("ABCD")
# setA.update([6,7,8])
# print(setA.intersection(setB))
# print(setA )


# เครื่องหมายการดำเนินการแบบอัปเดต (Update Operators) ใน Python ใช้สำหรับปรับปรุงชุดข้อมูล (set) โดยตรงโดยไม่สร้างชุดข้อมูลใหม่ การดำเนินการเหล่านี้จะเปลี่ยนแปลงชุดข้อมูลต้นฉบับแทนที่จะสร้างชุดข้อมูลใหม่
# set1 =  {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7}

# set1 &= set2
# print("After &= operator:", set1)

# set1 = {1, 2, 3, 4, 5}
# set1 -= set2
# print("After -= operator:", set1)
# set1 = {1, 2, 3, 4, 5}
# set1 ^= set2
# print("After ^= operator:", set1)



# set_a = {1, 2, 3, 4}
# set_b = {2,3}
# set_c = {1,2,3,4}
# set_d ={1, 2, 3, 4, 5}

# print("set a is superset of set b:", set_a >= set_b)
# print("set b is subset of set a:", set_b <= set_a)

# print("is set_a a proper subset of set_b:", set_a < set_b)
# print("is set_b a proper subset of set_a:", set_b < set_a)

# print("are set_a and set_c equal:", set_a == set_c)

# print("is set_b a subset of set_d: and not equal", set_b <= set_d and set_b != set_d)


# ออกสอบไฟนอลครัฟฟ
# def remove_duplicates(input_list):
#     return list(set(input_list))

# numbers = [1, 2, 3,1,2,4,5,6,5,4,3]
# print(remove_duplicates(numbers))


# exammmmmmmmmm!!!!!!!!!!!
attendance_week = [
    ["alice", "Bob", "Charlie", "David"],
    ["alice", "David", "Charlie"],
    ["alice", "Bob","David"],
    ["alice","David","eve"],
    ["Bob", "Charlie", "David"]
]

attendance_sets = [set(day) for day in attendance_week]
print(attendance_sets)

present_every_day = set.intersection(*attendance_sets)
print("present every day:", present_every_day)

all_students = set.union(*attendance_sets)
absent_students = all_students - present_every_day
print("absent students:", absent_students)

first_day_students = attendance_sets[0]
last_day_students = attendance_sets[-1]
first_day_not_last_day = first_day_students - last_day_students
print("first day not last day:", first_day_not_last_day)

unique_students = len(all_students)
print("total unique students:", unique_students)


survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Java", "C++", "Python", "JavaScript"]
]

survey_sets = [set(day) for day in survey_results]
print(survey_sets)
# Find the most popular programming language
popular_language = set.intersection(*survey_sets)
print("popular language:", popular_language)

all_languages = set.union(*survey_sets)
one_only_languages = [lang for lang in all_languages if sum(lang in day for day in survey_sets) == 1]
print("languages mentioned by only one respondent:", one_only_languages)