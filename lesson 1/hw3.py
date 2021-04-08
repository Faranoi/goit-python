if __name__ == '__main__':
    n = int(input('Введите номер вычесляемого члена: '))


def fibonacci(n):
    print(n)
    if 0 < n <=2:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(n))