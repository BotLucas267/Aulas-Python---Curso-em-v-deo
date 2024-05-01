#Desafio 3 e Exercício 3

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
print('A soma entre o primeiro valor:', numero1,' e o segundo valor:', numero2, 'é igual a:', numero1 + numero2 )
#ou
print("A soma entre {} e {}, é igual a: {}" .format (numero1, numero2, numero1 + numero2))

#Desafio 3 pt2 e exercício 4

d = (input("Digite algo: "))
print('O tipo é:', type(d))
print('È alfanuméricp',d.isalnum)
print('É alfabético?', d.isalpha)
print('É numérico?', d.isnumeric)

#O intuito é dissecar os dados atribuídos a variável, por algum motivo, o VS code não mostrou os resultados, que deviam ser booleanos.
