#Exercício 5: Conversor de Tempo de Maratonista
#Um maratonista registrou seu tempo total de treino apenas em
#segundos.
#Objetivo: Leia a quantidade total de segundos.
#Saída: Converta e exiba esse tempo no formato: Horas,
#Minutos e Segundos. (Dica: use os operadores de divisão / e
#resto da divisão %).

tempo_segundos = int(input('Digite o tempo de treino em (segundos): '))

tempo_horas = tempo_segundos / 3600
resto_tempo = tempo_segundos % 3600
tempo_minutos = resto_tempo / 60
segundos = resto_tempo % 60

print(f'O tempo foi: {tempo_horas} Horas, {tempo_minutos} Minutos, {segundos} Segundos.')
