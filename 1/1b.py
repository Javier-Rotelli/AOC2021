input_file = open('input.txt', 'r')

increased_count = 0
depths = [int(line) for line in input_file]

for i in range(len(depths)):
    window = depths[i-3:i]
    window_depth = sum(window)
    previous_window = depths[i-4:i-1]
    previous_window_depth = sum(previous_window)
    if window_depth > previous_window_depth:
        increased_count += 1

print(increased_count)
