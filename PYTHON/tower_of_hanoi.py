# TOWER OF HANOI 

def hanoi_tower(n, From, To, Aux):
    if(n==1): # if only 1 disk is present
        print(From + "->" + To)
        return 
    hanoi_tower(n-1, From, Aux, To)
    print(From + "->" + To)
    hanoi_tower(n-1, Aux, To, From)
n=int(input()) # n = no.of disks present
hanoi_tower(n, 'A', 'C', 'B') 