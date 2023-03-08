import sys

args = sys.argv
input = ''

with open(args[1], 'r') as f:
    input = f.read().splitlines()

def point_in(start, end, point):
    if start <= point and end >= point:
        return True
    return False

def overlap(a, b):
    if point_in(a[0], a[1], b[0]):
        return True
    if point_in(a[0], a[1], b[1]):
        return True
    if point_in(b[0], b[1], a[1]):
        return True

    return False

def get_lines(str):
    str = str.split(',')
    # a, b
    # c, d

    first_pair = str[0].split('-')
    second_pair = str[1].split('-')

    a = first_pair[0]
    b = first_pair[1]
    c = second_pair[0]
    d = second_pair[1]

    return [
        [int(a),int(b)],
        [int(c),int(d)]
    ]

number_of_hits = 0

for l in input:
    a, b = get_lines(l)

    if overlap(a,b):
        number_of_hits += 1

testCases = [
    [0,2,1,3], # ACBD
    [1,3,0,2], # CADB
    [1,2,0,3]  # CABD
]

for t in testCases:
    print(overlap(
        [t[0],t[1]],
        [t[2],t[3]]
    ))

print(number_of_hits)