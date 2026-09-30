#Exercício 9: Rendimento do Atleta
#Um corredor percorreu uma determinada distância em quilômetros em um tempo medido em minutos.
#Objetivo: Leia a distância percorrida (em km) e o tempo gasto (em minutos).
#Saída: Calcule a velocidade média do atleta em km/h e em
#m/s.(Dica: divida os minutos por 60 para achar o tempo em horas).

distancia_km = float(input('Digite a distancia percorrida em km: '))
tempo_minutos = int(input('Digite o tempo gasto em minutos: '))

tempo_horas = tempo_minutos / 60
distancia_metros = distancia_km * 1000
tempo_segundos = tempo_minutos * 60

velocidade_ms = distancia_metros / tempo_segundos
velociade_media = distancia_km / tempo_horas

print(f'A velocidade media foi de {velociade_media}km/hora e foi de {velocidade_ms:.2f} metros por segundo.')