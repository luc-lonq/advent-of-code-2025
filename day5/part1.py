doubles = []
total = 0

with open("input.txt", "r") as f:
    for l in f:
        if l != "\n":
            if '-' in l:
                a, b = l[:-1].split('-')
                doubles.append((int(a), int(b)))
            else:
                n = int(l)
                for a, b in doubles:
                    if a <= n <= b:
                        total += 1
                        break

print(total)