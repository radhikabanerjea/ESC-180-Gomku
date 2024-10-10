"""Gomoku starter code
Skeleton Code Created by Michael Guerzhoy
Final Funtionality Created by Radhika Banerjea
"""
#Last Update 4:20 AM
 
def is_empty(board):
    for r in range (len(board)):
        for c in range(len(board[r])):
            if board[r][c] == " ":
                pass
            else:
                return False
    return True
   
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    countBounds = 0
    if d_y == 0:
        if (x_end == 7) or (x_end ==  0):
            countBounds += 1
        elif (board[y_end+d_y][x_end+d_x])!=" ":
            countBounds += 1    
        
        if ((x_end - ((length-1)*d_x)) == 7) or ((x_end - ((length-1)*d_x)) == 0):
            countBounds += 1 
        elif (board[y_end][x_end - (length*d_x)])!= " ":
            countBounds += 1 
    
    elif d_x == 0:
        if (y_end == 7) or (y_end ==  0):
            countBounds += 1
        elif (board[y_end+d_y][x_end+d_x])!=" ":
            countBounds += 1    
        
        if (y_end - ((length-1)*d_y) == 7) or (y_end -(length-1)*d_y== 0):
            countBounds += 1 
        elif (board[y_end - (length*d_y)][x_end])!= " ":
            countBounds += 1 
    
    else:
        if (x_end == 7) or (x_end ==  0) or (y_end == 7) or (y_end ==  0):
            countBounds += 1
        elif (board[y_end+d_y][x_end+d_x])!=" ":
            countBounds += 1    

        if (y_end - ((length-1)*d_y) == 7) or (x_end - ((length-1)*d_x) == 7) or (y_end -((length-1)*d_y)== 0) or (x_end - ((length-1)*d_x) == 0):
            countBounds += 1 
        elif (board[y_end - (length*d_y)][x_end - (length*d_x)])!= " ":
            countBounds += 1 

    #This method detects the rows        
    if countBounds == 1:
        return "SEMIOPEN"
   
    elif countBounds == 0:
        return "OPEN"
    else:
        return "CLOSE"
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0
    lengthChecker = 0
    
    
    if d_y == 0:

        for c in range (len(board)):
            #print("c is,  ", c)
            #print("the lengthChecker is ", lengthChecker)
            if(board[y_start][c] == col):
                lengthChecker += 1
            else: 
                if lengthChecker == length:
                    #print("lengthchecker is equal to length")
                    if is_bounded(board, y_start, c-d_x, length, 0, 1) == "SEMIOPEN":
                        #print("its semiopen")
                        semi_open_seq_count += 1
                    elif is_bounded(board, y_start, c-d_x, length, 0, 1) == "OPEN":  
                        #print("its open") 
                        open_seq_count += 1
                    lengthChecker = 0
                   
        if lengthChecker == length:            

            if is_bounded(board, y_start, 7, length, 0, 1) == "SEMIOPEN":
                semi_open_seq_count += 1
            elif is_bounded(board, y_start, 7, length, 0, 1) == "OPEN":            
                open_seq_count += 1

               
    elif d_x == 0:
        for r in range (len(board)):
            if(board[r][x_start] == col):
                lengthChecker += 1
            else:
                if lengthChecker == length:
                    if is_bounded(board, r-d_y, x_start, length, 1, 0) == "SEMIOPEN":
                        semi_open_seq_count += 1
                    elif is_bounded(board, r-d_y, x_start, length, 1, 0) == "OPEN":   
                        open_seq_count += 1
                   
                    lengthChecker = 0
 
        if lengthChecker == length:            
            if is_bounded(board, 7, x_start, length, 0, 1) == "SEMIOPEN":
                semi_open_seq_count += 1
            elif is_bounded(board, 7, x_start, length, 0, 1) == "OPEN":            
                open_seq_count += 1
        
        
   
    else:
        if(board[y_start][x_start] == col):
                lengthChecker += 1
 
        x = x_start + d_x
        y = y_start + d_y
 
        while (x != 8) and (x != -1) and (y != 8) and (y != -1):
           # print("i entered the while loop")
            #print("x is ", x)
            #print("y is ", y)
            #print("the lengthchecker is a ", lengthChecker)
            if(board[y][x] == col):
                lengthChecker += 1         
            else:
                if lengthChecker == length:
                    #print("The lengthchecker is equal to length")    
                    if is_bounded(board, y-d_y, x-d_x, length, d_y, d_x) == "SEMIOPEN":
                        semi_open_seq_count += 1
                        #print("i added to the semi count")
                    elif is_bounded(board, y-d_y, x-d_x, length, d_y, d_x) == "OPEN":  
                        open_seq_count += 1
                        #print("i added to the open count")

                lengthChecker = 0
            
            #print("the lengthchecker is b ", lengthChecker)
            x += d_x
            y += d_y
        
        x -= d_x
        y -= d_y
        #print("out of the while: x = ", x)
        #print("out of the while: y = ", y)
        if lengthChecker == length:
            #print("The lengthchecker is equal to length")    
            if is_bounded(board, y, x, length, d_y, d_x) == "SEMIOPEN":
                semi_open_seq_count += 1
                #print("i added to the semi count")
            elif is_bounded(board, y, x, length, d_y, d_x) == "OPEN":  
                open_seq_count += 1
                #print("i added to the open count")

                    
    return open_seq_count, semi_open_seq_count
   
