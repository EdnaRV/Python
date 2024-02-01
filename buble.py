from random import randint 
tam = 10

def gNumber():
    a = []
    
    for i in range(0,tam):
        n = randint(0,100)
        a.append(n)

    print("a",a)
    return a

def buble(a,tam):
    for i in range(0, tam):
        for j in range(i + 1, tam):
            if(a[i] < a[j]):
                aux = a[i]
                a[i] = a[j]
                a[j] = aux
    return a
a = gNumber()
a = buble(a,tam)
print(a)