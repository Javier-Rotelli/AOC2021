input_file = open('input.txt', 'r')

position = 0
depth = 0
aim = 0

for line in input_file:
    what, value, *_ = str.split(line)
    if what == 'up':
        aim -= int(value)
    elif what == 'down':
        aim += int(value)
    elif what == 'forward':
        position += int(value)
        depth += int(value) * aim

print(depth * position)
