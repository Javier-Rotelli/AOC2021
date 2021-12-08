input_file = open('input.txt', 'r')

increased_count = -1
last_depth = 0
for line in input_file:
    depth = int(line)
    if depth > last_depth:
        increased_count += 1
    last_depth = depth

print(increased_count)