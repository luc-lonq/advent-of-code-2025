value = 50
password = 0


def update_value(line):
    global value
    if line[0] == 'R':
        value += int(line[1:])
    elif line[0] == 'L':
        value -= int(line[1:])

def verify_value():
    global value
    while value < 0 or value > 99:
        if value < 0:
            value += 100
        elif value > 99:
            value -= 100

def is_value_zero():
    global value, password
    if value == 0:
        password += 1

with open("input.txt", "r") as f:
    for line in f:
        # print("=====")
        # print("line: " + str(line))
        # print("value: " + str(value))
        # print("password: " + str(password))
        update_value(line)
        verify_value()
        is_value_zero()

print("end value: " + str(value))
print("end password: " + str(password))
