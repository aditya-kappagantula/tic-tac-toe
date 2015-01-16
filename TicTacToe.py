def isNumber(aValue):
        try:
                value = int(aValue)
                return True
        except ValueError:
                print("That's not an integer!")
                return False

def startGame():
        print ("Welcome To Tic-Tac-Toe!")
        print ("=======================")
        print ("Enter number of rows on board:")
        rows = input()
        while isNumber(rows) is False or int(rows) < 3:
                print ("Enter number of rows on board (Min 3):")
                rows = input()
        columns = int(rows)
        for eachBlock in range(0, int(rows)*int(columns)):                
                blocks.append("-")
        printBoard(int(rows),int(columns),blocks)
        startMoves(int(rows),int(columns),blocks)

def printBoard(rows,columns,blocks):
        print("Here is the board.")
        print("==================")
        for i in range(0,rows):
                for j in range(0,columns):
                        if(j<rows-1):
                                print(blocks[i*rows+j], end="|")
                        else:
                                print(blocks[i*rows+j], end="")
                        if(j==rows-1 and i < rows-1):
                                print()
                                for k in range(0,2*rows-1):
                                        print("-", end="")
                print()

def isError(blockNumber, blocks, rows, columns):        
        if int(blockNumber) > int(rows)*int(columns):
                print("Invalid block number. Valid range 1 -",rows*columns,".")
                return True
        elif blocks[int(blockNumber)-1] == 'O':
                print("This block is already occupied by computer.")
                return True
        elif blocks[int(blockNumber)-1] == 'X':
                print("This block is already occupied by you.")
                return True
        else :
                return False

def winCheck(parentString,rows,columns,blocks):
        import sys
        playerWin = "XXX"
        computerWin = "OOO"        
        if parentString.find(playerWin) >= 0:
                print("Game Over! You have won")
                printBoard(rows,columns,blocks)
                sys.exit(0)
        if parentString.find(computerWin) >= 0:                
                print("Game Over! You lost!")
                printBoard(rows,columns,blocks)
                sys.exit(0)
def isWin(rows, columns, blocks):        
        convertToMatrix = lambda blocks, size: [blocks[i:i+size] for i in range(0,len(blocks), size)]
        matrixBlock = convertToMatrix(blocks,rows)
        diagonal = [ row[i] for i,row in enumerate(matrixBlock) ]        
        diagonal = ''.join(diagonal)
        winCheck(diagonal,rows,columns,blocks)        
        reverseDiagonal = [ row[-i-1] for i,row in enumerate(matrixBlock) ]
        reverseDiagonal = ''.join(reverseDiagonal)
        winCheck(reverseDiagonal,rows,columns,blocks)  
        for count in range(0,rows):
                eachColumn = [sublist[count] for sublist in matrixBlock]
                eachColumn = ''.join(eachColumn)
                winCheck(eachColumn,rows,columns,blocks)
        for sublist in matrixBlock:
                eachRow = ''.join(sublist)
                winCheck(eachRow,rows,columns,blocks)        
        return False

def generateComputerMove(rows, columns, blocks):
        import random,sys        
        if ''.join(blocks).find('-') == -1:
                print("Game Over! It is a draw")
                printBoard(rows,columns,blocks)                
                sys.exit()
        selectedPosition = random.choice([index for index, value in enumerate(blocks) if value == "-"])
        return(selectedPosition)

def startMoves(rows, columns, blocks):
        while isWin(rows, columns, blocks) is False:
                while "-" in blocks:
                        print("Please enter a block number to mark it.")
                        blockNumber = input()
                        while isError(blockNumber, blocks,rows,columns) is True:
                                print ("Please enter a block number to mark it.")
                                blockNumber = input()
                        blocks[int(blockNumber)-1] = 'X'
                        isWin(rows,columns,blocks)
                        blocks[generateComputerMove(rows,columns,blocks)] = 'O'
                        isWin(rows,columns,blocks)
                        printBoard(rows, columns, blocks)

if __name__ == "__main__":        
        blocks = []
        rows = 0
        columns = 0
        startGame()
