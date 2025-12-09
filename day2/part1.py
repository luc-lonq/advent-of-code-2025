invalid_ids = []
txt = ""

with open("input.txt", "r") as f:
    for l in f:
        if l != "\n":
            txt += l

ranges = txt.split(",")
for r in ranges:
    n1, n2 = r.split("-")
    n1 = int(n1)
    n2 = int(n2)
    for i in range(n1, n2 + 1):
        i_str = str(i)
        if len(i_str) % 2 == 0:
            if i_str[len(i_str)//2:] == i_str[:len(i_str)//2]:
                invalid_ids.append(i)

total = 0
for invalid_id in invalid_ids:
    total += invalid_id
print(total)
