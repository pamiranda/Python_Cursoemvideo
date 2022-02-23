import random
from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura' )
pc = random.randint(0, 2)
sleep(2)
print("HEY, HUMANO...VAMOS JOGAR?\nSua opções:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA")
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('=*='*12)
print('Eu escolhi {}'.format(itens[pc]))
print('Você escolheu {}'.format(itens[jogador]))
print('=*='*12)
if pc == 0 :
    if jogador == 0:
        print('Empatamos!')
    elif jogador == 1:
        print('PARABÈNS, VOCÊ ME VENCEU!   =)')
    elif jogador == 2:
        print('EU VENCI, PARABÉNS PRA MIM!   =)')
elif pc == 1 :
    if jogador == 1:
        print('Empatamos!')
    elif jogador == 2:
        print('PARABÈNS, VOCÊ ME VENCEU! =)')
    elif jogador == 0:
        print('EU VENCI, PARABÉNS PRA MIM!   =)')
elif pc == 2:
    if jogador == 2:
        print('Empatamos!')
    elif jogador == 0:
        print('PARABÈNS, VOCÊ ME VENCEU!  =)')
    elif jogador == 1:
        print('EU VENCI, PARABÉNS PRA MIM!   =)')















 
 
 
 
