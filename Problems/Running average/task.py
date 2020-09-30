numbers = [int(x) for x in input()]
r = []
for p in range(len(numbers) - 1):
    r.append((numbers[p] + numbers[p + 1]) / 2)
print(r)
