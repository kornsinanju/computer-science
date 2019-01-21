import time
import os
tick=0
def print_pegs(pegs):
    global move
    global tick
    """Prints the pegs and the disks they contain."""
    #for i, peg in enumerate(pegs):
    #    print(f"{i}: {pegs[i]}")
    for y in reversed(range(n)):
        for x in range(3):
            #print(f"{x},{y}",end=" ")
            if pegs[x] and len(pegs[x])>y:
                #print(f"({len(pegs[x])})",end=" ")
                #print(f"{pegs[x][y]}",end=" ")
                for k in range(2*n-1):
                    if (n-1)-pegs[x][y]<=k<=n-1+pegs[x][y]:
                        print(f"#",end="")
                    else :
                        print(" ",end="")
            else :
                #print("|",end=" ")
                for k in range(2*n-1):
                    if k==n-1:
                        print("|",end="")
                    else :
                        print(" ",end="")
        print("")
    print(f"move count : {tick}")
    if(tick<move-1):
        time.sleep(0.6)
        os.system('cls')
def move_disk(pegs, source, dest):
    global tick
    """Moves a single disk from peg source to peg dest.

    Args:
        pegs (array):       Array holding the pegs
        disk ({0,...,n-1}): Number of the largest disk in the tower to move
        source ({0,1,2}):   Source peg (i.e., in which the tower is originally)
        dest ({0,1,2}):     Destination peg (i.e., where to put the tower)
    """
    # check if the move is valid
    #if source < 0 or 2 < source: raise AssertionError("source index out of bounds")
    #if dest   < 0 or 2 < dest:   raise AssertionError("destination out of bounds")
    #if pegs[source][-1] != disk: raise AssertionError("wrong disk in source peg")
    #if pegs[dest] and (pegs[dest][-1] <= disk): raise AssertionError("destination has smaller disk")

    # do the move
    if(pegs[source] and pegs[dest]):
        if(pegs[source][-1]<pegs[dest][-1]):
            disk=pegs[source].pop()
            print(f"STEP: move disk {disk+1} from peg {source} to peg {dest}")
            pegs[dest].append(disk)
        else:
            disk=pegs[dest].pop()
            print(f"STEP: move disk {disk+1} from peg {dest} to peg {source}")
            pegs[source].append(disk)
    elif(pegs[source]):
        disk=pegs[source].pop()
        print(f"STEP: move disk {disk+1} from peg {source} to peg {dest}")
        pegs[dest].append(disk)
    elif(pegs[dest]):
        disk=pegs[dest].pop()
        print(f"STEP: move disk {disk+1} from peg {dest} to peg {source}")
        pegs[source].append(disk)
    tick+=1
    # show the new state
    print_pegs(pegs)



def hanoi(n):
    """Solves the "Tower of Hanoi" puzzle for n disks."""
    if n <= 0: raise "n must be positive"

    # Initial settings
    pegs = [[] for i in range(3)]
    pegs[0] = list(reversed(range(n)))

    # show initial state
    print("Start")
    print_pegs(pegs)

    # move the tower
    move_tower(pegs)



def move_tower(pegs):
    global move
    global n
    if(n % 2 == 1):
        d=1
        a=2
    else:
        d=2
        a=1
    for i in range(1,move):
        if(i % 3 == 1):
            move_disk(pegs,0,d)
        elif(i % 3 == 2):
            move_disk(pegs,0,a)
        elif(i % 3 == 0):
            move_disk(pegs,a,d)

n = int(input("n = "))
os.system('cls')
move = 2**n
hanoi(n)