def addLists (list1, list2):
    listFinal = []
    for i in range(len(list1)):
        listFinal.append(list1[i]+list2[i])
    return listFinal

def minusLists (list1, list2):
    listFinal = []
    for i in range(len(list1)):
        listFinal.append(list1[i]-list2[i])
    return listFinal

def detect_rows(board, col, length):

    francassca = [0,0]
    
    for row in range(len(board)):
        #print("row = , ",row)
        francassca = addLists(francassca, list(detect_row(board, col, row, 0, length, 0, 1)))
        #print("francassa checked the rows, ", francassca)
        francassca = addLists(francassca, list(detect_row(board, col, row, 0, length, 1, 1)))
        #print("francassa checked diagonal, left top to right bottom DOWN, ", francassca)
        francassca = addLists(francassca, list(detect_row(board, col, row, 0, length, -1, 1)))
        #print("francassa checked diagonal, left bottom to right top UP, ", francassca)

    #print(francassca)

    for column in range(len(board)):
        #print("column = , ",column)
        francassca = addLists(francassca, list(detect_row(board, col, 0, column, length, 1, 0)))
        #print("francassa checked the columns, ", francassca)
        francassca = addLists(francassca, list(detect_row(board, col, 0, column, length, 1, 1)))
        #print("francassa checked diagonal, left top to right bottom UP, ", francassca)
        francassca = addLists(francassca, list(detect_row(board, col, 7, column, length, -1, 1)))
        #print("francassa checked diagonal, left bottom to right top DOWN, ", francassca)


    #print(francassca)

    francassca = minusLists(francassca, list(detect_row(board, col, 0, 0, length, 1, 1)))
    #print("minusing top left to bottom right ", francassca)
    francassca = minusLists(francassca, list(detect_row(board, col, 0, 7, length, 1, -1)))
    #print("minusing bottom left to top right ", francassca)


    #print(francassca)
    
    open_seq_count, semi_open_seq_count = francassca[0], francassca[1]
    return open_seq_count, semi_open_seq_count
   
