#Exercício 03 - Crie uma aplicação que solicite ao usuário digitar completo e
# imprima no console quantas vezes aparece a letra "a", independente de ser maiúscula ou minúscula.

nome_completo = input("Digite o seu nome completo: ")
nome_completo = nome_completo.lower()
quantidade_de_a = nome_completo.count('a')
print("A letra 'a' aparece", quantidade_de_a, "vezes no nome completo.")