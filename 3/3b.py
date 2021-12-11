from functools import reduce

input_file = open('input.txt', 'r')

all_inputs = []
for line in input_file:
    bits = list(line)
    all_inputs.append(list(int(b) for b in bits[:-1]))


def nearest_one(it, bit_criteria, pos=0):
    expected = bit_criteria(it, pos)
    filtered = [i for i in it if i[pos] == expected]
    return filtered[0] if len(filtered) == 1 else nearest_one(filtered, bit_criteria, pos + 1)


def most_common(it, pos): return 1 if len([bit for bit in it if bit[pos] == 1]) >= len(it)/2 else 0
def least_common(it, pos): return 0 if len([bit for bit in it if bit[pos] == 1]) >= len(it)/2 else 1


oxygen_rating = nearest_one(all_inputs, most_common)
co2_rating = nearest_one(all_inputs, least_common)


def to_dec(it):
    return reduce(
        lambda ac, bitpos: ac + (2 ** (bitpos[0])) * bitpos[1],
        enumerate(reversed(it)), 0)


print(to_dec(oxygen_rating) * to_dec(co2_rating))
