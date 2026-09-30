#Exercício 6: Fabricação de Capinhas de Celular
#Uma fábrica produz capinhas de celular. O custo de produção de
#cada capinha é composto por:
#R$ 3,50 de matéria-prima;
#R$ 1,50 de mão de obra;
#R$ 0,80 de embalagem.
#A fábrica vende cada capinha por um valor fixo informado pelo
#usuário.
#Objetivo: Leia a quantidade de capinhas produzidas e o preço
#de venda unitário.
#Saída: Exiba o custo total de produção e o lucro líquido obtido
#com a venda do lote.

materia_prima = 3.50
mao_obra = 1.50
embalagem = 0.80

valor_capinha = float(input('Digite o valor fixo de cada capinha: '))
qtd_capinha = int(input('Digite a quantidade de capinhas produzidas: '))

custo_produçao = (materia_prima + mao_obra + embalagem)
custo_produçao_total = custo_produçao * qtd_capinha
valor_venda = valor_capinha * qtd_capinha
lucro = valor_venda - custo_produçao_total

print(f'O custo de produçao por capinha foi de R${custo_produçao_total:.2f}')
print(f'O lucro da produçao foi de R${lucro:.2f}')
