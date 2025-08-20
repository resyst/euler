with open('0022_names.txt') as f:
    names = sorted(name.strip('"') for name in f.read().split(','))

total = sum(i * sum(ord(c) - ord('A') + 1 for c in name) for i, name in enumerate(names, 1))
print(total)
