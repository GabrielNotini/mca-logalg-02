#Exercício 1: O Mago das Poções

#Um mago precisa calcular a quantidade total de mana gerada por
#suas poções. Cada poção de cura concede 15 pontos de mana e
#cada poção de energia concede 25 pontos de mana.
#Objetivo: Leia a quantidade de poções de cura e de energia
#preparadas.
#Saída: Exiba o total de mana gerado.

pocao_cura = int(input('Digite a quantidade de pocao de cura: '))
pocao_energia = int(input('Digite a quantidade de poçao de energia: '))

pocao_cura = pocao_cura * 15
pocao_energia = pocao_energia * 25

print(f'A quantidade de mana gerada foi:{pocao_cura + pocao_energia}')