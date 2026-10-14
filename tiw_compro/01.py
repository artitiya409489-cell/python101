# def word_frequency(Hello_world_hello_everyone):
#     wordlist = Hello_world_hello_everyone.lower().split()
#     frequency = {}
#     for word in wordlist:
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
#     return frequency
# print(word_frequency("Hello world hello everyone")) abc_bca_cab_bac_xyz_yxz_zxy_dog


# def group_by_signature(words: list) -> list:
#     wordlist = [word.lower() for word in words]
#     # สร้างไดเร้กทอรี่เพื่อเก็บเป้นตัวเล้กและก็ตัวอักษรเหมือนกันแค่กลับกัน
#     list_of_groups = {}
#     # ทำลิส
#     for word in wordlist:
#         # สำหรับคำในกลุ่มคำ
#         signature = "".join(sorted(word))
#         if signature in list_of_groups:
#             list_of_groups[signature].append(word)
#             # ถ้าเหมือนกันแต่ละตัวอักษรจะถูกจัดกลุ่มเข้าด้วยกันแค่เรียงไม่เหมือนกันได่
#         else:
#             list_of_groups[signature] = [word]
#             # ถ้าไม่จะสร้างคำใหม่
#     return list(list_of_groups.values())
# print(group_by_signature(["ct","tc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]))


           
def find_duplicate_chars_count(s: str) -> dict:
    s_list = s.lower().split()
    list_of_duplicates = {}
    for word in s_list:
       if word in list_of_duplicates:
           list_of_duplicates[word] += 1
    return list_of_duplicates
print(find_duplicate_chars_count("missssu"))