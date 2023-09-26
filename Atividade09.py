#Exercício 09 - Crie uma aplicação que solicita ao usuário que digite um texto e imprima no console o texto digitado pelo usuário sem nenhuma vogal.

def remover_vogais(texto):
    vogais = "aeiouAEIOU"
    texto_sem_vogais = ''.join([letra for letra in texto if letra not in vogais])
    return texto_sem_vogais
texto_usuario = input("Digite um texto: ")
texto_sem_vogais = remover_vogais(texto_usuario)
print("Texto sem vogais:", texto_sem_vogais)
