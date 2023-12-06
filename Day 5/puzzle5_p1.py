file_path = './day5.txt'

def parse_seed(line):
    return list(map(int, line.split(':')[1].strip().split()))

# Initialize lists to store seed and map data
seed_data = []
maps_data = []

with open(file_path, 'r') as file:
    seed_data = parse_seed(file.readline())

    for line in file:
        words = line.split()

        if words and words[1].endswith(':'):
            maps_data.append([])
        elif words:
            data = tuple(map(int, words))
            maps_data[-1].append(data)

def searchLoc(seed):
    cur_seed = seed

    for i in maps_data:
        for dest_start, src_start, range_len in i:
            if src_start <= cur_seed < src_start + range_len:
                cur_seed = dest_start + (cur_seed - src_start)
                break

    return cur_seed

loc = [searchLoc(seed) for seed in seed_data]

result = min(loc)
print(result)
