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