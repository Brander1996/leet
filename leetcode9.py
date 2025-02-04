 #!/usr/bin/python3

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        length_input = len(x)
        middle = length_input//2
        odd = length_input%2==1
        pointer = 0
        stack = []
        for i in range(length_input):
            if(pointer < middle):
                stack.append(x[pointer])
                pointer = pointer + 1
            elif(odd and pointer == middle):
                pointer = pointer + 1
            else:
                if(stack.pop() != x[pointer]):
                    return False
                pointer = pointer + 1
        return True
                
                


        
def main():
    s = Solution()
    result = s.isPalindrome(-1)
    print(result)


if(__name__=="__main__"):
    main()