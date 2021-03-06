#!/usr/bin/python

import sys
class Board:
    def __init__(self):
        self.grid = None
        self.initGrid()

    def initGrid(self):
        self.grid = [[], [], [], [], [], [], [], [], []]
        ri = 0
        while ri < 9:
            ci = 0
            while ci < 9:
                self.grid[ri].append(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                ci += 1
            ri += 1

    def toString(self):
        string = ""
        ci = 0
        for row in self.grid:
            multi = 0
            while multi < 3:
                ri = 0
                for cell in row:
                    cnt = 1
                    while cnt <= 3:
                        num = str(multi*3 + cnt)
                        if num in cell:
                            string += num
                        else:
                            string += "*"
                        if cnt == 3:
                            string += " | "
                        else:
                            string += " "
                        cnt += 1
                    ri += 1
                    if not ri%3:
                        string += " || "
                string += "\n"
                multi += 1
            string += "\n"
            ci += 1
            if not ci%3:
                string += "-----------------------------------------------------------------------------\n"
        return string

    def __str__(self):
        return self.toString()

    def __repr__(self):
        return self.toString()

    def setValue(self, ri, ci, value):
        self.grid[ri][ci] = [value];
    
    def readBoardFromFile(self, filename):
        try:
            fileObj = open(filename, 'r')
        except IOError:
            print "cannot open file " + filename
            return
        ri = 0
        ci = 0
        line = fileObj.readline().strip()
        while line:
            if char == '\n':
                ri += 1
                ci = 0
            else:
                char = char.strip()
                if char:
                    if char != '*':
                        print str(char) + " " + str(ri) + " " + str(ci) 
                        self.grid[ri][ci] = [char]
                    ci += 1
            char = fileObj.read(1)
                
if __name__ == "__main__":                
    board = Board()
    print board
    board.readBoardFromFile(sys.argv[1])
        
    
                    

        

