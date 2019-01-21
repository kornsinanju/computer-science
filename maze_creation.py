import sys
import random
def genmaze(w, h):
    dirs = [[0,-1], [0,+1], [-1,0], [+1,0]]
    m = []
    for i in range(h):
        m.append([1]*w)
    mx = int(w/2)
    my = int(h/2)
    #print(f"{mx} {my}")
    root = [[mx,my]]
    m[my][mx]=0
    while 0 < len(root):
        check=0
        i = int(random.random()*len(root))
        p = root[i]
        x = p[0]
        y = p[1]
        shuffle(dirs)
        for where in range(4): #search around where to go
            v = dirs[where]
            vx = v[0]
            vy = v[1]
            ny = y + vy
            nx = x + vx
            if 0<ny<h-1 and 0<nx<w-1 and m[ny][nx] == 1: #check destination
                checkaround=0
                for where2 in range(4): # check around destination in 3 ways except the origin
                    v2=dirs[where2]
                    if m[ny+v2[1]][nx+v2[0]] == 0 and (ny+v2[1] != y or nx+v2[0]!=x):
                        checkaround=1
                if checkaround == 0:
                    m[ny][nx] = 0
                    root.append([nx, ny])
                    #showmaze(m)
                    #print(" ")
                    check=1
                    break
        if check == 0:
            del root[i]
    return m
def shuffle(a):
    # 配列の要素数ぶんだけ繰り返す。
    n = len(a)
    for k in range(n):
        # i, j: a中のランダムな位置
        x = int(random.random()*n)
        y = int(random.random()*n)
        temp=a[x]
        a[x]=a[y]
        a[y]=temp
    return a
def showmaze(m):
    for y in range(len(m)):
        s = ""
        for x in range(len(m[y])):
            if m[y][x] == 1:
                s = s + "#"
            else:
                s = s + " "
        print(s)
    return
width = int(sys.argv[1])
height = int(sys.argv[2])
m = genmaze(width, height)
showmaze(m)
