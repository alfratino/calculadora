#04092023-treinando python- CALCULADORA SIMPLES, REALIZANDO AS 4 OPERACOES BASICAS
#04092023 - adicionando potencia e raiz quadrada

import math as m

op = int(input("""Você pode realizar uma das quatros operações básicas abaixo: 
           1 - Soma
           2 - Subtração
           3 - Multiplicação
           4 - Divisão
           5 - Potênciação
           6 - Raiz quadrada
           
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

elif op == 5:
    n1 = int(input("Informe a base: "))
    n2 = int(input("Informe o expoente: "))
      
    s = n1 ** n2
    print(f"{n1} elevado à {n2} é {s}")

elif op == 6:
    n1 = int(input("Informe o valor que deseja a raiz: "))
    s = m.sqrt(n1)
    print(f"A raiz quadrade de {n1} é {s}")
        
else:
    print("Comando invalido!")


