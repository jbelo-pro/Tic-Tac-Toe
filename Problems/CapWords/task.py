sentence = input().split('_')

f = ''
for w in sentence:
    f = f + w.lower().capitalize()

print(f)