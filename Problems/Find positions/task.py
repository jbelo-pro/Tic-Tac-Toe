# put your python code here
sequence = input().split()
number = input()

pos = []

for x in range(len(sequence)):
    if sequence[x] == number:
        pos.append(str(x))

if pos:
    print(' '.join(pos))
else:
    print('not found')
