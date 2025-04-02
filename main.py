# criando uma variável que armazena todos os caracteres presentes na b64, que será utilizado para mapear os números dos caracteres
tabela_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# # atribuindo um valor para a variável 'mensagem', que o próprio usuário insere
mensagem = input('Insira uma frase: ')

modo = input("Você quer codificar ou decodificar? (c/d): ").strip().lower()

# atribuindo o valor inserido pelo usuário para a variável 'deslocamento', já que ela será a responsável por delimitar quantos caracteres serão pulados
    # e o valor deve ser lido como número inteiro
deslocamento = int(input('Deslocamento: '))

sinal = input("O deslocamento é positivo ou negativo? (+/-): ").strip()
if sinal == "-":
    deslocamento = -deslocamento

# atribuindo um valor vazio para a variável 'mensagem_cifrada', que será usada posteriormente
# mensagem_cifrada = ""

'''# cada caractere 'c' presente em 'mensagem' está sendo transformado em um número 'ASCII' com a função 'ord()'
    # a partir disso, eles vão passar pela transformação em binário de 8 bits, ':08b'
        # e por fim, a função '"".join()' é responsável por agrupar tudo em uma única string'''

if modo == "c":
    # Primeiro, aplica Base64
    binario = "".join(f"{ord(c):08b}" for c in mensagem)
    blocos = [binario[i:i+6] for i in range(0, len(binario), 6)]
    if len(blocos[-1]) < 6:
        blocos[-1] = blocos[-1].ljust(6, "0")
    indices = [int(b, 2) for b in blocos]
    mensagem_base64 = "".join(tabela_base64[i] for i in indices)
    
    while len(mensagem_base64) % 4 != 0:
        mensagem_base64 += "="
    
    print("Texto em Base64:\n", mensagem_base64)

    # Depois, aplica a Cifra de César
    mensagem_cifrada = ""
    for letra in mensagem_base64:
        if letra in tabela_base64:
            posicao = tabela_base64.index(letra)
            nova_posicao = (posicao + deslocamento) % 64
            nova_letra = tabela_base64[nova_posicao]
            mensagem_cifrada += nova_letra
        else:
            mensagem_cifrada += letra

    print("Texto Base64 cifrado:\n", mensagem_cifrada)

if modo == "d":
    # Aplica a Cifra de César antes de decodificar Base64
    mensagem_decifrada = ""
    for letra in mensagem:
        if letra in tabela_base64:
            posicao = tabela_base64.index(letra)
            nova_posicao = (posicao - deslocamento) % 64  # Inverte a Cifra de César corretamente
            nova_letra = tabela_base64[nova_posicao]
            mensagem_decifrada += nova_letra
        else:
            mensagem_decifrada += letra

    print("Texto Base64 decifrado:\n", mensagem_decifrada)

    # Agora, remove o padding e converte Base64 para texto original
    decifrado = mensagem_decifrada.rstrip("=")  # Remove '=' antes de converter
    valores = [tabela_base64.index(c) for c in decifrado]
    binario = "".join(f"{v:06b}" for v in valores)
    blocos = [binario[i:i+8] for i in range(0, len(binario), 8)]
    texto_original = "".join(chr(int(b, 2)) for b in blocos)

    print("Texto original:\n", texto_original)