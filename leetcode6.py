#!/usr/bin/python3
from  coordinate import Coordinate
class Solution(object):

    def convert(self, string, numRows):
        if(numRows == 1):
            return string
        listOfLinkedElements = self.linkLettersToCoordinates(string, numRows)
        if(listOfLinkedElements == [""]):
            return listOfLinkedElements
        newlistOfLinkedElements = [(letter, (coordinate.getX(), coordinate.getY())) for letter, coordinate in listOfLinkedElements]
        sortedOnXandYcord = sorted(newlistOfLinkedElements, key = lambda x : (x[1][0],x[1][0]))
        answer = ""
        for letter, coordinate in sortedOnXandYcord:
            answer = answer + letter
        return answer

                    



    def nextZigZagCoordinates(self, coordinate: Coordinate, numRows):
        if(coordinate.getY()%(numRows-1) != 0 or coordinate.getX() == numRows - 1):
            return Coordinate(coordinate.getX() - 1, coordinate.getY() + 1 ) 
        else:
            return Coordinate(coordinate.getX() + 1 , coordinate.getY())

        


    def linkLettersToCoordinates(self, string, numRows) -> list[tuple[str, Coordinate]]:
        listOfLinkedElements = []
        if(len(string)<= 0):
            return [""]
        first_letter = string[0]   
        current_intdex = 1
        currentCoordinate = Coordinate(0,0)
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
    result = s.convert("AB", 1)
    print(result)


if(__name__=="__main__"):
    main()