# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!
comando = 0
print("\n******************* Calculadora em Python *******************")
comandos ={
     1 : '+',
     2 : '-',
     3 : '*',
     4 : '/'
}

while True:
    n1 = int(input('Digite o primeiro numero '))
    n2 = int(input('Digite o segundo numero '))
    comando = int(input("""
    Digite A operação desejada:
    1 - soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão   
    5 - Sair               
    """)) 
    if(comando == 5):
        break
    elif(comando > 0 and comando <= len(comandos) + 1):

        print(eval(f"{n1}{comandos[comando]}{n2}")if comando in comandos else None)
    else:
        print('Você digitou um operação invalida')

       
        

