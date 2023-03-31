# Binary Search
import array
lis = array.array('i',[1,2,3,4,5,6,7])
def by_search(lis,v,l,r):
    if r>=l:
        mid = (r+l)//2
        if(v==lis[mid]):
            return mid
        if(v<lis[mid]):
            return (by_search(lis,v,l,mid))
        else:
            return (by_search(lis,v,mid+1,r))
    return -1
v=int(input("Enter the number:"))
l=0
r=len(lis)-1
result= by_search(lis,v,l,r)
if result != -1:
   print("The element found in the index is:",result)
else:
    print("Not found")
