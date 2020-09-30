sentence = input().split()

words = [w for w in sentence if w.endswith('s')]

print('_'.join(words))
