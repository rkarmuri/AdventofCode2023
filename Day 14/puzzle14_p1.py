def move_zeroes(rows):
    for j in range(len(rows[0])):
        slot = 0
        for i in range(len(rows)):
            if rows[i][j] == '#':
                slot = i + 1
            if rows[i][j] == 'O':
                rows[i][j] = '.'
                rows[slot][j] = 'O'
                slot += 1

    return rows

lines = open('./day14.in').read().strip().split('\n')

initial_grid = []
for line in lines:
    data = list(map(str, line.strip()))
    initial_grid.append(data)

tilted_grid = move_zeroes(initial_grid)

total_sum = 0
for r, row in enumerate(tilted_grid):
    total_sum += row.count("O") * (len(tilted_grid) - r)

print(total_sum)

