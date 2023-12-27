def lchain(*iterables):
    result = []
    for element in iterables:
        result.extend(element)
    return result


def main():
    iterables = ([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10))
    print(lchain(*iterables))


if __name__ == '__main__':
    main()