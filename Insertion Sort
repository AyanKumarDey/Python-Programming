import array
l=array.array('i',[1,8,9,7,3,4,5])
def insertion(l):
    for start in range(len(l)):
        pos=start
        while pos>0 and l[pos]<l[pos-1]:
            (l[pos],l[pos-1])=(l[pos-1],l[pos])
            pos=pos-1
    return l
result=insertion(l)
print("The sorted array is:",result)
