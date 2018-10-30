import time
def main():
    num = input("input: ")
    if(num == 1 ):
        print("1")
    else :
        x = 1
        done = False
        bucket[0 for a in range(num+1) ]
        print("0.", end = "")
        tick = 0
        while not done:
            time.sleep(0.1)
            if(x<num):
                x *= 10
                remainder = x
                count += 1
            else :
                quotient = x//num
                remainder = x%num
                x = remainder
                count +=1
            if(remainder == 0 ):
                done = True
                print("")
            else :
                if(bucket[remainder]==0):
                    bucket[remainder] +=1
                    print(f"{quotient}", end = "")
                elif(bucket[remainder]==1):
                    bucket[remainder]+=1
                    if(tick == 0):
                        print("(", end = "")
                        tick +=1
                    else:
                        print(f"{quotient}", end = "")
                else :
                    done = True
                    print(")")
if __name__=='__main__':
    main()
