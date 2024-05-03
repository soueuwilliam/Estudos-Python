from random import choice
from os import system,name

#Lista de palavras jogo
palavras = ["maca", "banana", "laranja", "uva", "morango", "abacaxi", "melancia", "mamao", "pera", "kiwi"]
palavra_sorteada = choice(palavras)
letrasAdivinhadas = list()
letrasErradas= list()
chances = 6

def limparTela():
    if name == 'nt':
        _ = system("cls")
    else:
        _ =system("clear")

def mostrarLetrasErradas(*letrasErradas):
    if len(letrasErradas) == 0 :
        return ''
    print(f'\nLetras Erradas: ',end=' ')
    for e,c in enumerate(letrasErradas):
        print(f'{c}', end= ' ')

def palavraSorteada(palavraSorteada,letrasAdivinhadas):
    palavraDescoberta = ['-' for letra in palavraSorteada]
    for e,c in enumerate(palavraSorteada):
        if c in letrasAdivinhadas:
            print(f'{c}',end=" ")
            palavraDescoberta[e] = c         
        else:
            print('_',end=" ")
    if '-' not in palavraDescoberta:
        return True
    
while True:
    limparTela()
    print(f"Bem vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo")
    if chances > 0:
        ganhou = palavraSorteada(palavra_sorteada,letrasAdivinhadas)
        print(f'\nNumeros de chances : {chances}')
        mostrarLetrasErradas(letrasErradas)
        letra = str(input("\nDigite a letra: "))[0]
        if letra in palavra_sorteada:
            letrasAdivinhadas.append(letra)
        else:
            if letra not in letrasErradas:
                letrasErradas.append(letra)
            chances-=1
    else:
        print(f'Você perdeu a palavra era {palavra_sorteada}') 
        break
    if ganhou == True:
        print("Parabéns você ganhou o jogo e advinhou a palavra !!!!!!!!!")
        break
       