
# alg=input("ALGO 1-min max or  2 - alpha beeta")
# fst=input("first who specify the game X or O")
print("ALGO 1-min max or  2 - alpha beeta")
print("first who specify the game X or O")
print("1 Mode : human (X) versus computer (O)")
print("2 Mode : computer (X) versus computer (O)")
# mde=input("1 or 2")
print("Babu, Raghunath, A20511598 solutions:")
inp_str=input("enter")
inp_str=inp_str.split(' ')
if(len(inp_str)>3):
    print("too many")
    exit()
if(len(inp_str)<3):
    print("not enough")
    exit()    
alg=inp_str[0]
fst=inp_str[1]
mde=inp_str[2]
pinp=['1','2']
pinp1=['X','O']
if(alg not in pinp):
    print("illegal  inputs arguements")
    exit()
if(mde not in pinp):
    print("illegal  inputs arguements")
    exit()

if(alg=='1'):
    print("Algorithm : MiniMax")
else:
    print("Algorithm : MiniMax with alpha-beta pruning")

print("FIRST ;",fst)

if(mde=='1'):
    print("Mode : human (X) versus computer (O)")
else:
    print("Mode : computer (X) versus computer (O)")
    
# from try_alpha import min_max_alpha  
    
if(alg=='1' and mde=='1'):
    # printing the board. the tic tax board is considered as a dictionary with 1 to 9 as keys and values with either X or X or space
    def printTic(t_board):
        print(t_board[1],'  |',t_board[2], "  |",t_board[3])
        print('---',"+","---","+","---")
        print(t_board[4],'  |',t_board[5], "  |",t_board[6])
        print('---',"+","---","+","---")
        print(t_board[7],'  |',t_board[8], "  |",t_board[9])
    
    # Checking available positions
    def available_pos(t_board):
        avai_array=[]
        for i in t_board:
            if(t_board[i]==' '):
                avai_array.append(i)
        print("the available positions are" ,avai_array)
        
    
    def Win_Check(criteria,a):
        a=int(a)
        #all possible strikes
        if(t_board[1]==t_board[2] and t_board[2]==t_board[3] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
       
        elif(t_board[4]==t_board[5] and t_board[5]==t_board[6] and (t_board[4]!=criteria if(a==0) else t_board[4]==criteria)):
            return True

        elif(t_board[7]==t_board[8] and t_board[8]==t_board[9] and (t_board[8]!=criteria if(a==0) else t_board[7]==criteria)):
            return True
        
        elif (t_board[1] == t_board[4] and t_board[1] == t_board[7] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
        
        elif (t_board[2] == t_board[5] and t_board[2] == t_board[8] and (t_board[2]!=criteria if(a==0) else t_board[2]==criteria)):
            return True
        
        elif (t_board[3] == t_board[6] and t_board[3] == t_board[9] and (t_board[3]!=criteria if(a==0) else t_board[3]==criteria)):
            return True
        
        elif (t_board[1] == t_board[5] and t_board[1] == t_board[9] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
        
        elif (t_board[7] == t_board[5] and t_board[7] == t_board[3] and (t_board[7]!=criteria if(a==0) else t_board[7]==criteria)):
            return True
        
        else:
            return False
    # player (human turn)
    def humanTurn():
        available_pos(t_board)
        pos_human=input("enter the position of X or 0 to exit")
        pos_human=int(pos_human)
        print(t_board)
        #entering 0 exit the game
        if(pos_human==0):
            return False
        
        #inserting letter X into the tic tac game 
        # checking for empty space
        if(t_board[pos_human]==" "):
            t_board[pos_human]='X'
            printTic(t_board)
            #checking if the inserted letter X leads to win or tie
            if(Win_Check(' ',0)==True):
                print("X won ")
                exit()
          
            if(' ' not in t_board.values()):
                print("Tie")
                exit()

        return True
    # min max implementation
    def minmax(t_board, d, condition):
        global depth_min,depth_max,count
        #if O win it the score is 1
        if(Win_Check('O',1)==True):
           
            return 1
        # if X win the score os -1
        elif(Win_Check("X",1)==True):
           
            return -1
        # if match tie the score is 0
        elif(' ' not in t_board.values()):
           
            return 0
        
        if(condition==True):
            # - infinity
            optimum_score=-1000
            # trying all possible moves for O 
            for i in t_board.keys():
                if(t_board[i]==' '):
                    t_board[i]='O'
                    #this will lead to minimize
                    lp_condition=False
                    count=count+1
                    # calling min max recursively
                    s=minmax(t_board,d+1,lp_condition)
                    t_board[i]=' '
                    # checking scores for all moves and choosing the max
                    if(s>optimum_score):
                        optimum_score=s
                        depth_max=d
            return optimum_score
        else:
            # for X search auto,minimizing
            # + infinity
            optimum_score=1000
            for i in t_board.keys():
                if(t_board[i]==' '):
                    t_board[i]= 'X'
                    # this will lead to maximize
                    lp_condition=True
                    count=count+1
                    # calling min max recursively
                    s=minmax(t_board,d+1,lp_condition)
                    t_board[i]=' '
                    # checking scores for all moves and choosing the minimum
                    if(s<optimum_score):
                        optimum_score=s
                        depth_min=d
            return optimum_score
        
    # Computer turn
    def compTurn():
        global depth_min,depth_max,count
        # - infinity
        optimum_score = -1000
        dict_comp={}  
        
        # taking every single possiblities and find the best score.
        for i in t_board.keys():
            if(t_board[i]==' '):
                t_board[i]='O'
                
                s=minmax(t_board,0,False)
                t_board[i]=' '
                if(s>optimum_score):
                    
                    optimum_score=s
                    dict_comp[i]=optimum_score
                    print(depth_min)
        #choosing the position for the maximum score
        if(t_board[max(dict_comp.keys())]==" "):
            t_board[max(dict_comp.keys())]='O'
            printTic(t_board)
            print(count)
            count=0
            # checking if O won the game or the game is tie
            if(Win_Check(' ',0)==True):
                print("O won")
                exit()
            
            if(' ' not in t_board.values()):
                print("Tie")
                exit()
                

        return 
  
    depth_min=0
    depth_max=0     
    count=0
    t_board={}
    c=1
    for i in range(1,10):
        if(i not in t_board.keys()):
            t_board[i]=' '

    printTic(t_board)
    human='X'
    comp='O'
    exit_0=True

    while(not Win_Check(' ',0)):
        if(fst=='X'):
            exit_0=humanTurn()
            
            
            compTurn()
            
        else:
            compTurn()
            exit_0=humanTurn()
            
        if(exit_0==False):
            break
    
if(alg=='1' and mde=='2'):
    # printing the board. the tic tax board is considered as a dictionary with 1 to 9 as keys and values with either X or X or space
    def printTic(t_board):
        print(t_board[1],'  |',t_board[2], "  |",t_board[3])
        print('---',"+","---","+","---")
        print(t_board[4],'  |',t_board[5], "  |",t_board[6])
        print('---',"+","---","+","---")
        print(t_board[7],'  |',t_board[8], "  |",t_board[9])
        
    
    def Win_Check(criteria,a):
        a=int(a)
        #all possible strikes
        if(t_board[1]==t_board[2] and t_board[2]==t_board[3] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
       
        elif(t_board[4]==t_board[5] and t_board[5]==t_board[6] and (t_board[4]!=criteria if(a==0) else t_board[4]==criteria)):
            return True

        elif(t_board[7]==t_board[8] and t_board[8]==t_board[9] and (t_board[8]!=criteria if(a==0) else t_board[7]==criteria)):
            return True
        
        elif (t_board[1] == t_board[4] and t_board[1] == t_board[7] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
        
        elif (t_board[2] == t_board[5] and t_board[2] == t_board[8] and (t_board[2]!=criteria if(a==0) else t_board[2]==criteria)):
            return True
        
        elif (t_board[3] == t_board[6] and t_board[3] == t_board[9] and (t_board[3]!=criteria if(a==0) else t_board[3]==criteria)):
            return True
        
        elif (t_board[1] == t_board[5] and t_board[1] == t_board[9] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
        
        elif (t_board[7] == t_board[5] and t_board[7] == t_board[3] and (t_board[7]!=criteria if(a==0) else t_board[7]==criteria)):
            return True
        
        else:
            return False
    # player (human turn)
    def humanTurn():
        global depth_min,depth_max
        global count
        # + infinity
        optimum_score = 1000
        dict_human={}
        # taking every single possiblities and find the best score.
        for i in t_board.keys():
            if(t_board[i]==' '):
                t_board[i]='X'
                # will lead to maximize thus true
               
                s=minmax(t_board,0,True)
                t_board[i]=' '
                if(s<optimum_score):
                    optimum_score=s
                    dict_human[i]=optimum_score
                    df_nw=depth_max
                    print(depth_max)
        #choosing the position for the minimum score
        if(t_board[max(dict_human.keys())]==" "):
            t_board[max(dict_human.keys())]='X'
            printTic(t_board)
            print(count)
            count=0
            
            if(Win_Check(' ',0)==True):
                print("Comp X won")
                exit()
            
            if(' ' not in t_board.values()):
                print("Draw")
                exit()
                
            # if(Win_Check(' ',0)==True):
            #     print("Computer won")
            #     exit()
        return 
    # min max implementation
    def minmax(t_board, d, condition):
        global depth_min,depth_max
        global count
        #if O win it the score is 1
        if(Win_Check('O',1)==True):
          
            return 1
        # if X win the score os -1
        elif(Win_Check("X",1)==True):
       
            return -1
        # if match tie the score is 0
        elif(' ' not in t_board.values()):
          
            return 0
        
        if(condition==True):
            # - infinity
            optimum_score=-1000
            # trying all possible moves for O 
            for i in t_board.keys():
                if(t_board[i]==' '):
                    t_board[i]='O'
                    #this will lead to minimize
                    lp_condition=False
                    count=count+1
                    # calling min max recursively
                    s=minmax(t_board,d+1,lp_condition)
                    t_board[i]=' '
                    # checking scores for all moves and choosing the max
                    if(s>optimum_score):
                        optimum_score=s
                        depth_max=d
            
            return optimum_score
        else:
            # for X search auto,minimizing
            # + infinity
            optimum_score=1000
            
            for i in t_board.keys():
                if(t_board[i]==' '):
                    t_board[i]= 'X'
                    # this will lead to maximize
                    lp_condition=True
                    count=count+1
                    # calling min max recursively
                    s=minmax(t_board,d+1,lp_condition)
                    t_board[i]=' '
                    # checking scores for all moves and choosing the minimum
                    if(s<optimum_score):
                        optimum_score=s
                        depth_min=d
                       

            return optimum_score
        
    # Computer turn
    def compTurn():
        global depth_min,depth_max,count
        # - infinity
        optimum_score = -1000
        dict_comp={}  
        # taking every single possiblities and find the best score.
        for i in t_board.keys():
            if(t_board[i]==' '):
                t_board[i]='O'
              
                s=minmax(t_board,0,False)
                t_board[i]=' '
                if(s>optimum_score):
                    optimum_score=s
                    dict_comp[i]=optimum_score
                    print(depth_min)

        #choosing the position for the minimum score
        if(t_board[max(dict_comp.keys())]==" "):
            t_board[max(dict_comp.keys())]='O'
            printTic(t_board)
            print(count)
            count=0
            # checking if O won the game or the game is tie
            if(Win_Check(' ',0)==True):
                print("Computer won")
                exit()
            
            if(' ' not in t_board.values()):
                print("Draw")
                exit()
                
            # if(Win_Check(' ',0)==True):
            #     print("Computer won")
            #     exit()
        return 
    
    depth_min=0
    depth_max=0 
    count=0
    t_board={}
    c=1
    for i in range(1,10):
        if(i not in t_board.keys()):
            t_board[i]=' '

    printTic(t_board)
    human='X'
    comp='O'
    exit_0=True

    while(not Win_Check(' ',0)):
        if(fst=='X'):
            exit_0=humanTurn()
            
            
            compTurn()
            
        else:
            compTurn()
            exit_0=humanTurn()
            
        if(exit_0==False):
            break
    
if(alg=='2' and mde=='2'):
    # printing the board. the tic tax board is considered as a dictionary with 1 to 9 as keys and values with either X or X or space
    def printTic(t_board):
        print(t_board[1],'  |',t_board[2], "  |",t_board[3])
        print('---',"+","---","+","---")
        print(t_board[4],'  |',t_board[5], "  |",t_board[6])
        print('---',"+","---","+","---")
        print(t_board[7],'  |',t_board[8], "  |",t_board[9])
    
    # Checking available positions
    def available_pos(t_board):
        avai_array=[]
        for i in t_board:
            if(t_board[i]==' '):
                avai_array.append(i)
        print("the available positions are" ,avai_array)
        
    
    def Win_Check(criteria,a):
        a=int(a)
        #all possible strikes
        if(t_board[1]==t_board[2] and t_board[2]==t_board[3] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
       
        elif(t_board[4]==t_board[5] and t_board[5]==t_board[6] and (t_board[4]!=criteria if(a==0) else t_board[4]==criteria)):
            return True

        elif(t_board[7]==t_board[8] and t_board[8]==t_board[9] and (t_board[8]!=criteria if(a==0) else t_board[7]==criteria)):
            return True
        
        elif (t_board[1] == t_board[4] and t_board[1] == t_board[7] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
        
        elif (t_board[2] == t_board[5] and t_board[2] == t_board[8] and (t_board[2]!=criteria if(a==0) else t_board[2]==criteria)):
            return True
        
        elif (t_board[3] == t_board[6] and t_board[3] == t_board[9] and (t_board[3]!=criteria if(a==0) else t_board[3]==criteria)):
            return True
        
        elif (t_board[1] == t_board[5] and t_board[1] == t_board[9] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
        
        elif (t_board[7] == t_board[5] and t_board[7] == t_board[3] and (t_board[7]!=criteria if(a==0) else t_board[7]==criteria)):
            return True
        
        else:
            return False
    # player (human turn)
    def humanTurn():
        

        
        global depth_min,depth_max,count
        # + infinity
        optimum_score = 1000
        dict_human={}
        # taking every single possiblities and find the best score.
        for i in t_board.keys():
            if(t_board[i]==' '):
                t_board[i]='X'
                # will lead to maximize thus true
              
                s=minmax(t_board,0,True,-1000,1000)
                t_board[i]=' '
                if(s<optimum_score):
                    optimum_score=s
                    dict_human[i]=optimum_score
                    df_nw=depth_max
                    print(depth_max)
        #choosing the position for the minimum score
        if(t_board[max(dict_human.keys())]==" "):
            t_board[max(dict_human.keys())]='X'
            printTic(t_board)
            print(count)
            count=0
            if(Win_Check(' ',0)==True):
                print("Comp X won")
                exit()
            
            if(' ' not in t_board.values()):
                print("Tie")
                exit()
        return True
                
    # min max implementation
    def minmax(t_board, d, condition,al,bt):
        global depth_min,depth_max,count
        #if O win it the score is 1
        if(Win_Check('O',1)==True):
        
            return 1
        # if X win the score os -1
        elif(Win_Check("X",1)==True):
           
            return -1
        # if match tie the score is 0
        elif(' ' not in t_board.values()):
       
            return 0
        
        if(condition==True):
            # - infinity
            optimum_score=-1000
            # trying all possible moves for O 
            for i in t_board.keys():
                if(t_board[i]==' '):
                    t_board[i]='O'
                    count=count+1
                    #this will lead to minimize
                    lp_condition=False
                    # calling min max recursively
                    s=minmax(t_board,d+1,lp_condition,al,bt)
                    t_board[i]=' '
                    # checking scores for all moves and choosing the max
                    if(s>optimum_score):
                        optimum_score=s
                        depth_max=d
                    tmp=max(optimum_score,s)
                    al=max(al,tmp)
                    if(al>=bt):
                        break
            return optimum_score
        else:
            # for X search auto,minimizing
            optimum_score=1000
            for i in t_board.keys():
                if(t_board[i]==' '):
                    t_board[i]= 'X'
                    count=count+1
                    lp_condition=True
                    s=minmax(t_board,d+1,lp_condition,al,bt)
                    t_board[i]=' '
                    # checking scores for all moves and choosing the minimum
                    if(s<optimum_score):
                        optimum_score=s
                        depth_min=d
                    tmp=min(optimum_score,s)
                    bt=min(bt,tmp)
                    if(bt<=al):
                        break
            return optimum_score
        
    # Computer turn
    def compTurn():
        global depth_min,depth_max,count
        optimum_score = -1000
        dict_comp={}  
        # taking every single possiblities and find the best score.
    
        for i in t_board.keys():
            if(t_board[i]==' '):
                t_board[i]='O'
            
                s=minmax(t_board,0,False,-1000,1000)
                t_board[i]=' '
                if(s>optimum_score):
                    
                    optimum_score=s
                    dict_comp[i]=optimum_score
                    print(depth_min)
        #choosing the position for the minimum score
        if(t_board[max(dict_comp.keys())]==" "):
            t_board[max(dict_comp.keys())]='O'
            printTic(t_board)
            print(count)
            count=0
            # checking if O won the game or the game is tie
            if(Win_Check(' ',0)==True):
                print("O won")
                exit()
            
            if(' ' not in t_board.values()):
                print("Tie")
                exit()
                

        return 
  
    depth_min=0
    depth_max=0     
    count=0
    t_board={}
    c=1
    for i in range(1,10):
        if(i not in t_board.keys()):
            t_board[i]=' '

    printTic(t_board)
    human='X'
    comp='O'
    exit_0=True

    while(not Win_Check(' ',0)):
        if(fst=='X'):
            exit_0=humanTurn()
            
            
            compTurn()
            
        else:
            compTurn()
            exit_0=humanTurn()
            
        if(exit_0==False):
            break

if(alg=='2' and mde=='1'):
    def printTic(t_board):
        print(t_board[1],'  |',t_board[2], "  |",t_board[3])
        print('---',"+","---","+","---")
        print(t_board[4],'  |',t_board[5], "  |",t_board[6])
        print('---',"+","---","+","---")
        print(t_board[7],'  |',t_board[8], "  |",t_board[9])
    
    # Checking available positions
    def available_pos(t_board):
        avai_array=[]
        for i in t_board:
            if(t_board[i]==' '):
                avai_array.append(i)
        print("the available positions are" ,avai_array)
        
    
    def Win_Check(criteria,a):
        a=int(a)
        #all possible strikes
        if(t_board[1]==t_board[2] and t_board[2]==t_board[3] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
       
        elif(t_board[4]==t_board[5] and t_board[5]==t_board[6] and (t_board[4]!=criteria if(a==0) else t_board[4]==criteria)):
            return True

        elif(t_board[7]==t_board[8] and t_board[8]==t_board[9] and (t_board[8]!=criteria if(a==0) else t_board[7]==criteria)):
            return True
        
        elif (t_board[1] == t_board[4] and t_board[1] == t_board[7] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
        
        elif (t_board[2] == t_board[5] and t_board[2] == t_board[8] and (t_board[2]!=criteria if(a==0) else t_board[2]==criteria)):
            return True
        
        elif (t_board[3] == t_board[6] and t_board[3] == t_board[9] and (t_board[3]!=criteria if(a==0) else t_board[3]==criteria)):
            return True
        
        elif (t_board[1] == t_board[5] and t_board[1] == t_board[9] and (t_board[1]!=criteria if(a==0) else t_board[1]==criteria)):
            return True
        
        elif (t_board[7] == t_board[5] and t_board[7] == t_board[3] and (t_board[7]!=criteria if(a==0) else t_board[7]==criteria)):
            return True
        
        else:
            return False
    # player (human turn)
    def humanTurn():
        

        
        available_pos(t_board)
        pos_human=input("enter the position of X or 0 to exit")
        pos_human=int(pos_human)
        print(t_board)
        #entering 0 exit the game
        if(pos_human==0):
            return False
        
        #inserting letter X into the tic tac game 
        # checking for empty space
        if(t_board[pos_human]==" "):
            t_board[pos_human]='X'
            printTic(t_board)
            #checking if the inserted letter X leads to win or tie
            if(Win_Check(' ',0)==True):
                print("X won ")
                exit()
          
            if(' ' not in t_board.values()):
                print("Tie")
                exit()
        return True
                
    # min max implementation
    def minmax(t_board, d, condition,al,bt):
        global depth_min,depth_max,count
        #if O win it the score is 1
        if(Win_Check('O',1)==True):
   
            return 1
        # if X win the score os -1
        elif(Win_Check("X",1)==True):
  
            return -1
        # if match tie the score is 0
        elif(' ' not in t_board.values()):
         
            return 0
        
        if(condition==True):
            # - infinity
            optimum_score=-1000
            # trying all possible moves for O 
            for i in t_board.keys():
                if(t_board[i]==' '):
                    t_board[i]='O'
                    count=count+1
                    #this will lead to minimize
                    lp_condition=False
                    s=minmax(t_board,d+1,lp_condition,al,bt)
                    t_board[i]=' '
                    # checking scores for all moves and choosing the max
                    if(s>optimum_score):
                        optimum_score=s
                        depth_max=d
                    tmp=max(optimum_score,s)
                    al=max(al,tmp)
                    if(al>=bt):
                        break
            return optimum_score
        else:
            # for X search auto,minimizing
            # + infinity
            optimum_score=1000
            for i in t_board.keys():
                if(t_board[i]==' '):
                    t_board[i]= 'X'
                    count=count+1
                    # this will lead to maximize
                    lp_condition=True
                    # calling min max recursively
                    s=minmax(t_board,d+1,lp_condition,al,bt)
                    t_board[i]=' '
                    # checking scores for all moves and choosing the minimum
                    if(s<optimum_score):
                        optimum_score=s
                        depth_min=d
                    tmp=min(optimum_score,s)
                    bt=min(bt,tmp)
                    if(bt<=al):
                        break
            return optimum_score
        
    # Computer turn
    def compTurn():
        global depth_min,depth_max,count
        # - infinity
        optimum_score = -1000
        dict_comp={}  
        # taking every single possiblities and find the best score.
    
        for i in t_board.keys():
            if(t_board[i]==' '):
                t_board[i]='O'
       
                s=minmax(t_board,0,False,-1000,1000)
                t_board[i]=' '
                if(s>optimum_score):
                    
                    optimum_score=s
                    dict_comp[i]=optimum_score
                    print(depth_min)
        #choosing the position for the minimum score
        if(t_board[max(dict_comp.keys())]==" "):
            t_board[max(dict_comp.keys())]='O'
            printTic(t_board)
            print(count)
            count=0
            # checking if O won the game or the game is tie
            if(Win_Check(' ',0)==True):
                print("O won")
                exit()
            
            if(' ' not in t_board.values()):
                print("Tie")
                exit()
                

        return 
  
    depth_min=0
    depth_max=0     
    count=0
    t_board={}
    c=1
    for i in range(1,10):
        if(i not in t_board.keys()):
            t_board[i]=' '

    printTic(t_board)
    human='X'
    comp='O'
    exit_0=True

    while(not Win_Check(' ',0)):
        if(fst=='X'):
            exit_0=humanTurn()
            
            
            compTurn()
            
        else:
            compTurn()
            exit_0=humanTurn()
            
        if(exit_0==False):
            break
      
