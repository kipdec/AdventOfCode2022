import sys


args = sys.argv

input = ''

with open(args[1], 'r') as f:
    input = f.read().splitlines()

breakFound = False

boardState = []
moves = []
for l in input:
    if breakFound:
        moves.append(l)
    else:
        if l == '':
            breakFound = True
            continue
        boardState.append(l)

# Get the max
max_line = boardState[-1]
max_line_items = max_line.split()
slots = len(max_line_items)

boardState = boardState[:-1]

def process_crates(line, slots):
    section = [' '] * slots
    line = line[1:]
    pos = 0
    while pos < len(line):
        slot = int(pos / 4)
        section[slot] = line[pos]
        pos += 4
    
    return section

board = []
for line in boardState:
    board.append(process_crates(line, slots))

def print_board(board):
    for row in board:
        print(row)

def parse_move(move):
    move_arr = move.replace('move','').replace('from','').replace('to','').split()
    return move_arr

def get_height(board):
    return len(board)

def get_next_row(board, c):
    prev_row = None
    for i in range(len(board)):
        row = board[i]
        if row[c] != ' ':
            return prev_row
        else:
            prev_row = i
    
    return prev_row

def get_top_item(board, c):
    for i in range(len(board)):
        row = board[i]
        if row[c] != ' ':
            return i
    
    return None

def search_items(board, c, depth):
    coords = []
    for i in range(len(board)):
        if len(coords) == depth: 
            return coords

        row = board[i]
        if row[c] != ' ':
            coords.insert(0, i)
    
    return coords

def get_item(board, x, y):
    return board[y][x]

def set_item(board, x, y, item):
    board[y][x] = item
    return board

def move_item(board, x1,y1,x2,y2):
    item = get_item(board, x1,y1)
    #print(item)
    board[y1][x1] = ' '
    board[y2][x2] = item
    return board

def add_row(board):
    empty_row = [' '] * len(board[0])
    board.insert(0, empty_row)
    return board

def apply_move(board, move):
    move_arr = parse_move(move)
    quantity = int(move_arr[0])
    origin = int(move_arr[1]) - 1
    dest = int(move_arr[2]) - 1

    items = search_items(board, origin, quantity)
    #print(items)
    offset = 0
    for y1 in items:
        y1 += offset
        y2 = get_next_row(board, dest)
        if y2 == None:
            add_row(board)
            #print(f"Added a row \n")
            offset += 1
            y1 += 1
            y2 = get_next_row(board, dest)
        
        board = move_item(board, origin, y1, dest, y2)
        #print(f"Moved\n")
    
    return board
        
    #print(f"Move: {move}")
for move in moves:
    board = apply_move(board, move)
    #print_board(board)

print_board(board)
        




    
