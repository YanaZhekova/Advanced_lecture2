numbers = list((x for x in input().split()))
numbers_dict = dict()

for num in numbers:
    count_num = numbers.count(num)
    if num not in numbers_dict:
        numbers_dict[num] = count_num

for i in numbers_dict.items():
    num, count = i
    print(f"{float(num):.1f} - {count} times")
