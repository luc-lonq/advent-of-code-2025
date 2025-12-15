doubles = []
full_range = []
total = 0

with open("input.txt", "r") as f:
    for l in f:
        if l != "\n":
            if '-' in l:
                a, b = l[:-1].split('-')
                doubles.append((int(a), int(b)))

print(doubles)
full_range.append(doubles[0])

for a, b in doubles[1:]:
    if full_range:
        print("Checking range: " + str((a, b)))
        range_to_remove = []
        for f in full_range:
            if a >= f[0] and a <= f[1] or b >= f[0] and b <= f[1] or a <= f[0] and b >= f[1]:
                print("Range conflict between: " + str((a, b)) + " and " + str(f))
                a, b = min(a, f[0]), max(b, f[1])
                range_to_remove.append(f)
                new_range = True
        for r in range_to_remove:
            full_range.remove(r)
            print("Removing range: " + str(r))
        full_range.append((a, b))
    else:
        full_range.append((a, b))

print(full_range)

for a, b in full_range:
    total += b - a + 1

print(total)

