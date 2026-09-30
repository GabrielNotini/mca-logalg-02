#Exercício 3: Consumo de Ração do Pet
#Um tutor comprou um saco de ração para seu cão com a
#quantidade medida em quilogramas (kg). Todos os dias, o cão
#consome uma quantidade fixa em gramas (g).
#Objetivo: Leia o peso do saco de ração (em kg) e a quantidade
#diária consumida pelo cão (em g).
#Saída: Calcule e exiba quanto da ração (em gramas) sobrará
#após 5 dias. (Dica: 1 kg = 1000 g).

print('Quanto sobrará de Racao em 5 dias ?')
racao = float(input('Digite a quantidade em (KG) do saco de raçao: '))
cao_gramas = float(input('Digite a quantidade de raçao em Gramas(g) consumida pelo cao: '))

racao_gramas = (racao * 1000)
cao_5dias_gramas = (cao_gramas * 5)
sobra = (racao_gramas - cao_5dias_gramas)

print(f'Com base na quantidade de Raçao, sobrará {sobra} gramas de Raçao')

