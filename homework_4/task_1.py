text = input('Введіть текст у форматі snake_case: ')

capitalized_words = text.title()

words_list = capitalized_words.split('_')
camel_case = ''.join(words_list)

print(camel_case)
