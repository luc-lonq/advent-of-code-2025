lines = []
numbers = []
operations = []
total = 0

with open("input.txt", "r") as f:
	for l in f:
		line = l[:-1]
		if line[0] in ['*', '+']:
			for c in line:
				if c != ' ':
					operations.append(c)
		else:
			lines.append(line)

for l in lines:
	print(l)

max_length = max(len(l) for l in lines)

for i in range(max_length):
	formed_number = 0
	numbers_in_column = []
	for j in range(len(lines)):
		if i < len(lines[j]) and lines[j][i] != ' ':
			numbers_in_column.append(int(lines[j][i]))
	for n in numbers_in_column:
		formed_number = formed_number * 10 + n
	numbers.append(formed_number)

print(numbers)

j = 0

for i in range(len(operations)):
	n = 0 if operations[i] == '+' else 1
	op = operations[i]
	print
	while j < len(numbers) and numbers[j] != 0:
		if op == '*':
			n = n * numbers[j]
		elif op == '+':
			n = n + numbers[j]
		j += 1
	j += 1
	print(f"Operation {i} total: {n}")
	total += n

print(total)
