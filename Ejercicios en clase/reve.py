notas = 0;
soma = 0
while notas>=0:
    notas = int(input("Digite a quantidade de notas: "))
    if notas >=0 and notas <6:
        if notas % 1 == 0 and notas % 2 != 0  or notas % 1 == 0 and  notas ==2:
            soma += notas
    
print("las notas sumadas en total es: ",soma)

