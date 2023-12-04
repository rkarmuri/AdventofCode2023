file_path = './day4.txt'

def count_occurrences(wins, nums):
    count = 0
    for w in wins:
        count += nums.count(w)
    return count

result1 = 0

with open(file_path,'r') as file:
    lines = file.read().strip().split("\n")
    scratch_cards = [[]for _ in range(len(lines)+1)]

    for i,line in enumerate(lines):
        cards_info = line.split(':')
        card_ids, card_lists = cards_info[0], cards_info[1]
        win_nums, user_nums = map(str.split,card_lists.split('|'))
        row_counts = count_occurrences(win_nums,user_nums)

        if row_counts>0:
            result1 += 2**(row_counts-1)

        # Based on the number of scratch cards, we store them in a list
        for j in range(i+1,i+row_counts+1):
            scratch_cards[i].append(j)

# Part 2
total_cards = [0] + [1 for _ in range(len(lines))]

# We go from the last card to the 1st card as we know the no of scratch cards for each card
for i in range(len(lines)-1,-1,-1):
    for j in scratch_cards[i]:
        total_cards[i] += total_cards[j]

result2 = sum(total_cards)

print(result1)
print(result2)



