#1 - Crie uma lista para cada informação a seguir: Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

numeros_1a10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_impares = [1, 3, 5, 7, 9, 11, 13]
nomes = ['Marcos', 'Pedro', 'Breno', 'Matheus']

for numero in numeros_1a10:
    print(numero)
 
for nome in nomes:
    print(f" - {nome}")

# soma dos valores impares

soma1 = 0 #calculando os números de 1 a 10
for i in range(1, 11):
        soma1 += i

print(f"Aqui a soma dos valores de 1 a 10: {soma1}")

soma_par = 0 #soma de valor par
for i in range(2,11,2):
    #  if i % 2 == 0:       ESSA PARTE DO CÓDIGO FICA DESNECESSÁRIA PORQUE JA FAÇO A VALIDAÇÃO DE PAR NO RANGE
          soma_par += i

print(f"Aqui temos os valores pares somados: {soma_par} ")



soma_impar = 0 #soma de valor impar 
for i in range(1, 11, 2):
        soma_impar += i
    
print(f"Aqui são os valores impares: {soma_impar} ")

print("Os valores na ordem descrescente: ")
descrescente = 0 #Imprimir os números em ordem decrescente
for i in range(10, 0, -1):
    print(i)

numero_multi = int(input("Digite um número que vamos multiplicar: "))

for i in range(1,11):
        resutlado = numero_multi * i
        print(f"{numero_multi}^2 = {resutlado}")# nao consigo mostrar todos os valores de 1 a 10, só mostro 10 vezes o mesmoresultado