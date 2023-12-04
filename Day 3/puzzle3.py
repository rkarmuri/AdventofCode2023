file_path = './day3.txt'

with open(file_path) as file:
    lines = file.read().strip().split("\n")

rows,cols = len(lines),len(lines[0])
result1,result2 = 0,0

gears = [[[]for _ in range(cols)]for _ in range(rows)]

# First we find the symbols across each grid
def check_symbol(i,j,num):
    # Check if the number or symbol is within the grid
    if not (0 <= i< rows and 0 <= j< cols):   return False
    # Get the number that has '*' as adjacent for part 2
    if lines[i][j] == "*": gears[i][j].append(num)
    return lines[i][j] != "." and not lines[i][j].isdigit()

for row,line in enumerate(lines):
    start,cur_col = 0,0
    
    while cur_col < cols:
        start = cur_col
        num = ""

        # To get the number as a whole if it is 2 or more digits
        while cur_col < cols and line[cur_col].isdigit():
            num += line[cur_col]
            cur_col += 1

        # If it is a period(.) just move the current column
        if num=="":
            cur_col += 1
            continue

        num = int(num) 

        # Check if the adjacents of numbers have symbols on both sides
        if check_symbol(row,start-1,num) or check_symbol(row,cur_col,num):
            result1 += num
            continue
        
        # Check the diagonals(top-left,bottom-left,top-right,bottom-right) of the numbers for symbols 
        for i in range(start-1,cur_col+1):
            if check_symbol(row-1,i,num) or check_symbol(row+1,i,num):
                result1 += num
                break

# Multiply the part numbers and add all the geared numbers across the grids
for i in range(rows):
    for j in range(cols):
        nums = gears[i][j]
        if lines[i][j]=="*" and len(nums)==2:
            result2 += nums[0] * nums[1]

print('Part 1 answer: ',result1)
print('Part 2 answer: ',result2)

