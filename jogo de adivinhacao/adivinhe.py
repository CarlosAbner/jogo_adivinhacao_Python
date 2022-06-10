#importando bibliotecas
from random import randint
from time import sleep

#fazendo o computador pensar no numero
computador = randint(0, 5)

print('==' * 25)
print('Olá! Vamos jogar o jogo advinhação?!') 
print('De 0 a 5, qual o Nº que o computador escolheu? ')
print('==' * 25)

#jogador tentando adivinhar o numero
jogador = int(input('Em qual numero o computador pensou? '))
print('PROCESSANDO...')

#sleep faz uma pausa como se estivesse "analisando" a resposta e o Nº 2 é o segundo de espera
sleep(2)

#validando as informações
if jogador == computador:
    print('PARABÉNS!! você acertou. O número escolhido pelo computador foi {}'.format(computador))
else:
    print('VOCÊ PERDEU! Você disse {}, mas o computador escolheu esse {}'.format(jogador, computador))

    