# python3


def money_change(money):
    assert 1 <= money <= 10 ** 3
    if money % 10 == 0:
        return int(money / 10)
    else:
        k_10 = money // 10

        k_5 = (money - k_10 * 10) // 5

        k_1 = (money - k_10 * 10 - k_5 * 5)

        return k_1 + k_5 + k_10


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
