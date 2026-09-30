#Exercício 10: Caverna do Tesouro (Divisão de Saque)
#Um grupo de exploradores encontrou um baú com moedas de ouro.
#Eles decidiram dividir as moedas igualmente entre o número de membros da equipe. Caso sobrem moedas que não possam ser
#divididas igualmente, elas são doadas ao líder da expedição como bônus.
#• Objetivo: Leia a quantidade total de moedas de ouro encontradas e o número de exploradores.
#• Saída: Exiba quantia exata que cada explorador receberá e quantas moedas sobraram para o líder.

exploradores = int(input('Digite o numero de exploradores: '))
moedas_qtd = int(input('Digite a quantidade de moedas de ouro achadas: '))

moedas_exploradores = moedas_qtd // exploradores
bonus_lider = moedas_qtd % exploradores

print(f'Cada explorador recebera: {moedas_exploradores} moedas de ouro.')
print(f'e sobraram {bonus_lider} moedas de ouro para o lider.')