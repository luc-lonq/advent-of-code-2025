numbers = []
operations = []
total = 0

with open("input.txt", "r") as f:
	for l in f:
		parsed_line = l[:-1].split(' ')
		if parsed_line[0] in ['*', '+']:
			for c in parsed_line:
				if c != '':
					operations.append(c)
		else:
			numbers_line = []
			for c in parsed_line:
				if c != '':
					numbers_line.append(c)
			numbers.append(numbers_line)

print(numbers)
print(operations)

for i in range(len(operations)):
	op = operations[i]
	column_total = 0 if op == '+' else 1
	for n in numbers:
		num = int(n[i])
		if op == '*':
			column_total *= num
		elif op == '+':
			column_total += num
	print(f"Column {i} total: {column_total}")
	total += column_total

print(total)