def SumaDigitos(a):
    
    if(abs(a)<10):
        return a
    if(abs(a)==10):
        return 1
    return abs(a)%10 + SumaDigitos(abs(a)/10)
print(SumaDigitos(input("Ingrese un entero: ")))
