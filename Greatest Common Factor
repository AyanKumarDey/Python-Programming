# Python Code For Greatest Common Factor.
def gcd(m,n):
    fm=[] #List for factor list of m.
    for i in range(1,m+1):
        if (m%i==0):
            fm.append(i)
    fn=[] #List for factor list of n.
    for j in range(1,n+1):
        if (n%j==0):
            fn.append(j)
    cf=[] #List for common factor list.
    for f in fm:
        if f in fn:
            cf.append(f)
    return cf[-1]
m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
print("The Greatest Common Divisor is:",gcd(m,n))
