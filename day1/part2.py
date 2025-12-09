def update(line, value, password):
    for _ in range(int(line[1:])):
        if line[0] == 'R':
            value += 1
        elif line[0] == 'L':
            value -= 1
        if value < 0:
            value += 100
        elif value > 99:
            value -= 100
        if value == 0:
            password += 1
    return value, password

with open("input.txt", "r") as f:
    value = 50
    password = 0
    for line in f:
        #print("=====")
        #print("line: " + str(line))
        #print("value: " + str(value))
        #print("password: " + str(password))
        if line != "\n":
            value, password = update(line, value, password)

print("end value: " + str(value))
print("end password: " + str(password))
