# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 100
    list = []
    list.append(0)
    list.append(1)

    for i in range(2, n + 1):
        list.append(list[i - 1] + list[i - 2])

    return list[n]







if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))



