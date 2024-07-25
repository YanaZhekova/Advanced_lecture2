n = int(input())
cars = set()
for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        cars.remove(car_number)

if len(cars) == 0:
    print("Parking Lot is Empty")
else:
    print(*cars, sep="\n")
