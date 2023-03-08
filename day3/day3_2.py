import sys

args = sys.argv

input = ''
with open(args[1],'r') as f:
    input = f.read().splitlines()

def get_rucksack(str):
    l = int(len(str) / 2)
    return [
        str[0:l],
        str[l:]
    ]

def get_lowercase_priority(c):
    return ord(c) - 96

def get_uppercase_priority(c):
    return ord(c) - (65 - 27)

def get_priority(c):
    if c.isupper():
        return get_uppercase_priority(c)
    
    return get_lowercase_priority(c)

def match_char(str):
    res = get_rucksack(str)
    x = set(res[0])
    y = set(res[1])

    return list(x.intersection(y))[0]

def match_lines(lines):
    res = None
    for l in  lines:
        s = set(l)
        if res == None:
            res = s
        else:
            res = res.intersection(s)

    return list(res)[0]

total_priority = 0

group = []
for l in input:
    group.append(l)

    if len(group) == 3:
        total_priority += get_priority(match_lines(group))
        group = []

print(total_priority)