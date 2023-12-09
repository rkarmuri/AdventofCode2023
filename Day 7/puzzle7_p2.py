file_path = './day7.in'

# We use . for J as the ASCII value of symbols are lower than the numbers
letter_map = {'T':'A','J':'.','Q':'C','K':'D','A':'E'}
plays = []
result = 0

def score(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 7
    elif 4 in counts:
        return 6
    elif 3 in counts and 2 in counts:
        return 5
    elif 3 in counts and 1 in counts:
        return 4
    elif counts.count(2) == 4:
        return 3
    elif 2 in counts:
        return 2
    return 1

def replacements(hand):
    if hand=="":
        return [""]
    # We are trying to replace J with rest of the elements when 1st character is J
    # This checks all possible replacements of every element 
    return [
        x+y for x in ("23456789TQKA" if hand[0]=="J" else hand[0]) 
        for y in replacements(hand[1:])]

def classify(hand):
    return max(map(score,replacements(hand)))

def compare(hand):
    return (classify(hand),[letter_map.get(char,char) for char in hand])

with open(file_path, 'r') as file:
    lines = file.read().strip().split("\n")

    for line in lines:
        line = line.split()
        plays.append((line[0], int(line[1])))

    plays.sort(key=lambda x: compare(x[0]))

print(plays)

for i, value in enumerate(plays):
    result += (i + 1) * value[1]

print(result)