def search_max(board):
    count = 0
    pointMax = 0
    move_y = 0
    move_x = 0

    
    for row in range(len(board)):
        for column in range (len(board[row])):
            if board[row][column] == " ":
                #print("the point is: (", row, ",", column,")")
                count = count+1
                
                if count == 1:
                    board[row][column] = "b"
                    pointMax = score(board)
                    move_y = row
                    move_x = column
                    board[row][column] = " "

                board[row][column] = "b"
                #print("the score of the board is ", score(board))
                if score(board) > pointMax:
                    #print(score(board), " > ", pointMax)
                    pointMax = score(board)
                    move_y = row
                    move_x = column
                board[row][column] = " "

    return move_y, move_x
   
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def is_full(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if (board[row][column] == " "):
                return False
    return True

def is_5(board, col, y_start, x_start, d_y, d_x):

    lengthChecker = 0  
    
    if d_y == 0:

        for c in range (len(board)):
            if(board[y_start][c] == col):
                lengthChecker += 1
                if lengthChecker == 5:
                    return True
            else:
                lengthChecker = 0

    elif d_x == 0:

        for r in range (len(board)):
            if(board[r][x_start] == col):
                lengthChecker += 1
                if lengthChecker == 5:
                    return True
            else:
                lengthChecker = 0
    
    else:
        if(board[y_start][x_start] == col):
                lengthChecker += 1
 
        x = x_start + d_x
        y = y_start + d_y
 
        while (x!= 8) and (x != -1) and (y!= 8) and (y != -1):
            if(board[y][x] == col):
                lengthChecker += 1
                if lengthChecker == 5:
                    return True
            else:
                    lengthChecker = 0
            x += d_x
            y += d_y


    return False

def whole_fives(board, col):
    
    for row in range(len(board)):
        if is_5(board, col, row, 0, 0, 1) == True or is_5(board, col, row, 0, 1, 1) == True or is_5(board, col, row, 0, -1, 1) == True:
            return True

    for column in range(len(board)):
        if is_5(board, col, 0, column, 1, 0) == True or is_5(board, col, 0, column, 1, 1) == True or is_5(board, col, 7, column, -1, 1) == True:
            return True

    return False

def is_win(board):
    if whole_fives(board, "w") == True:
        return "White won"
    elif whole_fives(board, "b") == True:
        return "Black won"
    elif is_full(board):
        return "Draw"
    else:
        return "Continue playing"

def print_board(board):
   
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
   
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])
   
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
   
    print(s)
   
def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                
def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i)
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
         
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
   
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
           
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
       
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
       
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
       
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
                              
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")
 
def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
   
    y_end = 3
    x_end = 5
 
    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")
 
def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")
 
def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")
 
def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")
 
def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()
 
def some_tests():
    board = make_empty_board(8)
 
    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
   
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
   
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
   
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
   
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #    
   
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
   
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
 
 
 
           
if __name__ == '__main__':

    #play_gomoku(8)
    #board = make_empty_board(8)
    '''
    *0|1|2|3|4|5|6|7*
    0 | | | | | | | *
    1 | | | | | | | *
    2b|b|b|b|w| | | *
    3 | | | |w| | | *
    4 | | | |w| | | *
    5 | | | | | | | *
    6 | | | | | | | *
    7 | | | | | | | *
    *****************
    '''
    '''
    gomokuBoard = [ [" "," "," "," "," "," "," "," "],
                    [" "," "," "," ","b"," "," "," "],
                    ["b","b","b","b","w"," "," "," "],
                    [" "," "," "," ","w"," "," "," "],
                    [" "," "," "," ","w"," "," "," "],
                    [" "," "," "," "," "," "," "," "],
                    [" "," "," "," "," "," "," "," "],
                    [" "," "," "," "," "," "," "," "]]
    '''

    #print(test_search_max())
    #print(search_max(gomokuBoard))
    #print(score(gomokuBoard))

    #print_board(gomokuBoard)    
    #print(detect_rows(gomokuBoard,"b", 3))
    #print(detect_row(gomokuBoard, "b", 0, 5, 3, 1, 0))
    #print(is_empty(gomokuBoard))
    #print(is_bounded(gomokuBoard,2, 2, 2, 1, 1))
   
    #print(detect_rows(gomokuBoard,"w", 2))
    #print(is_win(gomokuBoard))
    #print(whole_fives(gomokuBoard, "b"))
    
