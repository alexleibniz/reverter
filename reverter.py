# Definindo a string
string = "Olá, mundo!"

# Convertendo a string em uma lista
lista_caracteres = list(string)

# Obtendo o número de caracteres da string
n_caracteres = len(lista_caracteres)

# Invertendo a ordem dos caracteres da lista
for i in range(n_caracteres//2):
    lista_caracteres[i], lista_caracteres[n_caracteres-1-i] = lista_caracteres[n_caracteres-1-i], lista_caracteres[i]

# Convertendo a lista de volta para string
string_invertida = "".join(lista_caracteres)

# Imprimindo a string invertida
print(string_invertida)
