# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    prices_for_1 = {(price / weights[i]) : i for i, price in enumerate(prices)}
    # print(capacity)
    # print(weights)
    # print(prices)
    # print(prices_for_1)

    v = 0
    w = 10 ** 4

    while capacity != 0 and w != 0:
        max_price = max(prices_for_1.keys())
        idx_max = prices_for_1[max_price]
        a = min(capacity, weights[idx_max])
        v += a * max_price
        capacity = capacity - a
        weights[idx_max] = weights[idx_max] - a
        if len(prices_for_1.keys()) > 1:
            prices_for_1.pop(max_price)
        min_price = min(prices_for_1.keys())
        idx_min = prices_for_1[min_price]
        w = weights[idx_min]


    return v


# if __name__ == "__main__":
#     data = list(map(int, input().split()))
#     n, input_capacity = data[0:2]
#     input_prices = data[2:(2 * n + 2):2]
#     input_weights = data[3:(2 * n + 2):2]
#     opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
#     print("{:.10f}".format(opt_value))


#3 50 60 20 100 50 120 30
data = list(map(int, stdin.read().split()))
n, input_capacity = data[0:2]
input_prices = data[2:(2 * n + 2):2]
input_weights = data[3:(2 * n + 2):2]
opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
print("{:.10f}".format(opt_value))
