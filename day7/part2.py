lines = []
number_timeline = 0

with open("input.txt", "r") as f:
  for l in f:
    lines.append(l[:-1])

for l in range(len(lines) - 1):
  for idx, c in enumerate(lines[l]):
    if c == 'S':
      lines[l+1] = lines[l+1][:idx] + '|' + lines[l+1][idx+1:]
    elif c == '|':
      if lines[l+1][idx] == '^':
        if lines[l][idx-1] != '|':
          lines[l+1] = lines[l+1][:idx-1] + '|' + lines[l+1][idx:]
        if lines[l][idx+1] != '|':
          lines[l+1] = lines[l+1][:idx+1] + '|' + lines[l+1][idx+2:]
      else:
        lines[l+1] = lines[l+1][:idx] + '|' + lines[l+1][idx+1:]
  print("".join(lines[l]))

branch_values = [0] * len(lines[0])
for l in range(len(lines) - 1):
  new_branch_values = branch_values.copy()
  for idx, c in enumerate(lines[l]):
    if lines[l][idx] == '|':
      if idx - 1 >= 0 and lines[l][idx-1] == '^':
        new_branch_values[idx] += branch_values[idx-1]
        new_branch_values[idx-1] = 0
      if idx + 1 < len(lines[l]) and lines[l][idx+1] == '^':
        new_branch_values[idx] += branch_values[idx+1]
        new_branch_values[idx+1] = 0

    elif lines[l][idx] == 'S':
      new_branch_values[idx] = branch_values[idx] + 1

  branch_values = new_branch_values

number_timeline = sum(branch_values)
print(number_timeline)




