
import sys

args = sys.argv

input = ''

#input = [args[1]]
with open(args[1], 'r') as f:
    input = f.read().splitlines()

def isPacketStart(str):
    if len(str) != 4:
        return False

    count = 0
    while len(str) > 0:
        #print(str)
        count += 1
        str = str.replace(str[0],'')
    
    if count != 4:
        return False

    return True

def isMessageStart(str):
    if len(str) != 14:
        return False

    count = 0
    while len(str) > 0:
        #print(str)
        count += 1
        str = str.replace(str[0],'')
    
    if count != 14:
        return False

    return True

def processStreamForStart(stream):
    processed = []
    packet = ''
    for c in stream:
        if len(packet) > 3:
            packet = packet[1:]
        packet = f"{packet}{c}"
        processed.append(c)
        #print(packet)
        #print(processed)
        if isPacketStart(packet):
            
            return len(processed)

def processStreamForMessage(stream):
    processed = []
    packet = ''
    for c in stream:
        if len(packet) > 13:
            packet = packet[1:]
        packet = f"{packet}{c}"
        processed.append(c)
        #print(packet)
        #print(processed)
        if isMessageStart(packet):
            
            return len(processed)

print(f"Part 1: {processStreamForStart(input[0])}")
print(f"Part 2: {processStreamForMessage(input[0])}")
