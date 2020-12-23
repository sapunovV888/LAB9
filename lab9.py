from random import choice

def strochka(k,n):
    str_list = [str(i) for i in range(k+1)]
    s=' '.join(choice(str_list) for i in range(n))
    return s
