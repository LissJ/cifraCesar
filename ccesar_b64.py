# criando uma variável que armazena todos os caracteres presentes na b64, que será utilizado para mapear os números dos caracteres
tabela_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# solicitando que o usuário digite uma frase e armazenando o valor na variável 'mensagem'
mensagem = input('Insira uma frase: ')

# solicitando ao usuário se ele deseja codificar ou decodificar e armazenando em letras minúsculas na variável 'modo'
modo = input("Você quer codificar ou decodificar? (c/d): ").strip().lower()

# solicitando ao usuário o valor do deslocamento e convertendo a resposta para número inteiro
deslocamento = int(input('Deslocamento: '))

# perguntando ao usuário se o deslocamento é positivo ou negativo, armazenando o sinal na variável 'sinal'
sinal = input("O deslocamento é positivo ou negativo? (+/-): ").strip()

# verificando se o sinal é negativo, e invertendo o valor do deslocamento se for o caso
if sinal == "-":
    deslocamento = -deslocamento

# verifica se o modo escolhido é de codificação
if modo == "c":
    # transforma cada caractere da 'mensagem' em código ASCII com ord()
        # depois converte esse número para binário de 8 bits com zeros à esquerda usando :08b
            # por fim, junta tudo em uma única string binária com "".join()
    binario = "".join(f"{ord(c):08b}" for c in mensagem)

    # divide a string binária em blocos de 6 bits, que é o padrão do Base64
    blocos = [binario[i:i+6] for i in range(0, len(binario), 6)]

    # verifica se o último bloco tem menos de 6 bits, e completa com zeros à direita se necessário
    if len(blocos[-1]) < 6:
        # 'ljust' é uma função que tem como objetivo preencher os espaços vazios com o caractere especificado, até que o texto tenha um total de 6 caracteres
        # o [-1] seleciona o último bloco da lista, pra verificar se ele tem 6 bits, e caso não tenha, ele aplica a função 'ljust'
        blocos[-1] = blocos[-1].ljust(6, "0")

    # converte cada bloco binário de 6 bits para número inteiro, base 2
        # cada bloco representa um número de 0 a 63 (faixa do Base64)
    indices = [int(b, 2) for b in blocos]

    # usa cada número (índice) para buscar o caractere correspondente na tabela_base64
        # monta a string codificada em Base64 com base nesses índices
    mensagem_base64 = "".join(tabela_base64[i] for i in indices)

    # enquanto o tamanho da string Base64 não for múltiplo de 4,
        # adiciona o caractere "=" no final, que é o padding usado pelo padrão Base64
    while len(mensagem_base64) % 4 != 0:
        mensagem_base64 += "="

    # exibe a mensagem convertida para base64
    print("Texto em Base64:\n", mensagem_base64)

    # inicializa a variável que vai conter o texto da cifra de césar
    mensagem_cifrada = ""

    # percorre cada letra da mensagem base64
    for letra in mensagem_base64:
        # verifica se a letra está presente na tabela base64
        if letra in tabela_base64:
            # pega o índice da letra na tabela
            posicao = tabela_base64.index(letra)
            # aplica o deslocamento informado pelo usuário
                # utilizando o método 'módulo 64', para que o resultado da posição sempre fique dentro de 64 caracteres (base64)
            nova_posicao = (posicao + deslocamento) % 64
            # pega a nova letra da tabela com a posição deslocada
            nova_letra = tabela_base64[nova_posicao]
            # adiciona a nova letra à mensagem cifrada
            mensagem_cifrada += nova_letra
        else:
            # se o caractere não está na tabela (como '='), adiciona ele direto
            mensagem_cifrada += letra

    # exibe a mensagem base64 após aplicar a cifra de césar
    print("Texto Base64 cifrado:\n", mensagem_cifrada)

# verifica se o modo escolhido é de decodificação
if modo == "d":
    # inicializa a variável que vai conter o texto decifrado da cifra de césar
    mensagem_decifrada = ""

    # percorre cada letra da mensagem digitada
    for letra in mensagem:
        # verifica se a letra está presente na tabela base64
        if letra in tabela_base64:
            # pega o índice da letra na tabela
            posicao = tabela_base64.index(letra)
            # aplica o deslocamento informado pelo usuário
                # utilizando o método 'módulo 64', para que o resultado da posição sempre fique dentro de 64 caracteres (base64)
            nova_posicao = (posicao + deslocamento) % 64
            # pega a nova letra da tabela com a posição deslocada
            nova_letra = tabela_base64[nova_posicao]
            # adiciona a nova letra à mensagem decifrada
            mensagem_decifrada += nova_letra
        else:
            # se o caractere não está na tabela (como '='), adiciona ele direto
            mensagem_decifrada += letra

    # exibe o texto após aplicar a cifra de césar
    print("Texto Base64 decifrado:\n", mensagem_decifrada)

    # remove os caracteres '=' do final da string, apenas para o cálculo dos bits
    mensagem_sem_padding = mensagem_decifrada.rstrip("=")

    # converte cada caractere base64 para seu índice correspondente na tabela
    valores = [tabela_base64.index(c) for c in mensagem_sem_padding]

    # transforma cada valor da lista 'valores' (que representa os caracteres em base64) em binário de 6 bits com zeros à esquerda,
        # e depois junta todos esses blocos em uma única string binária que representa toda a mensagem codificada
    binario = "".join(f"{v:06b}" for v in valores)

    # divide a string binária gigante em vários pedaços menores de 8 bits (bytes), que representam o caractere original
        # se i == 0, o binário será quebrado de 0 até 8 bits
        # se i == 8, o binário será quebrado de 8 até 16 bits
        # e assim por diante
            # e para cada i presente no alcance de
                # 0, que determina o início no primeiro caractere
                # até o tamanho da string binária (len(binario))
                # e pulando de 8 em 8 caracteres
                    # ou seja, a cada iteração que ocorre, ele pula 8 posições
    blocos = [binario[i:i+8] for i in range(0, len(binario), 8)]

    # converte cada bloco de 8 bits para um número decimal, depois para caractere ASCII, junstando todos os caracteres em uma string só
    texto_original = "".join(chr(int(b, 2)) for b in blocos)

    # exibe o texto original
    print("Texto original:\n", texto_original)
