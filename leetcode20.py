#!/usr/bin/python3

from itertools import permutations
class Solution(object):
    def create_hash_map(self,nums, my_permutations_set):
        hash_mapje = {}
        for tuple in my_permutations_set:
            sum = nums[tuple[0]] + nums[tuple[1]]
            if(hash_mapje.get(sum) == None):
                hash_mapje[sum] = [tuple]
            else:
                hash_mapje[sum].append(tuple)
        return hash_mapje

    def remove_duplicates(self, sorted_list):
        new_list = []
        value = None
        my_memory = 0
        for element in sorted_list:
            if(element[1] != value):
                new_list.append(element)
                value = element[1]
                my_memory = 0
            elif(my_memory < 3):
                new_list.append(element)
                my_memory +=1
        return new_list
    


    def fourSum(self, nums, target):
        nums_copy = sorted(enumerate(nums), key = lambda x : x[1])
        nums_copy = self.remove_duplicates(nums_copy)
        my_permutations = permutations((element[0] for element in nums_copy), 2)
        my_permutations_set = set(tuple(sorted(p)) for p in my_permutations)
        mapje = self.create_hash_map(nums, my_permutations_set)
        set_of_sets = set()
        for element in my_permutations_set:
            first, second = element[0], element[1]
            sum_current_element = nums[element[0]] + nums[element[1]]
            required_sum = target - sum_current_element
            if(mapje.get(required_sum) != None): #checken met chat of dit wel snel is
                for map_element in mapje.get(required_sum):
                    first_map = map_element[0]
                    second_map = map_element[1]
                    if(first != first_map and first != second_map and second != first_map and second != second_map):
                        set_of_sets.add(tuple(sorted(nums[index] for index in (element + map_element))))
        return [list(tuple) for tuple in set_of_sets]


def main():
    s = Solution()
    print(s.fourSum([1,0,-1,0,-2,2], 0))


if(__name__=="__main__"):
    main()

