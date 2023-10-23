"""
Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções sempre que necessário. 
Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. 
Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). 
Após a conclusão da soma, o novo estado da memória passa a ser 8.

Estado da memória: 0
Opções:(1) Somar
(2) Subtrair
(3) Multiplicar
(4) Dividir
(5) Limpar memória
(6) Sair do programa
Qual opção você deseja?
"""

import random as rnd

def somar (memoria, numero):
    return memoria + numero

def subtrair (memoria, numero):
    return memoria - numero

def multiplicar (memoria, numero):
    return memoria * numero

def dividir (memoria, numero):
    if numero != 0:
        return memoria / numero
    else:
        print("erro, zero nao divide")
        return memoria     
    
def limpar ():
    return 0

def menu ():
        memoria = 0
        print('='*10)
        print(f"estado da memória: {memoria}")
        print("(1) somar")
        print("(2) subtrair")
        print("(3) multiplicar")
        print("(4) dividir")
        print("(5) limpar memória")
        print("(6) sair")
        return int(input('Digite sua opcao: '))

def main ():
   memoria = 0
   op = 0
   while op !=6:
       op = menu()
       if op == 1:
        numero = float(input("digite o número para somar: "))
        memoria = somar(memoria, numero)
       elif op == 2:
        numero = float(input("digite o número para subtrair: "))
        memoria = subtrair(memoria, numero)
       elif op == 3:
        numero = float(input("digite o número para multiplicar: "))
        memoria = multiplicar(memoria, numero)
       elif op == 4:
        numero = float(input("digite o número para dividir: "))
        memoria = dividir(memoria, numero)
       elif op == 5:
        memoria = limpar()
       elif op == 6: 
        print("saindo....")
        break
       else:
            print("opção inválida")

if __name__ == '__main__':
    main()