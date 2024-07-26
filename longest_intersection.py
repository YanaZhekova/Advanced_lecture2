def sets(ranges):
    returned_set = set()
    set_parts = ranges.split(",")
    start = int(set_parts[0])
    end = int(set_parts[1])
    for i in range(start, end+1, 1):
        returned_set.add(i)
    return returned_set


n = int(input())
largest_set = set()
for _ in range(n):
    ranges = input().split("-")
    first_set = sets(ranges[0])
    second_set = sets(ranges[1])
    intersection = first_set.intersection(second_set)
    if len(intersection)>len(largest_set):
        largest_set = intersection
result = ", ".join(list(str(x) for x in largest_set))

print(f"Longest intersection is [{result}] with length {len(largest_set)}")