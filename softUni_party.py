n = int(input())
vip_guest = set()
normal_guest = set()

for _ in range(n):
    reservation_code = input()
    if reservation_code[0].isdigit():
        vip_guest.add(reservation_code)
    else:
        normal_guest.add(reservation_code)

command = input()

while command != "END":
    if command in vip_guest:
        vip_guest.remove(command)
    else:
        normal_guest.remove(command)
    command = input()

vip_sorted = sorted(vip_guest)
normal_sorted = sorted(normal_guest)


all_guest = vip_guest.union(normal_guest)
print(len(all_guest))
print(*vip_sorted, sep="\n")
print(*normal_sorted, sep="\n")
