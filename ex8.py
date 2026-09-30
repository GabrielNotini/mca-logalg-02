#Exercício 8: O Cofrinho da Vovó
#Um neto quer saber quanto guardou em moedas no cofrinho da sua avó
#Objetivo: Leia a quantidade de moedas de R$ 0,10, R$ 0,25 e R$ 0,50
#Saída: Calcule e exiba o valor total poupado em reais (R$)

moeda_010_qtd = int(input('Digite a quantidade de moedas de 10 centavos: '))
moeda_025_qtd = int(input('Digite a quantidade de moedas de 25 centavos: '))
moeda_050_qtd = int(input('Digite a quantidade de moedas de 50 centavos: '))

moeda_010_total = moeda_010_qtd * 0.10
moeda_025_total = moeda_025_qtd * 0.25
moeda_050_total = moeda_050_qtd * 0.50

valor_total = (moeda_010_total + moeda_025_total + moeda_050_total)

print(f'O Valor poupado foi: R${valor_total:.2f}')