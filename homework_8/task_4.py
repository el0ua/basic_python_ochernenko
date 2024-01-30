def gen_primes():
    primes_list = [2]
    for i in range(3, 101, 2):
        is_prime = True
        for n in range(3, int(i**0.5) + 1, 2):
            if i % n == 0:
                is_prime = False
                break

        if is_prime:
            primes_list.append(i)
    return primes_list


def main():
    result = gen_primes()
    print(f'Прості числа в діапазоні від 1 до 100: {result}')


if __name__ == '__main__':
    main()
