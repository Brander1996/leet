#!/usr/bin/python3
class Solution(object):

    def convert(self, string, numRows):
        if(numRows == 1):
            return string
        listOfLinkedElements = self.linkLettersToCoordinates(string, numRows)
        if(listOfLinkedElements == [""]):
            return listOfLinkedElements
        sortedOnXandYcord = sorted(listOfLinkedElements, key = lambda x : (x[1][0],x[1][0]))
        answer = ""
        for letter, coordinate in sortedOnXandYcord:
            answer = answer + letter
        return answer

                    



    def nextZigZagCoordinates(self, coordinate, numRows):
        if(coordinate[1]%(numRows-1) != 0 or coordinate[0] == numRows - 1):
            return (coordinate[0] - 1, coordinate[1] + 1 ) 
        else:
            return (coordinate[0] + 1 , coordinate[1])

        


    def linkLettersToCoordinates(self, string, numRows) -> list[tuple[str, tuple]]:
        listOfLinkedElements = []
        if(len(string)<= 0):
            return [""]
        first_letter = string[0]   
        current_intdex = 1
        currentCoordinate = (0,0)
        listOfLinkedElements.append((string[0],currentCoordinate))
        stringLength = len(string)
        while(current_intdex < stringLength):
            nextCoordinate = self.nextZigZagCoordinates(currentCoordinate, numRows)
            listOfLinkedElements.append((string[current_intdex],nextCoordinate))
            current_intdex = current_intdex + 1
            currentCoordinate = nextCoordinate
        return listOfLinkedElements


        
def main():
    s = Solution()
    result = s.convert("ABCDE", 3)
    print(result)


if(__name__=="__main__"):
    main()