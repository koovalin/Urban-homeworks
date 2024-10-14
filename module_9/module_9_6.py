def all_variants(text):
    length = len(text)
    for end in range(length):
        for start in range(length-end):
            yield text[start:start+end+1]


# Пример использования функции-генератора
a = all_variants("abc")
for i in a:
    print(i)