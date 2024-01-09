from random import sample


def pemrtuate(text):
    words = text.split()
    shuffled_words = []

    for word in words:
        first_char = word[0]
        last_char = word[-1]
        middle = word[1:-1]
        shuffled_text = []

        while len(middle) >= 3:
            three_char = middle[:3]
            middle = middle[3:]
            shuffled_three_char = ''.join(sample(three_char, len(three_char)))

            if shuffled_three_char != three_char:
                shuffled_text.append(shuffled_three_char)

        if len(middle) == 1:
            shuffled_text.append(middle)
        elif len(middle) == 2:
            shuffled_text.append(middle[1] + middle[0])
        else:
            shuffled_text.append(middle)

        middle_part = ''.join(shuffled_text)
        shuffled_words.append(first_char + middle_part + last_char)
    return ' '.join(shuffled_words)


def main():
    text = input('Enter any text: ')
    shuffled_text = pemrtuate(text)
    print(shuffled_text)


if __name__ == "__main__":
    main()
