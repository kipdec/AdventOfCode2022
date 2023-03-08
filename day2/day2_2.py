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
loses = {
    'Paper':'Scissors',
    'Scissors':'Rock',
    'Rock':'Paper'
}

shape_score = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

outcomes = {
    'X':'lose',
    'Y':'draw',
    'Z':'win'
}

def lose_hand(elf_hand):
    return beats[elf_hand]

def draw_hand(elf_hand):
    return elf_hand

def win_hand(elf_hand):
    return loses[elf_hand]

def choose_hand(outcome, elf_hand):
    if outcome == 'lose':
        return lose_hand(elf_hand)
    if outcome == 'draw':
        return draw_hand(elf_hand)

    return win_hand(elf_hand)

def score(hand_a, hand_b):
    if hand_a == hand_b:
        return 3
    
    if beats[hand_a] == hand_b:
        return 0

    return 6

def scorer(elf_input, me_input):
    return shape_score[me_input] + score(elf_map[elf_input], me_input)

def parser(line):
    elf_hand = line[0]
    outcome = outcomes[line[2]]

    me_hand = choose_hand(outcome, elf_map[elf_hand])
    #print(me_hand)


    return scorer(elf_hand, me_hand)

scores = []
for l in input:
    #print(parser(l))
    scores.append(parser(l))

print(sum(scores))