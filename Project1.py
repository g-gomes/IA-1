def print_board(board):
    for i in range(len(board)):
        print (board[i])
     
        
# TAI color
# sem cor = 0
# com cor > 0
def get_no_color():
    return 0
def no_color (c):
    return c==0
def color (c):
    return c > 0

# TAI pos
# Tuplo (l, c)
def make_pos (l, c):
    return (l, c)
def pos_l (pos):
    return pos[0]
def pos_c (pos):
    return pos[1] 

def new_group():
    group = []
    return group
def add_group(group,pos):
    group.append(pos)
    return group
def find_group(group,pos):
    index = group.index(pos)
    return index
        

def board_find_groups(board):
    group_lst = []
    k = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i == 0) and (j == 0):
                pos = make_pos(i,j)
                group_lst.append(new_group())
                temp = group_lst[k]
                add_group(temp,pos)
            elif ((board[i])[j]) == ((board[i])[j-1]):
                pos = make_pos(i,j)
                temp = group_lst[k]
                add_group(temp,pos)
            elif ((board[i])[j]) == ((board[i-1])[j]):
                index = 0
                for k in range(len(group_lst)):
                    for l in range(len(group_lst[k])):
                        if ((group_lst[k])[l]) == ((board[i])[j]):
                            index = k
                pos = make_pos(i,j)
                temp = group_lst[index]
                add_group(temp,pos)
            else:
                k = k+1
                group_lst.append(new_group())
                temp = group_lst[k]
                add_group(temp,pos)                
   
    return group_lst

def board_remove_group(board,group):
    col_check = []
    clone = board
    for i in len(group):
        l = pos_l(group[i])
        c = pos_c(group[i])
        if (l != 0) and (color((clone[l-1])[c])):
            (clone[l])[c] = (clone[l-1])[c]
            (clone[l-1])[c] = 0
        else:
            (clone[l])[c] = 0
    for j in len(clone):
        for k in len(clone[j]):
            if (clone[j])[k] == 0:
                col_check[k] += 1
    for l in len(col_check):
        if col_check[l] == (len(clone)-1):
            for m in len(clone):
                (clone[m])[l] = (clone[m])[l+1]
                (clone[m])[l+1] = 0
                col_check[l+1] = (len(clone)-1)
            
            
            
        
