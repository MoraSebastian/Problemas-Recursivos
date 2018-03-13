#Ejemplo Map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)
def rest(x):
    return (x-1)

funcs = [multiply, add,rest]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

#Ejemplo Filter
number_list = range(-10, 10)
less_than_zero = list(filter(lambda x: x%2== 0, number_list))
print(less_than_zero)


# Ejemplo Reduce
from functools import reduce
number_list = range(0, 10)
product = reduce((lambda x, y: x + y), number_list)
print(product)
