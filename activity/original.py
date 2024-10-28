def count_dict_generator(array:list, table: dict):
    for item in array:
        table[item] = table.get(item, 0) + 1

def uncommon_from_sentences(s1, s2):
    l1 = s1.split(" ")
    l2 = s2.split(" ")
    result = []

    word_table = {}
    count_dict_generator(l1, word_table)
    count_dict_generator(l2, word_table)

    for word, count in word_table.items():
        if count == 1:
            result.append(word)

    return result
