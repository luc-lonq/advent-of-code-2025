total = 0

with open("input.txt", "r") as f:
    for l in f:
        if l != "\n":
            nb_max = 0
            for i in range(len(l) - 1):
                for j in range(i + 1, len(l) - 1):
                    nb = int(l[i]) * 10 + int(l[j])
                    if nb > nb_max:
                        nb_max = nb
            total += nb_max
print(total)