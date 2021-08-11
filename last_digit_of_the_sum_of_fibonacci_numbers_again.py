# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = (fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]) % 10


    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10

def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = (fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]) % 10

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0
    if from_index == 0:
        return last_digit_of_the_sum_of_fibonacci_numbers_naive(to_index % 60)

    start = from_index % 60 - 1

    stop = to_index % 60

    start_last = last_digit_of_the_sum_of_fibonacci_numbers_naive(start)
    stop_last = last_digit_of_the_sum_of_fibonacci_numbers_naive(stop)

    if stop_last >= start_last:
        return stop_last - start_last

    else:
        return (stop_last + 10) - start_last





if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    #print(last_digit_of_the_sum_of_fibonacci_numbers_again_naive(input_from, input_to))
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
