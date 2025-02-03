#!/usr/bin/python3

class Solution(object):

    def convert(self, string, numRows):
        pointer = 0
        currentCoordinates = (0,0)
        stringLength = len(string)
        while(pointer < stringLength):
            self.nextZigZagCoordinatites(currentCoordinates, numRows)


    def nextZigZagCoordinatites(self, coordinatines, numRows):
        if(coordinatines[1]//(numRows-1) != 0 or coordinatines[0] == numRows):
            return (coordinatines[0] + 1, coordinatines[1] - 1 ) 
        else:
            return (coordinatines[0], coordinatines[1] + 1)

        


        