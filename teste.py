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

#TAI
#grupos  
def new_group():
    group = []
    return group
def add_group(group,pos):
    group.append(pos)
    return group
def find_group(group,pos):
    index = group.index(pos)
    return index

b1 = [[0,0,0,0,0],[0,2,3,3,0],[1,2,1,3,0],[2,2,2,2,0]]
grupo_fora = [(1,1),(2,1),(3,1),(3,2),(3,3),(3,0)]


def procura_em_adjacentes(board, pos, visitados):
    bolas_cor_igual=[]
    for l,c in [(0,1),(1,0),(-1,0),(0,-1)]:
        if ((((pos_l(pos) + l) >= 0 and ((pos_l(pos) + l)) < (len(board))) and ((pos_c(pos) + c) >= 0) and ((pos_c(pos) + c) < len(board[c])))):
            if board[pos_l(pos)][pos_c(pos)] == board[pos_l(pos) + l][pos_c(pos) + c]:
                if visitados[pos_l(pos)+l][pos_c(pos)+c] == 0:
                    bolas_cor_igual.append((pos_l(pos)+l,pos_c(pos)+c))
    return bolas_cor_igual

def constroi_grupo(board, pos, visitados):
    pilha = [pos]
    grupo = [pos]
    while pilha:
        posicao = pilha.pop()
        visitados[pos_l(posicao)][pos_c(posicao)] = 1
        viz = procura_em_adjacentes(board, posicao, visitados)
        for x in viz:
            l1, c1 = x
            if visitados[l1][c1] == 0:
                pilha.append(x)
                grupo.append(x)
                visitados[l1][c1] = 1
    return grupo


def board_find_groups(board):
    grupos = []
    posicao = make_pos(0,0)
    visitados = [[0 for i in range(0,len(board[0]))] for j in range(0,len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            pos = make_pos(i,j)
            if visitados[i][j] == 0:
                gru = constroi_grupo(board, pos, visitados)
                for m in gru:
                    l2, c2 = m  
                    visitados[l2][c2] = 1
                grupos.append(gru)
    return grupos

def espaco_livre(board):
    espaco = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if make_pos(i,j) == 0:
                espaco.append(constroi_grupo(board, make_pos(i,j), visitados))
    return espaco

def board_remove_group(board,group):
    col_check = [0] * len(board[0])
    lin_check = [0] * len(board)
    clone = board
    if len(group) > 1:
        for i in range(len(group)):
            l = pos_l(group[i])
            c = pos_c(group[i])
            clone[l][c] = 0
            if lin_check[l] == 0:
            	lin_check[l] = 1
            if col_check[c] == 0:
            	col_check[c] = 1


    

board_remove_group(b1,[(1,1),(2,1),(3,1),(3,2),(3,3),(3,0)])
"""
for j in range(len(clone)):
        for k in range(len(clone[j])):
            if (clone[j])[k] == 0:
                col_check[k] += 1
    for l in range(len(col_check)):
        if col_check[l] == (len(clone)-1):
            for m in range(len(clone)):
                (clone[m])[l] = (clone[m])[l+1]
                (clone[m])[l+1] = 0
                col_check[l+1] = (len(clone)-1)
"""

def auxColDel(board):
    newboard = board
    lastline = board[len(board)-1]
    for i in range(len(lastline)):
	if (lastline[i] == 0) and (i != (len(lastline)-1)):
	    for j in range(len(board)-1):
		newboard[j][i] = board[j][i+1]
		newboard[j][i+1] = 0
	elif i == (len(lastline)-1):
	    return newboard
    auxColDel(newboard)
	
class sg_state:
	_tabuleiro = []
	def __init__(self, tabuleiro):
		self._tabuleiro = tabuleiro

def auxColDel(board):
	newboard = board
	lastline = board[len(board)-1]
	for i in range(len(lastline)):
		if(lastline[i] == 0) and (i != (len(lastline)-1)):
			for j in range(len(board)-1):
				newboard[j][i] = board[j][i+1]
				newboard[j][i+1] = 0
		elif i == (len(lastline)-1):
			return newboard
	auxColDel(newboard)

#class sg_state(tabuleiro)
