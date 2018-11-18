import time
def main():
    num = int(input("input: "))
    if(num == 1 ):
        print("1")
    else :
        count = 0
        x = 10
        checkpo = False
        done = False
        bucket = [ 0 for i in range(num+1) ]
        print("0.")
        tick = 0
        remainder = 1
        while not done:
            #time.sleep(0.5)
            quotient = x//num
            remainder = x%num
            x = remainder * 10
            count += 1
            if(quotient != 0):
                checkpo = True
            if(remainder == 0 ):
                done = True
                print(f"{count} : {quotient} {remainder}")
            else :
                if(bucket[remainder]==0 and checkpo == True):
                    bucket[remainder] +=1
                    print(f"{count} : {quotient} {remainder}")
                elif(bucket[remainder]==1):
                    bucket[remainder]+=1
                    print(f"saving {count} : {quotient} {remainder}")
                elif(bucket[remainder]==3) :
                    done = True
if __name__=='__main__':
    main()
