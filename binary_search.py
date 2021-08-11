# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, l, h, query):
    #assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    #assert 1 <= len(keys) <= 3 * 10 ** 4

    if h - l == 1:
        if keys[l] == query:
            return l
        else:
            return -1

    mid = l + (h - l) // 2

    if keys[mid] > query:
        return binary_search(keys, l, mid, query)
    else:
        return binary_search(keys, mid, h, query)


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]
    low = 0
    high = len(input_keys)
    for q in input_queries:
        print(binary_search(input_keys, low, high, q), end=' ')

