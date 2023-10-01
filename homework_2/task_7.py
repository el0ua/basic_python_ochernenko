number = int(input('Введіть довільне ціле число (не більше 63): '))

b1, r1 = divmod(number, 32)
b2, r2 = divmod(r1, 16)
b3, r3 = divmod(r2, 8)
b4, r4 = divmod(r3, 4)
b5, r5 = divmod(r4, 2)
b6, r6 = divmod(r5, 1)
print(str(b1) + str(b2) + str(b3) + str(b4) + str(b5) + str(b6))