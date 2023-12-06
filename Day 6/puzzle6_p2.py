file_path = './day6.txt'

with open(file_path, 'r') as file:
    lines = file.read().strip().split("\n")
    time = list(map(str, lines[0].split(':')[1].strip().split()))
    distance = list(map(str, lines[1].split(':')[1].strip().split()))

    total_time,total_distance = '',''
    for i in range(len(time)):
        total_time += time[i]
        total_distance += distance[i]

    total_time,total_distance = int(total_time),int(total_distance)

    total_ways = 0
    for i in range(total_time,-1,-1):
        pos_dis = i * (total_time - i)
        if pos_dis > total_distance:
            total_ways += 1

print(total_ways)