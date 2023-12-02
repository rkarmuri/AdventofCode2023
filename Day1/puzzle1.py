file_path = './day1.txt'
with open(file_path,'r') as file:
    lines = []
    for line in file:
        lines.append(line.strip())

# Part 1
calibration_values1 = []
output1 = 0

for i in lines:
    nums1 = [char for char in i if char.isdigit()]
    if len(nums1) == 1:
        calibration_values1.append(int(nums1[0] * 2))
    else:
        calibration_values1.append(int(nums1[0] + nums1[-1]))

output1 = sum(calibration_values1)

print(output1)

# Part 2
calibration_values2 = []
output2 = 0
num_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

for line in lines:
    nums2 = []
    for index, character in enumerate(line):
        if character.isdigit():
            nums2.append(character)
        else:
            for end_point in range(4, 1, -1):
                if index < len(line) - end_point:
                    substr = line[index:index + end_point + 1]
                    if substr in num_mapping:
                        nums2.append(num_mapping[substr])
    if len(nums2) == 1:
        calibration_values2.append(int(nums2[0] * 2))
    else:
        calibration_values2.append(int(nums2[0] + nums2[-1]))

output2 = sum(calibration_values2)

print(output2)

