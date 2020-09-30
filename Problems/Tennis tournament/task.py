n_lines = int(input())

winners = []
for l in range(n_lines):
    i = input().split(' ')
    if i[1] == 'win':
        winners.append(i[0])

print(winners)
print(len(winners))
