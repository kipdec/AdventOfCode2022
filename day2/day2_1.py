import sys


input = ""

args = sys.argv
with open(args[1], "r") as f:
    input = f.readlines()

elf_map = {
    'A':'Rock',
    'B':'Paper',
    'C':'Scissors'
}

me_map = {
    'X':'Rock',
    'Y':'Paper',
    'Z':'Scissors'
}

beats = {
    'Rock':'Scissors',
    'Paper':'Rock',
    'Scissors':'Paper'
}

shape_score = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

def score(hand_a, hand_b):
    if hand_a == hand_b:
        return 3
    
    if beats[hand_a] == hand_b:
        return 0

    return 6

def scorer(elf_input, me_input):
    return shape_score[me_map[me_input]] + score(elf_map[elf_input], me_map[me_input])

def parser(line):
    elf_hand = line[0]
    me_hand = line[2]

    return scorer(elf_hand, me_hand)



scores = []
for l in input:
    scores.append(parser(l))

print(sum(scores))