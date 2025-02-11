#!/usr/bin/python3
class Solution(object):

    def maxArea(self, height: List[int]) -> int:
         left_index = 0
         right_index = len(height)
         max_area = 0
         while():
            current_area = self.computeArea(left_index, right_index, height)
            if(current_area > max_area):
                max_area = current_area                 

              
    def compareHeights(self,left, right, heigth):
        if(heigth[left] > heigth[right]):
             return left
        return right
    
    def computeArea(self, left, right, height):
         return (right-left) * min(height[left], height[right]) 
      

            
def main():
        s = Solution()
        result = s.convert("ABCDE", 3)
        print(result)


if(__name__=="__main__"):
    main()