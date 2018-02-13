def encontrarMay(num):
    if num<10:
        return int(num)
    else:
        if num%10>(num/10)%10:
            return encontrarMay(nuevoNum(num/10,num%10))
        else:
            return encontrarMay(nuevoNum(num / 10, (num/10)%10))

def nuevoNum(num, mod):
    return (num-num%10)+mod



print(encontrarMay(int(input("Ingrese numero: "))))



