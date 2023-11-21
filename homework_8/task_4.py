def gen_primes():
    primes_list = list()
    for i in range(2, 101):
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            primes_list.append(i)
    return primes_list


def main():
    result = gen_primes()
    print(f'Прості числа в діапазоні від 1 до 100: {result}')


if __name__ == '__main__':
    main()
