import socket
import random
import bingo

gamedict = {}

def newgame():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    gamecodelist = random.sample(alpha,4)
    gengamecode = gamecodelist[0]+gamecodelist[1]+gamecodelist[2]+gamecodelist[3]

    while gengamecode in gamedict:
            gamecodelist = random.sample(alpha,4)
            gengamecode = gamecodelist[0]+gamecodelist[1]+gamecodelist[2]+gamecodelist[3]

    g = bingo.bingogame(gengamecode)
    gamedict[gengamecode]=g
    
    #EXAMPLE DATA WILL BE RETURNED
    #gengamecode = "EMAG"
    return gengamecode

def gamestat(gc):
    genstats = str(gc)
    genstats += ',' 
    gwinner = 'E'
    if gc in gamedict:
        game = gamedict[gc]      
        if game.winner:
            gwinner = 'W'
        else:
            gwinner = 'X'
           
        for b in game.bdict:
            
            genstats += str(game.bdict[b].bcode)
            genstats += ','
            genstats += str(game.bdict[b].drawcount)
            genstats += ','            
    
    #EXAMPLE DATA WILL BE RETURNED
    #genstats = gc+",987,20,968,10,X"
    genstats += gwinner
    return genstats


def genboard(gc):

    boardcode = random.randint(100,999)
    if gc in gamedict:
        game = gamedict[gc]
        while boardcode in game.bdict:
            boardcode = random.randint(100,999)
    b1 = bingo.bingoboard(boardcode)
    game.bdict[boardcode]=b1  #Add the newly created board to the board dictionary, bdict, inside the game
    
    #EXAMPLE DATA WILL BE RETURNED
    #board = [987,2,5,8,11,12,17,22,26,24,30,31,33,40,42,38,48,55,56,53,51,62,68,64,69,72]
    boardstr = ''
    boardstr +=str(boardcode)+','
    for n in b1.board:
        boardstr +=str(n)+','
    boardstr = boardstr[:-1] #eliminates the last comma that was added by the loop
    return boardstr



def genball(gc,bd):
    ball = -100
    gwinner = 'E'
    if gc in gamedict:
        game = gamedict[gc]
        if game.winner:
            gwinner = 'W'
        else:
            gwinner = 'X'
        if int(bd) in game.bdict:
            board = game.bdict[int(bd)]
            ball = game.draws[board.drawcount]
            board.drawcount += 1
            
    #EXAMPLE DATA WILL BE RETURNED
    #ball = random.randint(1,75)
    ballstr = str(ball)+","+gwinner
    
    return ballstr


def boardquit(gc,bd):
    if gc in gamedict:
        game = gamedict[gc]
        if int(bd) in game.bdict:
            print("BOARD "+str(gc)+":"+str(bd)+" QUIT")
            game.bdict.pop(int(bd))
        if len(game.bdict) == 0:
            print("GAME "+str(gc)+" ENDED")
            gamedict.pop(gc)
    
    
    quitstr = str(gc)+","+str(bd)+",BYE"
    #REMOVE BOARD FROM PLAY
    #CHECK TO SEE IF OTHER BOARDS STILL PLAY, IF NOT - REMOVE GAME
    return quitstr



def windec(gc,bd,bingotype):
    if gc in gamedict:
        game = gamedict[gc]
        game.winner = 1

    winstr = str(gc)+","+str(bd)+",OK"
    return winstr


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 48488  # initiate port no above 1024

    print("BINGO SERVER STARTING: "+str(host)+":"+str(port))

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(20)

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        command = data.split('#')
        
        print("RECEIVED: " + str(data))

        if 'NG' in command[0]:
            data = newgame()
            print("Sending:",data)
            conn.send(data.encode())  # send reply to the client
        elif 'GS' in command[0]:
            gc = command[1]
            data = gamestat(gc)
            print("Sending:",data)
            conn.send(data.encode())  # send reply to the client
        elif 'GB' in command[0]:
            gc = command[1]
            data = genboard(gc)
            print("Sending:",data)
            conn.send(data.encode())  # send reply to the client
        elif 'NB' in command[0]:
            gc = command[1]
            bd = command[2]
            data = genball(gc,bd)
            print("Sending:",data)
            conn.send(data.encode())  # send reply to the client
        elif 'QG' in command[0]:
            gc = command[1]
            bd = command[2]
            data = boardquit(gc,bd)
            print("Sending:",data)
            conn.send(data.encode())  # send reply to the client
        elif 'WW' in command[0]:
            gc = command[1]
            bd = command[2]
            bingotype = command[3]
            data = windec(gc,bd,bingotype)
            print("Sending:",data)
            conn.send(data.encode())  # send reply to the client  
        conn.close()  # close the connection
    


if __name__ == '__main__':
    server_program()
