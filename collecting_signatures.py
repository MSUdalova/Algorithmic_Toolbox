# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')

def compute_optimal_points(segments):
    n = len(segments)
    points = []
    curr_seg = 0
    idx = 1

    while curr_seg < n and idx < n:
        l_curr = segments[curr_seg][0]
        r_curr = segments[curr_seg][1]
        l_next = segments[idx][0]
        r_next = segments[idx][1]
        if l_next > r_curr:
            points.append(r_curr)
            curr_seg = idx
            idx += 1
        else:
            if r_next <= r_curr:
                curr_seg = idx
                idx += 1
            elif r_next > r_curr:
                idx += 1
    r_curr = segments[curr_seg][1]
    points.append(r_curr)
    return points



if __name__ == '__main__':
    n = int(input())
    input_segments = []
    for i in range(n):
        input_segments.append(list(map(int, input().split())))

    input_segments.sort(key=lambda x: x[0])
    # print(input_segments)

    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)




# 3
# 1 3
# 2 5
# 3 6
# 1 3 2 5 3 6
# if __name__ == '__main__':
#     print('hi')
#     n, *data = map(int, stdin.read().split())
#     print('говно какое-то')
#     input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#     print(input_segments)
#     assert n == len(input_segments)
#     output_points = compute_optimal_points(input_segments)
#     print(output_points)
#     print(len(output_points))
#     print(*output_points)

   # starts = []
    # ends = []
    # for i in range(n):
    #     starts.append((input_segments[i][0],0, i))
    #     ends.append((input_segments[i][1],1, i))
    # starts.sort()
    # ends.sort()
