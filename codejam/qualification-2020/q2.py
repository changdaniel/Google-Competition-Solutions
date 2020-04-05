from sys import stdin
T = int(input())
strings = [[int(i) for i in line] for line in stdin.read().splitlines()]

def add_parens(nums):
    string = ""
    left = 0
    for num in nums:
        if num <= left:
            left -= num
            string += ")" * left + str(num)
            left = num
            
        else:
            string += "(" * (num - left) + str(num)
            left = num

    string += ")" * left
        
    return string


for i, nums in enumerate(strings,1):

    print("Case #{}: {}".format(i, add_parens(nums)))
    