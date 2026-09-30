#Exercício 7: Tinta para Pintura de Parede
#Um pintor sabe que 1 litro de tinta pinta exatamente 3 metros quadrados (3m2) de parede.
#• Objetivo: Leia a largura e a altura de uma parede retangular (em metros).
#• Saída: Calcule a área total da parede e a quantidade exata de litros de tinta necessária para pintá-la.

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = altura * largura
litros_tinta = area / 3

print(f'A area da parede é {area:g}m².')
print(f'Sera necessário {litros_tinta:.2f} litros de tinta para pintar.')

