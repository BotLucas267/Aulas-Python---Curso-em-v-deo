#Exercício 014 - Converter graus Celsius em graus Fahrenheit

temp = float(input("Digite uma temperatura em °C: "))
f = temp * 1.8 + 32
print("A temperatura de {}°C, é equivalente a {}°F".format(temp, f))

#Exercício 015 - Calcular o aluguel de um carro por dias, e Km rodados

km = float(input("Quantos kilômetros o carro alugado percorreu? "))
dias = int(input("Por quantos dias esse carro foi alugado? "))
AluguelpDia = 60 * dias
preçokm = 0.15 * km
total = AluguelpDia + preçokm
print("O valor total do aluguel do carro foi de {:.2f}R$".format(total))
