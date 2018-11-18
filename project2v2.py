import time
def main():
    num = int(input("input: "))
    x = 1
    done = False
    bucket = [ 0 for i in range(num+1) ]
        #print("0.", end = "")
    count=0
    tick = 0
    while not done:
        #time.sleep(0.1)
        quotient = x//num
        remainder = x%num
        x = remainder * 10
        count += 1
        #print(f"{count} : {quotient} {remainder}")
        if(remainder == 0 ):
            print(f"{quotient}")
            break
        else :
            if(bucket[remainder]==0):
                bucket[remainder] +=1
                print(f"{quotient}", end = "")
            elif(bucket[remainder]==1):
                bucket[remainder] +=1
                print(f"{quotient}", end = "")
                if(tick == 0) :
                    print("(", end = "")
                    tick = 1
            elif(bucket[remainder]==2):
                print(f"{quotient}", end = "")
                print(")", end = "")
                done = True
        if(count == 1 ):
            print(".", end = "")
if __name__=='__main__':
    main()
