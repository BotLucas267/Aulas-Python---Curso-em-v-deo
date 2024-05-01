#Desafio 005 - Antecessor e Sucessor

d = int(input("Digite um número: "))
a = d - 1
s = d + 1
print("O antecessor desse número é:", a,"e o Sucessor é:", s)

#Desafio 006 - Multiplicação e Raiz quadrada

n = int(input("Digite um número: "))
pq = n * 2
pc = n * 3
r = n ** (1/2)
print("O dobro desse núnero é: {}\nO triplo é: {}\nE a raiz quadrada é: {:.3f}".format(pq, pc, r))

#Desafio 007 - Calcular a média

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
media = (nota1 + nota2) / 2
print("A sua média foi: ", media)

#Desafio 008 - Converter de metros para kilômtros, centímetros e milímetros

metros = float(input("Digite uma distância em metros: "))
kilometros = metros / 1000
centimetros = metros * 100
milimetros = metros * 1000
print("A distância em centímetros é: {}\nEm milímetros é: {}\nE em kilômetros é: {}".format(centimetros, milimetros, kilometros))

#Desafio 009 - Tabuadas

numero = int(input("Digite um número: "))
tabuada = numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10
print("A tabuada de multiplicação desse número é", tabuada)

#Ou (forma bonitinha que o Guanabara fez)

tab = int(input("Dgite um número para ver a sua tabuada: "))
print("{} x {} = {}".format(tab, 1, tab*1))
print("{} x {} = {}".format(tab, 2, tab*2))
print("{} x {} = {}".format(tab, 3, tab*3))
print("{} x {} = {}".format(tab, 4, tab*4))
print("{} x {} = {}".format(tab, 5, tab*5))
print("{} x {} = {}".format(tab, 6, tab*6))
print("{} x {} = {}".format(tab, 7, tab*7))
print("{} x {} = {}".format(tab, 8, tab*8))
print("{} x {} = {}".format(tab, 9, tab*9))
print("{} x {} = {}".format(tab, 10, tab*10))

#Desafio 010 - Conversão de real para dólar

real = float(input("Quanto reais você tem? R$"))
dolar = real / 5.01
print("Seu dinheiro vale {:.2f} de dólares!".format(dolar))

#Desafio 011 - Calcular áreas, e saber quanto vai gastar de tinta (cada litro pinta 2m²)

largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura dessa parede? "))
area1 = largura * altura
print("A área dessa parede é de: {:.2f} m²".format(area1))
tinta = area1 / 2
print("Portanto, vai se gastar {:.2f} litros de tinta para cada metro quadrado!".format(tinta))

#Desafio 012 - Calcular desconto em porcentagem

preço = float(input("Qual o preço desse produto? R$"))
print("Este produto tem 5 porcento de desconto!")
desc = preço * 0.05
preçof = preço - desc
print("Portanto, o novo valor desse produto com desconto é de: {:.2f}R$".format(preçof))

#Desafio 013 - Calcular aumento em porcentagem

salario = float(input("Quanto você recebe de salário? "))
print("Seu salário terá um aumento de 15%")
aum = salario * 0.15
salariof = salario + aum
print("Portanto,seu novo salário será de {:.2f} reais!".format(salariof))
