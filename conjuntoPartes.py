
def conjunto_das_partes(set):
    size = pow(2, len(set))
    if not set:
        print("{{ }}",end='')
    else:
        print("{",end='')
        for counter in range(0,size):
            print("{",end='')
            for j in range(0,size):
                if(counter & (1 << j)):
                    print(set[j]+ ",",end='')
            print("\b", end='}\n')

#Insira aqui o seu conjunto
mySet = ['a','b','c']
conjunto_das_partes(mySet)