import array
arr = array.array('i',[1,2,3,4])
print("The Array before reversing is:",end=" ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
print("\nThe Array after reversing is:",end=" ")
arr.reverse()
for i in range(0,len(arr)):
    print(arr[i],end=" ")
