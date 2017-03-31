
def maximo_int(y):
    tam = len(y)
    maior = y[0]
    for i in range(len(y)):
        if y[i] > maior:
            maior = y[i]
    return maior

def maximo_rec(y,n):
    if n == 1 :
        return y[0]
    else:
        x = maximo_rec(y,n-1)
        if (x>y[n-1]):
            return x
        else:
            return y[n-1]

def soma_array_rec (y,n):
    if n == 1:
        r = y[0]
        return r
    else:
        r = y[n-1] + soma_array_rec(y,n-1)
        return r

def soma_array_rec2 (y):
    if len(y) == 1:
        r = y[0]
        return r
    else:
        r = y[0] + soma_array_rec2(y[1:])
        return r

def fatorial(y):
    if y <= 1:
        return 1
    else:
        return y * fatorial(y-1)


def menor_elemento_int(y):
    menor = y[0]
    for x in range(len(y)):
        if y[x] < menor:
            menor = y[x]
    return menor

def menor_elemento_rec(y,n):
    if n == 1:
        return y[0]

    meio = n/2
    menor = y[n-1]
    if menor < menor_elemento_rec (y,n-1):
        return menor
    else:
        return menor_elemento_rec(y, n - 1)

myList=[12,32,5,15,0]
tam = len(myList)
print(menor_elemento_int(myList))
print(menor_elemento_rec(myList,tam))

#print(fatorial(15))

#myList=[1,1,5,15,0]
#tamL = len(myList)
#print(soma_array_rec2(myList))

#print ("Máximo e:")
#print(maximo_rec(myList,tamL))