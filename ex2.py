#Exercício 2: Divisão de Lucro da Feira
#Três amigos venderam limonada na feira e decidiram dividir o lucro
#igualmente. No entanto, do total arrecadado, 10% deve ser guardado
#para comprar mais limões na próxima semana.
#Objetivo: Leia o valor total arrecadado com as vendas.
#Saída: Exiba o valor guardado para os limões e quanto cada
#um dos 3 amigos vai receber

total_arrecadado = float(input('Digite o total arrecadado: '))

limoes = (total_arrecadado * (10 / 100))
lucro = (total_arrecadado - limoes)
amigos = (lucro / 3)

print(f'Sera guardado R${limoes:.2f} para compra de novos limoes.')
print(f'Cada amigo recebera R${amigos:.2f}')