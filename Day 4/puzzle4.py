file_path = './day4.txt'

def count_occurrences(wins, nums):
    count = 0
    for w in wins:
        count += nums.count(w)
    return count

result1 = 0
with open(file_path,'r') as file:
    for line in file:
        cards_info = line.split(':')
        card_ids, card_lists = cards_info[0], cards_info[1]
        win_nums, user_nums = map(str.split,card_lists.split('|'))
        row_counts = count_occurrences(win_nums,user_nums)
        if row_counts>0:
            result1 += 2**(row_counts-1)

print(result1)



