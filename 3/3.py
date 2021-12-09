from functools import reduce

input_file = open('input.txt', 'r')

acc = [0] * 12
take_bit = lambda ac, b: ac + 1 if b == '1' else ac - 1
for line in input_file:
    bits = list(line)
    acc = list(map(take_bit, acc, bits))

gamma = list(map(lambda b: 1 if b > 0 else 0, acc))
epsilon = list(map(lambda b: 1 if b == 0 else 0, gamma))


def to_dec(it):
    return reduce(
      lambda ac, bitpos: ac + (2 ** (bitpos[0])) * bitpos[1],
      enumerate(reversed(it)), 0)


print(to_dec(gamma) * to_dec(epsilon))
