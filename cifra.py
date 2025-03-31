# importando a função 'sys', que permite a manipulação do sistema
import sys

# importando a função 'unidecode', que permite remover acentos das letras
        # como por exemplo: é = e
from unidecode import unidecode

# imprimindo linhas e uma mensagem que marca o início do código da cifra de césar
print('--------------------------------------------'
      '\nIniciando Cifra de César'
      '\n--------------------------------------------')

# atribuindo um valor para a variável 'mensagem', que o próprio usuário insere
# a função 'lower()' serve para que todos os caracteres se padronizem, fazendo com que sejam apenas letras minúsculas
mensagem = input('Insira uma frase: ').lower()

# crio uma condição de erro
try:

    # atribuindo o valor inserido pelo usuário para a variável 'deslocamento', já que ela será a responsável por delimitar quantos caracteres serão pulados
            # e o valor deve ser lido como número inteiro
    deslocamento = int(input('Deslocamento: '))

    # se o valor atribuído ao deslocamento for maior do que 25
    if deslocamento > 25:
        # uma mensagem de erro será impressa, solicitando que o valor inserido seja entre 0 e 25, e que o programa será encerrado
        print('--------------------------------------------'
              '\nErro. Por favor, insira um número entre 0 e 25.'
              '\n--------------------------------------------'
              '\nEncerrando programa.')
        # saindo do sistema, ou seja, encerrando-o
        sys.exit()

# se o usuário inserir algo que não seja um número
except ValueError:

    # uma mensagem de erro será impressa
    print('Por favor, insira um número. Encerrando programa.')
    # saindo do sistema, ou seja, encerrando-o
    sys.exit()
    
# perguntando ao usuário se o deslocamento será positivo ou negativo, atribuindo a resposta para a variável 'modo'
        # a função 'strip()' retira os espaços antes e depois da resposta
        # a função 'lower()' faz com que os caracteres sejam apenas letras minúsculas
modo = input('Positivo ou negativo? (p/n) ').strip().lower()

# atribuindo um valor vazio para a variável 'mensagem_cifrada', que será usada posteriormente
mensagem_cifrada = ""

# se a resposta do usuário for 'n'
if modo == 'n':
    # o deslocamento passará a ser negativo
    deslocamento = -deslocamento

# a variável 'mensagem_s_acento' armazena a transformação da variável 'mensagem' para uma frase livre de acentos, com a função importada da 'unidecode()'
mensagem_s_acento = unidecode(mensagem)

# para cada letra presente na variável 'mensagem_s_acento'
for letra in mensagem_s_acento:
    # se a letra estiver entre 'a' e 'z'
        # garantindo que apenas as letras do alfabeto sejam modificadas pela cifra (com os espaços mantidos)
    if 'a' <= letra <= 'z':
        # converto a letra para um número, e acrescento o valor atribuído pelo usuário na variável 'deslocamento', armazenando na nova variável 'numero'
        numero = ord(letra) + deslocamento

        # se o número for maior do que o número de 'z'
        if numero > ord('z'):
            # subtrai 26 caracteres, voltando para o início do alfabeto
            numero -= 26

        # a variável 'nova_letra' armazena as letras convertidas, que antes eram números, ou seja, transformo-as em alfabeto novamente
        nova_letra = chr(numero)

        # adiciono a 'nova_letra' na variável 'mensagem_cifrada', antes vazia
        mensagem_cifrada += nova_letra
            
    else:
        # se o caracter não for uma letra (tipo espaços e números), ele adiciona automaticamente na 'mensagem_cifrada'
        mensagem_cifrada += letra

# imprimindo uma mensagem final, que exibe a mensagem original e a mensagem codificada pela cifra de césar
print(f'--------------------------------------------'
      f'\nEntrada: {mensagem}'
      f'\nSaída: {mensagem_cifrada}') 
