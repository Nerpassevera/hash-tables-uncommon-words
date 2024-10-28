def count_dict_generator(array:list, table: dict):
    for item in array:
        table[item] = table.get(item, 0) + 1

def uncommon_from_sentences(sentences:list):

    result = []
    word_table = {}
    for sentence in sentences:
        count_dict_generator(sentence.split(), word_table)

    for word, count in word_table.items():
        if count == 1:
            result.append(word)

    return result
