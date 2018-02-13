def potencia(b,e):
    if e==0:
        return 1
    if e==1:
        return b
    return b*potencia(b,e-1)

b=input("ingrese la base: ")
e=input("ingrese el exponente: ")
print( potencia(b,e))
