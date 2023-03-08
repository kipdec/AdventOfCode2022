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

sum_priorities = 0

for l in input:
    sum_priorities += get_priority(match_char(l))


print(sum_priorities)