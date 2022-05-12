'''
Given an array of integers, return a new array such that each element at index
 i of the new array is the product of all the numbers in the original array
  except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
 [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
  would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

import math

#First brute force solution would be to loop through the list twice
#but the follow-up gives away a more elegatn solution.

#get the total product, and then divide the product by each number
#should be O(n)

def div_product(nums : []):
    product = math.prod(nums)
    out = []
    for num in nums:
        out.append(product/num)
    return out

#if we cannot use division we have to reconize that the product
#the answer is looking for is x_l * x_r, where x_l is the
#product of all the numbers to the left and x_r is the product
#of all the numbers on the right

def mul_leftright(nums : []):
    out = []
    mulleft = {}
    mulright = {}
    #set the limits
    mulleft[-1] = 1
    mulright[len(nums)] = 1
    #we can populate both dicts at the same time
    j = len(nums) - 1
    for i in range(len(nums)):
        left = nums[i] * mulleft[i-1]
        right = nums[j] * mulright[j+1]
        mulleft[i] = left
        mulright[j] = right
        j -= 1
    #use dict to generate out list
    for i in range(len(nums)):
        out.append(mulleft[i-1]*mulright[i+1])
    return out

if __name__ == "__main__":
    test = [1, 2, 3, 4, 5]
    solution1 = div_product(test)
    print(solution1)
    solution2 = mul_leftright(test)
    print(solution2)
