# put your python code here
word = input().split()
print(round(len([x for x in word if x == 'A'])/len(word), 2))
