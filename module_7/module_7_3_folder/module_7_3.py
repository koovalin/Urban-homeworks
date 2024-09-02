import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    # Удаление пунктуации
                    text = text.translate(str.maketrans('', '', string.punctuation.replace(' - ', '')))
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word.lower() in words:
                result[name] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                result[name] = count
        return result


finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

finder3 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))

finder4 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder4.get_all_words())
print(finder4.find('captain'))
print(finder4.count('captain'))
