def longitud(n):
    if(abs(n)<10):
        return 1
    return 1+ longitud(abs(n)/10)

def Invertir(n):
    if(n<10):
        return n
    return n%10*potencia(10, longitud(n)-1)+Invertir(n/10)

def potencia(b,e):
    if e==0:
        return 1
    if e==1:
        return b
    return b*potencia(b,e-1)

print(Invertir(input("ingrese un entero: ")))
