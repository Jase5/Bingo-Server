import random

class bingogame:
    def __init__(self,gamecode):
          self.gamecode = str(gamecode)
          self.bdict = {}
          self.winner = 0
          self.draws = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]
          random.shuffle(self.draws)
          
class bingoboard:
    def __init__(self,boardcode):
          self.bcode = int(boardcode)
          self.board = generateboard()
          self.drawcount = 0
          
          self.playboard = self.board[:]
          for i,val in enumerate(self.playboard):
              if val < 0:
                  self.playboard[i] = 1000

    def ub(self,ball): #update playboard - aka see if the integer is on the board, if so update playboard to 1000
        if int(ball) in self.board:
            i = self.board.index(int(ball))
            self.playboard[i]=1000
            
    def pboard(self):
        print(self.board)

    def ppboard(self):
        print(self.playboard)


def generateboard():
    board=[]
    b=random.sample(range(1,16),5)
    i=random.sample(range(16,31),5)
    n=random.sample(range(31,46),5)
    n[2]=-1
    g=random.sample(range(46,61),5)
    o=random.sample(range(61,76),5)

    for x in b:
        board.append(x)
    for x in i:
        board.append(x)
    for x in n:
        board.append(x)
    for x in g:
        board.append(x)
    for x in o:
        board.append(x)
    #board = [2,5,8,11,12,17,22,26,24,30,31,33,40,42,38,48,55,56,53,51,62,68,64,69,72]
    return board
    
def wincol(self):
        result = 0
        if self.playboard[0] == 1000 and self.playboard[1] == 1000 and self.playboard[2] == 1000 and self.playboard[3] == 1000 and self.playboard[4] == 1000 :
            result = 1
        elif self.playboard[5] == 1000 and self.playboard[6] == 1000 and self.playboard[7] == 1000 and self.playboard[8] == 1000 and self.playboard[9] == 1000 :
            result = 2
        elif self.playboard[10] == 1000 and self.playboard[11] == 1000 and self.playboard[12] == 1000 and self.playboard[13] == 1000 and self.playboard[14] == 1000 :
            result = 3
        elif self.playboard[15] == 1000 and self.playboard[16] == 1000 and self.playboard[17] == 1000 and self.playboard[18] == 1000 and self.playboard[19] == 1000 :
            result = 4
        elif self.playboard[20] == 1000 and self.playboard[21] == 1000 and self.playboard[22] == 1000 and self.playboard[23] == 1000 and self.playboard[24] == 1000 :
            result = 5           
        return result
        

def winrow(self):
        result = 0
        if self.playboard[0] == 1000 and self.playboard[5] == 1000 and self.playboard[10] == 1000 and self.playboard[15] == 1000 and self.playboard[20] == 1000 :
            result = 1
        elif self.playboard[1] == 1000 and self.playboard[6] == 1000 and self.playboard[11] == 1000 and self.playboard[16] == 1000 and self.playboard[21] == 1000 :
            result = 2
        elif self.playboard[2] == 1000 and self.playboard[7] == 1000 and self.playboard[12] == 1000 and self.playboard[17] == 1000 and self.playboard[22] == 1000 :
            result = 3
        elif self.playboard[3] == 1000 and self.playboard[8] == 1000 and self.playboard[13] == 1000 and self.playboard[18] == 1000 and self.playboard[23] == 1000 :
            result = 4
        elif self.playboard[4] == 1000 and self.playboard[9] == 1000 and self.playboard[14] == 1000 and self.playboard[19] == 1000 and self.playboard[24] == 1000 :
            result = 5           
        return result

def windl(self):
        result = 0
        if self.playboard[0] == 1000 and self.playboard[6] == 1000 and self.playboard[12] == 1000 and self.playboard[18] == 1000 and self.playboard[24] == 1000 :
            result = 1
        return result


def windr(self):
        result = 0
        if self.playboard[4] == 1000 and self.playboard[8] == 1000 and self.playboard[12] == 1000 and self.playboard[16] == 1000 and self.playboard[20] == 1000 :
            result = 1
        return result

    
