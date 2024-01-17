# Процедурная парадигма — возможность переиспользования кода в программе:

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prod = i * j
            print(f'{i} * {j} = {prod}')
        print('----------')


n = int(input('Enter the number n: '))
multiplication_table(n)


# Структурная парадигма — быстрая проверка кода на работоспособность:

m = int(input('Enter the number m: '))

for i in range(1, m + 1):
    for j in range(1, m + 1):
        print(f'{i} * {j} = {i * j}')
    print('----------')
