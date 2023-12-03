file_path = './day2.txt'

with open(file_path, 'r') as file:
    valid_game_ids = []
    powers = []

    for line in file:
        if ":" in line:
            game_info = line.split(':')

            game_num = game_info[0].strip()
            game_details = game_info[1].split(';')

            max_red, max_green, max_blue = 0, 0, 0
            condition_satisfied = True

            for round_num in game_details:
                round_info = round_num.split(',')

                for item in round_info:
                    count, color = item.strip().split(' ')
                    count = int(count)

                    if color == 'red':
                        max_red = max(max_red, count)
                    elif color == 'green':
                        max_green = max(max_green, count)
                    elif color == 'blue':
                        max_blue = max(max_blue, count)

            if (max_red > 12) or (max_green > 13) or (max_blue > 14):
                condition_satisfied = False

            if condition_satisfied:
                nums = [char for char in game_num if char.isdigit()]
                if len(nums) == 3:
                    valid_game_ids.append(int(nums[0] + nums[1] + nums[2]))
                elif len(nums) == 2:
                    valid_game_ids.append(int(nums[0] + nums[1]))
                else:
                    valid_game_ids.append(int(nums[0]))

            cubes_power = max_red * max_green * max_blue
            powers.append(cubes_power)

result1 = sum(valid_game_ids)
result2 = sum(powers)
print('part1 result is: ', result1)
print('part2 result is: ', result2)
