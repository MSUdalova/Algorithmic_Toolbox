# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    stops.append(d)
    stops.insert(0, 0)
    #print(stops)
    n = len(stops)
    n_refills = 0
    current_refill = 0
    if d <= m:
        return 0
    else:
        while current_refill < n - 1:
            last_refill = current_refill
            while (current_refill < n - 1 and
                   (stops[current_refill + 1] - stops[last_refill]) <= m):
                current_refill += 1
                #print('current_refill')
                #print(current_refill)
            if current_refill == last_refill:
                return -1
            if current_refill < n - 1:
                n_refills += 1
                #print(n_refills)
        return n_refills





if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n


    print(compute_min_number_of_refills(input_d, input_m, input_stops))
#200 375 550 750
