#Exercício 07 - Crie uma aplicação em que o usuário digite o seu nome e sobrenome de uma só vez e armazene o nome em uma variável
# 'nome_usuário' e o sobrenome em uma variável 'sobrenome_usuario'. Em seguida, crie uma variável 'nome_completo' que armazene
# o nome completo do usuário com todas as letras maiúsculas e imprima no console o nome completo do usuário com todas as letras minúsculas.
# Além disso, crie outra variável chamada 'tamanho_nome_completo' que armazene o tamanho do nome completo
# do usuário e imprima no console o tamanho do nome completo do usuário.



nome_completo = input("Digite o seu nome completo: ")
nome_usuario, sobrenome_usuario = nome_completo.split()
nome_completo_maiusculo = nome_completo.upper()
tamanho_nome_completo = len(nome_completo)
print("Nome completo em minúsculas:", nome_completo)
print("Tamanho do nome completo:", tamanho_nome_completo)
