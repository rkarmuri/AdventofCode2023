file_path = './day6.txt'

with open(file_path, 'r') as file:
    lines = file.read().strip().split("\n")
    time = list(map(int, lines[0].split(':')[1].strip().split()))
    distance = list(map(int, lines[1].split(':')[1].strip().split()))

total_ways = []

for i in range(len(time)):
    count = 0
    for j in range(time[i], -1, -1):
        pos_dis = j * (time[i] - j)
        if pos_dis > distance[i]:
            count += 1

    total_ways.append(count)

result = 1
for i in total_ways:
    result *= i

print(result)
