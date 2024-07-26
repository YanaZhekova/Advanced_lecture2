import math
n = int(input())
odd_sum = set()
even_sum = set()
for row in range(1, n + 1, 1):
    name = input()
    sum_char = math.floor(sum(ord(x) for x in name) / row)
    if sum_char % 2 == 0:
        even_sum.add(sum_char)
    else:
        odd_sum.add(sum_char)

sum_odd_set = sum(x for x in odd_sum)
sum_even_set = sum(x for x in even_sum)

if sum_odd_set == sum_even_set:
    print(*(odd_sum.union(even_sum)),sep=", ")
elif sum_odd_set > sum_even_set:
    print(*(odd_sum.difference(even_sum)), sep=", ")
else:
    print(*(odd_sum.symmetric_difference(even_sum)), sep=", ")
