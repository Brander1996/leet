#!/usr/bin/python3

from itertools import permutations
class Solution(object):

    def create_hash_map(self, nums):
        mapje = {}
        for index in range(len(nums)):
            if (mapje.get(nums[index])==None):
                mapje[nums[index]] = index
        return mapje

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
                

    def threeSum(self, nums):
        nums = self.remove_duplicates(sorted(nums))
        mapje = self.create_hash_map(nums)
        three_sum = set()
        for index1 in range(len(nums)):
            for index2 in range(len(nums)):
                if(index1<index2):
                    first_number = nums[index1]
                    second_number = nums[index2]
                    sum_value = first_number + second_number
                    sum_negative_value = -sum_value
                    index3 = mapje.get(sum_negative_value)
                    if (index3 != None):
                        if(not(index1 == index3 or index2 == index3)):                            
                            three_sum.add(tuple(sorted([sum_negative_value, first_number, second_number])))
        return [list(tuple) for tuple in three_sum]


def main():
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))


if(__name__=="__main__"):
    main()

