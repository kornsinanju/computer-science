import time
def main():
    num = int(input("input: "))
    if(num == 1 ):
        print("1")
    else :
        count = 0
        x = 10
        checkzero = False
        done = False
        bucket = [ 0 for i in range(num+1) ]
        print("0.", end = "")
        tick = 0
        remainder = 1
        while not done:
            #time.sleep(0.1)
            quotient = x//num
            remainder = x%num
            x = remainder * 10
            count += 1
            if(quotient != 0):
                checkzero = True
            #print(f"{count} : {quotient} {remainder}")
            if(remainder == 0 ):
                print(f"{quotient}")
                done = True
            else :
                if(bucket[remainder]==0):
                    if(checkzero == True):
                        bucket[remainder] +=1
                    print(f"{quotient}", end = "")
                elif(bucket[remainder]==1):
                    bucket[remainder]+=1
                    if(tick == 0):
                        print(f"(", end = "")
                        tick +=1
                    print(f"{quotient}", end = "")
                else :
                    done = True
                    print(")")
if __name__=='__main__':
    main()
