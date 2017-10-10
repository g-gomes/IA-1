def print_table(table):
    for i in range(len(table)):
        print (table[i])
     
        
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

def find_groups(table):
    groups = [[],[],[],[],[],[],[]]
    k = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            posicao = make_pos(i,j)
            if (i == 0) and (j == 0):
                groups[k].append(posicao)
            elif ((table[i])[j]) == ((table[i])[j-1]):
                groups[k].append(posicao)
            elif ((table[i])[j]) == ((table[i-1])[j]):
                l = groups.index((i-1,j))
                groups[l].append(posicao)
            else:
                k = k+1
                groups[k].append(posicao)
    
    return groups