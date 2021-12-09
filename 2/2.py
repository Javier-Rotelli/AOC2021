input_file = open('input.txt', 'r')

position = 0
depth = 0

for line in input_file:
    what, value, *_ = str.split(line)
    if what == 'up':
        depth -= int(value)
    elif what == 'down':
        depth += int(value)
    elif what == 'forward':
        position += int(value)

print(depth * position)
