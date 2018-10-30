#The concept is to use decimal expansion theory (ref: mathworld.wolfram.com/DecimalExpansion.html)
#stating that when a rational number m/n with (m,n)=1 is expanded, the period (repetitive decimal)
#begins after s terms and has length  t, where s and t are the smallest numbers satisfying
#                            10^s=10^(s+t) (mod n).
#When n≢0 (mod 2, 5), s=0, and this becomes a purely periodic decimal with
#                            10^t=1 (mod n).
#In the code I change the variable a liitle by making s = s+t. Also I use bucket theory to save possible 's' value because
# the idea is just to find what is the positive minimum t and s that 10^t (mod n) gives
# the same remainder as 10^(s+t) mod(n) where n = divider(input).
#After I implement this theory into the code(line 18-32). I will know exactly from when is the decimal be repetitive and how long.
#After that, I use this information as the define condition in  the common long divition method under the length t.
#Noted that when the decimal is finite, t-s will be equal to one and the next quotient
# of the calculation is 0 (finite deciamal is when 0 is repetitive at the end of the number)
#In addition to that, I also need to add the condition for when will I add '(' and ')' (further explantion along the code)

def main():
    num = int(input("input: "))
    if(num == 1 ): #exclude exception from the algorithm
        print("1")
    elif(num == 0): #exclude exception from the algorithm
        print("ERROR(infinity)")
    else :
        count = 0 #will be used for number of s+t and pointer of the postion of decimal
        x = 1# start implementing the decimal method theory from 10^0(equal to one)
        done = False
        bucket = [ 0 for i in range(num+1) ]# create bucket array that will save the possible t value by bucket method(its size should be equal to all possible remainder).Noted that 0 means unoccupied.
        while not done:
            remainder = x%num # mod it by n(input)
            if(bucket[remainder]==0 and remainder!=1):
                bucket[remainder]=count # use bucket method to save possible "s" value in it
            elif(remainder==1): #specific case when the remainder equal '1' since if i use the upper condition, the program will save bucket[1]=0 (t=0) and that make it seems that it is not occupied (saved with t=0 value).
                if(count != 0): #to make it skip the first loop
                    done = True #stop loop
                    t = count #save my t value(=s+t of the theory)
                    s = 0 #the start of the repetitive will be from the start.
            else : #when the bucket[remainder] is already occupied with s before running until t which give the same remainder.By this, we will get what we want already.
                done = True# After we got minimum s,t, we just stop the loop.
                t = count #Different from the theory,my t equal to t+s of the theory = the length of both non-repetitive decimals and repetitive decimals.
                s = bucket[remainder] #save the real s value saved in the bucket to s variable
            x = remainder * 10 #According to the theory,keep times ten until I get s and t.
            count += 1 # the length of non-repetitive decimals plus the length of repetitive decimals.(the length of the supposed decimal's output)
#from now on,it is to print out the answer according to s and t value we got from above.
        x=10 # set numberator equal to 10 since I will start calculation from the first decimals.
        print(f"0.",end="")# print out common output and prevent it from adding new line or extra space
        count = 0 # restart the ticker( for the loop) for usage in the next line
        while count < t:# run the loop for the length of the supposed output(t)
            if(count==s):#Check whether the position of the decimal reach repetitive decimal zone or not. If yes, print out '('
                if(x//num==0 and t-s==1):# to exclude out the case where the answer is finite decimal as explained above.
                    break # breakout from the loop (make it finite)
                print(f"(",end="")# if it didn't break out from the loop(not finite decimals), the program will start print '('
            quotient = x//num #line 47-49 : implementing normal long divition method
            remainder = x%num
            x = remainder * 10
            print(f"{quotient}",end="") # print out quotient and restrict the function from starting new line or add extra space at the end of the output
            count +=1#updating the ticker (pointer)
            if(count==t): # when print out to the end of the repetitive decimals, print ')'
                print(f")")
        #print(f"{s} {t}")
if __name__=='__main__':
    main()
