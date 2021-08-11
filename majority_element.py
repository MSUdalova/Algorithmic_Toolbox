# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements, l, r):
    #assert len(elements) <= 10 ** 5
    if r - l == 2:
        if elements[0] == elements[1]:
            return elements[l]
        else:
            return -1
    if r - l == 1:
        return elements[r - 1]
    else:
        mid = r - l // 2
        a = majority_element(elements, r, mid)
        b = majority_element(elements, mid, r)
    if a != -1:
        count_a = 0
        for i in range(r,l):
            if elements[i] == a:
                count_a += 1
    if b != -1:
        count_b = 0
        for i in range(r, l):
            if elements[i] == b:
                count_b += 1
    if count_a > mid:
        return a
    if count_b > mid:
        return b






if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n

    print(majority_element(input_elements, 0, input_n))
