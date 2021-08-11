# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = [1]


    list_sum = [1]
    summ = 1
    candy = 1
    # if n == 1:
    #     return summands
    while summ <= n:
        candy = candy + 1
        summ += candy
        if summ <= n:
            summands.append(candy)
            list_sum.append(summ)
    summands[-1] = n - sum(summands[: -1])
    return summands




if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
