lines = []
number_split = 0

with open("input.txt", "r") as f:
  for l in f:
    lines.append(l[:-1])

for l in range(len(lines) - 1):
  for idx, c in enumerate(lines[l]):
    if c == 'S':
      lines[l+1] = lines[l+1][:idx] + '|' + lines[l+1][idx+1:]
    elif c == '|':
      if lines[l+1][idx] == '^':
        lines[l+1] = lines[l+1][:idx-1] + '|^|' + lines[l+1][idx+2:]
        number_split += 1
      else:
        lines[l+1] = lines[l+1][:idx] + '|' + lines[l+1][idx+1:]
  print("".join(lines[l]))
print(f"Splits {number_split}")



