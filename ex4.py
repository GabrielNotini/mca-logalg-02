#Exercício 4: Painel Solar e Economia
#Uma residência instalou painéis solares. Cada painel gera 1.2 kWh
#por dia.
#Objetivo: Leia a quantidade de painéis instalados e o valor
#cobrado pela concessionária por kWh em reais (R$).
#Saída: Mostre quantos kWh o sistema gera em 30 dias e
#quanto a casa economizará em reais ao final do mês.

paineis_solares = int(input('Digite a quantidade de paines solares instalados: '))

valor_cobrado_concessionária = float(input('Digite a o valor cobrado por KWH: R$'))

kwh = paineis_solares * 1.2

valor_final = valor_cobrado_concessionária * kwh

mes_valor = valor_final * 30
mes_kwh = kwh * 30

print(f'O sistema gera: {mes_kwh}KWH')
print(f'O valor economizado no final do mes será R${mes_valor:.2f}')

