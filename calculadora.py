#-treinando python- CALCULADORA SIMPLES, REALIZANDO AS 4 OPERACOES BASICAS

import math as m

op = int(input("""Você pode realizar uma das quatros operações básicas abaixo: 
           1 - Soma
           2 - Subtração
           3 - Multiplicação
           4 - Divisão
           
           Qual operação deseja: """))
if op == 1:
    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))
    
    s = n1 + n2
    print(f"{n1} + {n2} = {s}")
    
elif op == 2:
    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))
    
    s = n1 - n2
    print(f"{n1} - {n2} = {s}")

elif op == 3:
    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))
    
    s = n1 * n2
    print(f"{n1} + {n2} = {s}")
    
elif op == 4:
    n1 = float(input("Informe o primeiro número: "))
    n2 = float(input("Informe o segundo número: "))
    
    s = n1 / n2
    print(f"{n1} / {n2} = {s:.2f}")
   
else:
    print("Comando invalido!")


