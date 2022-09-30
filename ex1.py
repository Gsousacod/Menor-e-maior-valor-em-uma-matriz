matriz =  [ [0,0,0], [0,0,0], [0,0,0]]
me = 88888
ma = 0
for i in range (0,3):
    for j in range(0,3):
        matriz[i][j] = int(input("Digite um elemento:"))
        if(matriz[i][j]==0):
            ma=me=matriz[i][j]
        else:
                if (ma<matriz[i][j]):
                    ma = matriz[i][j]
                if(me > matriz[i][j]):
                    me = matriz[i][j]
print('<<>>'*5)                    
print(matriz)
print('<<>>'*5)
for i in range (0,3):
        for j in range(0,3):
                print(f'[{matriz[i] [j] :^5}]', end = "")
        print()
print('<<>>'*5)
print(ma)
print('<<>>'*5)
print(me)
print('<<>>'*5)