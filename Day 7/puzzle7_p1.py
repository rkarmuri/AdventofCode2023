file_path = './day7.in'

# We use letter mapping to make the sorting easy when comparing same ranked cards
letter_map = {'T':'A','J':'B','Q':'C','K':'D','A':'E'}
plays = []
result = 0

def get_type(hand):
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

def compare(hand):
    return (get_type(hand),[letter_map.get(char,char) for char in hand])

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
