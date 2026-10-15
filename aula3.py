"""Python é uma linguagem de programação com tipagem dinamica e forte
str -> string -> texto
Strings são textos que estao dentro de aspas simples ou duplas"""

# Aspas simples
print('Matheus Goes')
print(1, 'Matheus "Goes"')

#Aspas duplas
print("Matheus Goes")
print(2, "Matheus 'Goes'")

#Escape
print("Matheus \"Goes\"") # O \ pula oara o proximo caractere, nesse caso ele pula para o " e nao fecha a string

# r
print(r"Matheus \"Goes\"") # O r antes da string faz com que o \ seja ignorado, ou seja, ele nao pula para o proximo caractere