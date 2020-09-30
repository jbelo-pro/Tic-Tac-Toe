words = input().lower().split()

r = words[0]

if len(words) > 1:
    for w in words[1:]:
        r = r + w.capitalize()
print(r)
