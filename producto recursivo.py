def producto(m,n):
    if n==0:
        return 0
    if n==1:
        return n
    return n + producto(m,n-1)

m=input()
n=input()
print(producto(m,n))
    
