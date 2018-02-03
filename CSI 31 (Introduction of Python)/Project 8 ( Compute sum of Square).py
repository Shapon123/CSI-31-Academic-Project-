# CSI 31 Sabina.Akter sumlist.py
# This program computes the sum of the squares in a list.

def sumList(lists):
    sList = 0
    for i in lists:
        sList = i + sList
    return sList
    

def toNumbers(nums):
    new_nums = []
    for l in nums:
        new_nums.append(int(l))
    return new_nums

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    return nums

def main():
    print("This program computes the sum of the squares in a list:  ")  
    numbers = input("Please enter the file name that contains the numbers: ")
    infile = open(numbers,'r')
    nums = []
    for line in infile:
        nums.append(line)
        print(nums)
        nums = toNumbers(nums)
    print(nums)
    sqnums = squareEach(nums)
    sum = sumList(sqnums)
    print(sum)
  
main()
"""
This program computes the sum of the squares in a list:  
Please enter the file name that contains the numbers: r.txt
['1\n']
[1, '2\n']
[1, 2, '3\n']
[1, 2, 3, '4']
[1, 2, 3, 4]
30
"""



    
    
    
     

    
