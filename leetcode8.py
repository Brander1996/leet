#!/usr/bin/python3

class Solution(object):

    def removeWhiteSpace(self, input_string):
        pointer = 0 
        while(pointer<len(input_string)):
            if(input_string[pointer] != " "):
                return input_string[pointer:]  
            pointer = pointer + 1
        return ""

    
    def isNegative(self, input_string):
        if(len(input_string)==0):
            return False
        if(input_string[0] =="-"):
            return True
        else:
            return False
    
    def removeSign(self, input_string):
        if(len(input_string)==0):
            return ""
        if(input_string[0] =="-" or input_string[0] == "+"):
            return input_string[1:]
        else: 
            return input_string
    
    def skipZeros(self, input_string):
        pointer = 0
        while(pointer<len(input_string)):
            if(input_string[pointer] != "0"):
                return input_string[pointer:]
            pointer = pointer + 1
        return ""
    
  
    def provideLeadingDigits(self, input_string):
        if(len(input_string)==0):
            return ""
        else:
            pointer = 0
            while(pointer<len(input_string)):
                if(not input_string[pointer].isdigit()):
                    return input_string[:pointer]
                pointer = pointer + 1
            return input_string
    
    def roundNumber(self, number):
        negative_boundry = -(2**31)
        positive_boundry =2**31 - 1
        if(number <= negative_boundry):
            return negative_boundry
        if (number >= positive_boundry):
            return positive_boundry
        return number
    
    def myAtoi(self, input_string):
        without_whitespace = self.removeWhiteSpace(input_string)
        is_negative =self.isNegative(without_whitespace)
        without_sign = self.removeSign(without_whitespace)
        without_zeros = self.skipZeros(without_sign)
        digits= self.provideLeadingDigits(without_zeros)
        if(digits == ""):
            return 0
        number = int(digits)
        if(is_negative):
            number = -number
        return self.roundNumber(number)


def main():
    s = Solution()
    print(s.myAtoi("10"))


if(__name__=="__main__"):
    main()

