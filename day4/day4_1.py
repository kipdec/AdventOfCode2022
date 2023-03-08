import sys

args = sys.argv
input = ''

with open(args[1], 'r') as f:
    input = f.read().splitlines()

def point_in(start, end, point):
    if start <= point and end >= point:
        return True
    return False

def contains_line(a, b):
    if point_in(a[0], a[1], b[0]) and point_in(a[0], a[1], b[1]):
        return True
    
    return False

def either_contains(a, b):
    if contains_line(a, b):
        return True

    if contains_line(b, a):
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

    if either_contains(a,b):
        number_of_hits += 1

print(number_of_hits)