def create_bi(super):
    s = []
    for i in range(1,super):
        s.append("{0:b}".format(i))
    return s

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

def check_disk(num):
    global super
    k = 10
    h = 0
    for i in range(super):
        if(num%k == 1):
            return h
        k *= 10
        h += 1

def check_move(pegs,super):
    moveset=create_bi(super)
    for i in range(super-1):
        disk = check_disk(moveset[i])
        if(disk%2==0):
            move(pegs,disk,-1)
        else:
            move(pegs,disk,+1)
def hanoi(n):
    super = 2 ** n
    if n <= 0: raise "n must be positive"
    # Initial settings
    pegs = [[] for i in range(3)]
    pegs[0] = list(reversed(range(n)))
    print("Start")
    print_pegs(pegs)
    check_move(pegs,super)

n = int(input())
hanoi(n);
super = 2 ** int(n)
b=create_bi(super)
check_move(b)
