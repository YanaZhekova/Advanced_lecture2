n = int(input())
names_set = set()
for _ in range(n):
    name = input()
    names_set.add(name)

print(*names_set, sep="\n")
