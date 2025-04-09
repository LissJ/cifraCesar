# criando variáveis com os alfabetos maiúsculo e minúsculo
maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculo = "abcdefghijklmnopqrstuvwxyz"

# pedindo ao usuário para inserir uma frase cifrada
mensagem = input("Digite a frase cifrada: ")

# fazendo um loop que vai de 1 até 25 (testando todos os deslocamentos possíveis, exceto 0, já que ele não muda nada)
for deslocamento in range(1, 26):
    # criando uma variável vazia para armazenar a mensagem decifrada com esse deslocamento
    decifrada = ""

    # para cada letra presente em 'mensagem'
    for letra in mensagem:
        # verificando se a letra está em algum dos alfabetos (maiúsculo ou minúsculo)
        if letra in maiusculo or letra in minusculo:
            # verificando se a letra é maiúscula
            if letra in maiusculo:
                # caso seja, o alfabeto maiúsculo será atribuído para a variável 'alfabeto'
                alfabeto = maiusculo
            else:
                # se não for, o alfabeto minúsculo será atribuído para a variável 'alfabeto'
                alfabeto = minusculo

            # encontrando a posição original da letra com a função 'index()'
            posicao = alfabeto.index(letra)
            # calculando a nova posição subtraindo o deslocamento, utilizando o módulo '% 26'
            nova_posicao = (posicao - deslocamento) % 26
            # adicionando a nova letra na mensagem decifrada
            decifrada += alfabeto[nova_posicao]
        else:
            # mantendo o caractere como estava originalmente, caso não seja uma letra
            decifrada += letra

    # exibindo o resultado do deslocamento atual
    print(f"\nDeslocamento {deslocamento}:\n{decifrada}")
