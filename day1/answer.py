source = ""

with open("input", "r") as f:
    source = f.readlines()

top_3 = [0,0,0]
current = 0

def check(num):
    for i in range(3):
        if num > top_3[i]:
            # push down the others
            j = 0
            while(j < i):
               top_3[j] = top_3[j + 1]
               j += 1
            
            top_3[i] = num


for l in source:
    l = l.rstrip('\n')
    if l == "":
        check(current)
        current = 0
    else:
        current += int(l)

print(sum(top_3))