def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n = input("Ingrese el termino de la sucesion que desea conocer: ")
print fibonacci(n)
  
