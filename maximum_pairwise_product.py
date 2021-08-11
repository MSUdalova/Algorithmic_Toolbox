# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    n = len(numbers)
    index_max_1 = 0
    index_max_2 = 0

    for i in range(n - 1):
        if numbers[i + 1] > numbers[index_max_1]:
            index_max_1 = i + 1

    a = numbers[index_max_1]

    del numbers[index_max_1]

    n -= 1

    for i in range(n - 1):
        if numbers[i + 1] > numbers[index_max_2]:
            index_max_2 = i + 1
    return numbers[index_max_2] * a


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))


