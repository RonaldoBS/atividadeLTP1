#Exercício 08 - Crie um programa que solicite apresenta um menu de opções no Console e solicite ao usuário que digite a opção desejada. Em seguida, crie uma função para cada opção do menu que execute a ação solicitada pelo usuário. O menu deve conter as seguintes opções:

#1. Conte o número total de palavras digitadas.
#2. Conte o número de vogais na palavra digitada (ignore maiúsculas/minúsculas, ou seja, "Python" e "python" devem ser contadas como iguais).
#3. Substitua todas as ocorrências da palavra "Python" por "Java".
#4. Converta todas as letras da string para minúsculas.
#5. Crie uma lista com todas as palavras únicas encontradas na string (ignorando maiúsculas/minúsculas).
#6. Imprima as palavras na string em ordem alfabética.


def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)


def contar_vogais(texto):
    texto = texto.lower()
    vogais = 'aeiou'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador


def substituir_python_por_java(texto):
    return texto.replace("Python", "Java")


def converter_para_minusculas(texto):
    return texto.lower()

def palavras_unicas(texto):
    palavras = texto.split()
    palavras_unicas = set(palavras)
    return list(palavras_unicas)


def ordem_alfabetica(texto):
    palavras = texto.split()
    palavras.sort(key=lambda x: x.lower())
    return palavras


def main():
    texto = input("Digite uma frase: ")

    while True:

        print("\nMenu de Opções:")
        print("1. Conte o número total de palavras digitadas.")
        print("2. Conte o número de vogais na palavra digitada.")
        print("3. Substitua todas as ocorrências da palavra 'Python' por 'Java'.")
        print("4. Converta todas as letras da string para minúsculas.")
        print("5. Crie uma lista com todas as palavras únicas na string.")
        print("6. Imprima as palavras na string em ordem alfabética.")
        print("0. Sair")


        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            print("Número total de palavras digitadas:", contar_palavras(texto))
        elif escolha == '2':
            print("Número de vogais na palavra digitada:", contar_vogais(texto))
        elif escolha == '3':
            texto = substituir_python_por_java(texto)
            print("Texto após a substituição:")
            print(texto)
        elif escolha == '4':
            texto = converter_para_minusculas(texto)
            print("Texto em minúsculas:")
            print(texto)
        elif escolha == '5':
            lista_palavras_unicas = palavras_unicas(texto)
            print("Lista de palavras únicas na string:")
            print(lista_palavras_unicas)
        elif escolha == '6':
            palavras_ordenadas = ordem_alfabetica(texto)
            print("Palavras na string em ordem alfabética:")
            print(" ".join(palavras_ordenadas))
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
