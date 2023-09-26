#Exercício 01 - Crie uma função que solicite ao usuário digitar uma palavra e substitua as vogais por "*" e a execute numa aplucação
# que solicite uma palavra ao usuário e imprima o resultado no console, independentemente do usuário digitar a palavra em maiúscula ou minúscula.

def substituir_vogais_por_asteriscos(palavra):
    palavra = palavra.lower()
    vogais = ['a', 'e', 'i', 'o', 'u']
    palavra_com_asteriscos = ''
    for letra in palavra:
        if letra in vogais:
            palavra_com_asteriscos += '*'
        else:
            palavra_com_asteriscos += letra
    return palavra_com_asteriscos
palavra_usuario = input("Digite uma palavra: ")
resultado = substituir_vogais_por_asteriscos(palavra_usuario)
print("Palavra com vogais substituídas por asteriscos:", resultado)