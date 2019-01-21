#question one : n times at most
#question two :
def sorted_search(elt,array):
    k=0 #set as not found at first
    mid = len(array)//2
    if(array[mid]==elt):
        return 1 #if found return 1
    if(len(array)>1):
        if(array[mid]>elt):
            lefthalf = array[:mid]
            k=sorted_search(elt,lefthalf)
        elif(array[mid]<elt):
            righthalf = array[mid+1:]
            k=sorted_search(elt,righthalf)
    return k
elt = 1
array = [1,3,5,8,12,13,15,16,18,20,22,30,40,50,55,67]
print(sorted_search(elt,array)) # 0 means cant find, 1 mean found
#question 3 : ln(N)/ln(2) times at most	(log n base 2 times at most)
