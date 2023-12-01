total = 0
with open('01/input.txt') as f:
  for line in f:
    nums = [n for n in line if n.isnumeric()]
    nums = ''.join([nums[i] for i in (0, -1)])
    total += int(nums)
print(total)