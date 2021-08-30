# import random

# string = "kick"
# s_string = [i for i in string]
# anagram = random.choice(s_string)
# print(anagram)
# for item in s_string:
#     pass


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    s = input()

    N, K, S = map(int, s.split())

    # Initial
    total_time_taken = K - 1

    # Case 1: if it is the fastest way to start from initial stage
    # total_time_taken += N + 1 (restart 1 min + N minutes for completing until N th level)

    # Case 2: if take back step is more faster than start from scratch
    # total_time_taken += (K - S) + (N - S + 1) (N-S level to complete + S level)

    # Mixed
    total_time_taken += N + 1 if (K + N - 2 * S + 1) >= (N + 1) else (K + N - 2 * S + 1)

    print("Case #{}: {}".format(i, total_time_taken))