# EX1
# Um aluno tem 10 anos. Armazene essa idade em uma variável
# e exiba seu tipo.

idade = 10
print(type(idade))

# EX2
# A temperatura medida é 23.5°C.
# Armazene esse valor e mostre seu tipo.
temp = 23.5
print(type(temp))

# EX3
# Crie um número complexo representando uma impedância elétrica
# de 5 + 8j e mostre sua parte real.
numero_complexo = 5 + 8j
print("Valor:", numero_complexo)
print("Tipo", type(numero_complexo))

# EX4
# Mostre a parte imaginária do número complexo
# criado no exercício anterior.

print("Parte imaginária:", numero_complexo)

# EX5
# Declare uma variável chamada "populacao"
# com o valor 8_000_000_000 (8 bilhões)
# e mostre seu tipo.
populacao = 8_000_000_000
print("Tipo da populacao:", type(populacao))

# EX6
# Verifique se o número 7 é do tipo int
# usando a função type().
print(type(7) == int)

# EX7
# Crie uma variável chamada "aprovado"
# com o valor booleano True e mostre seu tipo.
aprovado = True
print(type(aprovado))

# EX8
resultado_soma = True + False
print("Resultado:", resultado_soma)
print("Tipo:", type(resultado_soma))

# EX9
# Mas podemos exibir o tamanho máximo suportado pela arquitetura nativa (sys.maxsize).
import sys
print("Limite nativo da arquitetura:", sys.maxsize)

# EX10
print(bin(10))


