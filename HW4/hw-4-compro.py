def group_by_signature(words: list) -> list:
    groups = {}
    for word in words:
        signature = "".join(sorted(word))
        groups.setdefault(signature, []).append(word)
    return list(groups.values())

if __name__ == "_main_":
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [['abc', 'bca', 'cab', 'bac'], ['xyz', 'yxz', 'zxy'], ['dog']]

    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [['apple', 'papel'], ['pale', 'leap', 'plea'], ['hello']]