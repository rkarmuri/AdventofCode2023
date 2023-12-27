file_path = './day9.in'

# Part 1 extrapolate function that goes forward once
def extrapolate1(nums):
    if all(x==0 for x in nums):
        return 0
    # Zip function will help us find the differnce of pairs in each row
    diff = [y-x for x,y in zip(nums,nums[1:])]
    return nums[-1]+extrapolate1(diff)

# Part extrapolate function to go backwards once
def extrapolate2(nums):
    if all(x==0 for x in nums):
        return 0
    # Zip function will help us find the differnce of pairs in each row
    diff = [y-x for x,y in zip(nums,nums[1:])]
    return nums[0]-extrapolate2(diff)

result1,result2 = 0,0
with open(file_path,'r')as file:
    lines = file.read().strip().split('\n')

    for line in lines:
        nums = list(map(int,line.split()))
        result1 += extrapolate1(nums)
        result2 += extrapolate2(nums)

print(result1)
print(result2)

