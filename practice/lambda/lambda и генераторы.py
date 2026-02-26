#lambda аргумен: выражение
from tabnanny import check

f = lambda x: x**2
print (f(5))

#filter like if, else
#map like for i in range
check = lambda x: "positive" if x > 0 else "negative"
print (check(5))
print (check(-5))

#генераторы (чтоб память сэкономить) там не return(бытып калады) a yield (ол замораживает)
def simple_gen():
    yield 1
    yield 2
g = simple_gen()
print (g)
print (next(g))
print (next(g))
for x in simple_gen(): #next қолданбаймыз
    print (x)

