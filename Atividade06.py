#Exercício 06 - Crie uma aplicação que solicite ao usuário digitar o seu nome e sobrenome e imprima no console o nome com todas as
# letras maiúsculas e o sobrenome com todas as letras minúsculas sem espaços entre o nome e o sobrenome e sem alterar a variável original.

nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")

nome_maiusculo = nome.upper()
sobrenome_minusculo = sobrenome.lower()

nome_completo = nome_maiusculo + sobrenome_minusculo

print("Nome completo formatado:", nome_completo)
