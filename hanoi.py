import time
import os
tick=0
def print_pegs(pegs):
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
    time.sleep(0.6)
    os.system('cls')
def move_disk(pegs, disk, source, dest):
    global tick
    """Moves a single disk from peg source to peg dest.

    Args:
        pegs (array):       Array holding the pegs
        disk ({0,...,n-1}): Number of the largest disk in the tower to move
        source ({0,1,2}):   Source peg (i.e., in which the tower is originally)
        dest ({0,1,2}):     Destination peg (i.e., where to put the tower)
    """
    print(f"STEP: move disk {disk} from peg {source} to peg {dest}")
    # check if the move is valid
    #if source < 0 or 2 < source: raise AssertionError("source index out of bounds")
    #if dest   < 0 or 2 < dest:   raise AssertionError("destination out of bounds")
    #if pegs[source][-1] != disk: raise AssertionError("wrong disk in source peg")
    #if pegs[dest] and (pegs[dest][-1] <= disk): raise AssertionError("destination has smaller disk")

    # do the move
    pegs[source].pop()
    pegs[dest].append(disk)
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
    move_tower(pegs, n-1, 0, 1)



def move_tower(pegs, disk, source, dest):
    spare = 3-source-dest    # number of the third peg (i.e., neither source nor dest)
    # TODO: (code missing) solve the Tower of Hanoi puzzle.
    if disk>=1:
        move_tower(pegs,disk-1,source,spare)
        move_disk(pegs,disk,source,dest)
        move_tower(pegs,disk-1,spare,dest)
    else :
        move_disk(pegs,disk,source,dest)
    # use function move_disk(...) to move a disk from one peg to another.

n = int(input("n = "))
os.system('cls')
hanoi(n)
