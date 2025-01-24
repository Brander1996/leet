#!/usr/bin/python3

def f(array, index ,target, nsum, memoization = {}):
    if (nsum == 1):
        if (array[index] == target):
            return [index]
        elif(index>len(array)):
            return None
        else:
            return f(array, index + 1, nsum, memoization)
    rec_index = index +1
    local_list = []
    while rec_index < len(array):
        local_list.append(f(array, rec_index, target - array[index], nsum -1))
        rec_index = rec_index + 1
    
    
    if (not (target, nsum) in memoization):
        recursive_call  = f(array, index + 1, target-array[index], nsum - 1, memoization)
        if 
        memoization[(target, nsum)] = list(map(lambda x: if(not x == None): x.append(index),f(array, index + 1, target-array[index], nsum - 1, memoization)))
    else :
        return memoization[(target, nsum)]






def main():
    array = [1,8,6,2,5,4,8,3,7]
    print(container_with_most_water(array))

if (__name__=="__main__"):
    main()

