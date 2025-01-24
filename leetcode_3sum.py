#!/usr/bin/python3
from itertools import permutations
class Solution(object):

    def create_hash_map(self, nums):
        mapje = {}
        for index1 in range(len(nums)):
            for index2 in range(len(nums)):
                if(index1 != index2):
                    first_number = nums[index1]
                    second_number = nums[index2]
                    mapje[nums[first_number]+nums[second_number]] = (index1,index2)

    def remove_duplicates(self, sorted_list):
        new_list = []
        value = None
        my_memory = 0
        for element in sorted_list:
            if(element != value):
                new_list.append(element)
                value = element
                my_memory = 0
            elif(my_memory < 2):
                new_list.append(element)
                my_memory +=1
        return new_list
                

    def threeSum(self, nums, target):
        mapje = self.create_hash_map(nums)
        nums = sorted(self.remove_duplicates(nums))
        three_sum = set()
        for number in nums:
            if(mapje.get(target - number)!= None):
                three_sum.add(tuple(sorted([number, mapje[number][0], mapje[number][1]])))
        return [list(tuple) for tuple in three_sum]



            




        

def main():
    s = Solution()
    print(s.fourSum([1,0,-1,0,-2,2], 0))


if(__name__=="__main__"):
    main()

