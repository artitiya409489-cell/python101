def group_by_signature(words: list) -> list:
    groups = {}

    for word in words:
        if word == "":
            continue

        signature = "".join(sorted(word))
        groups.setdefault(signature, []).append(word)

    return list(groups.values())