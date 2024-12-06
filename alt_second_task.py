
nums = [2,0,2,1,1,0]

def sortColors(nums):    

    red_c = nums.count(0)
    white_c = nums.count(1)
    blue_c = nums.count(2)

    red = list([0] * red_c)
    white = list([1] * white_c)
    blue = list([2] * blue_c)

    nums.clear()

    nums.extend(red + white + blue)



sortColors(nums)

print(nums)

