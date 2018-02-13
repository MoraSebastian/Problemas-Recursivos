import sys
def division(dividendo, divisor):
    if divisor == 0:
       return 'la division en 0 no es valida'
    if dividendo == 0:
        return 0
    if divisor <0:
        return -1*division(dividendo,-divisor)
    if dividendo<0:
        return -1*division(-dividendo,divisor)
    if dividendo==divisor:
        return 1
    if dividendo<divisor:
        print('no es divisible')
        sys.exit()
    if dividendo>divisor:
          return 1 + division((dividendo-divisor) ,divisor)

print(division(int(input('Dividendo:')),int(input('Divisor'))))



