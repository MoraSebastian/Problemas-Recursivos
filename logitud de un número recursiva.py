def longitud(n):
    if(abs(n)<10):
        return 1
    return 1+ longitud(abs(n)/10)

print(longitud(input("ingrese un n�mero para optener su longitud: ")))
