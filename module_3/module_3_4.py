# Версия 1
def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if word.lower() in root_word.lower() or root_word.lower() in word.lower():
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)


# Вариант с использованием list comprehension:
def single_root_words_v2(root_word, *other_words):
    return [word for word in other_words if word.lower() in root_word.lower() or root_word.lower() in word.lower()]


result1 = single_root_words_v2('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words_v2('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
