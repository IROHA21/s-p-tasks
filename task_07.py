def combine_anagrams(moon) :
    result = []
    used = set()

    for i in range(len(moon)):
        if moon[i] in used:
            continue

        current_group = [moon[i]]
        used.add(moon[i])

        for j in range(i + 1, len(moon)):
            if moon[j] in used:
                continue

            all_chars_match = True
            if len(moon[i]) != len(moon[j]):
                all_chars_match = False
            else:
                for elem in moon[i]:
                    if moon[j].find(elem) == -1:
                        all_chars_match = False
                        break

            if all_chars_match:
                current_group.append(moon[j])
                used.add(moon[j])

        result.append(current_group)

    print(result)



combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
"creams", "scream"])