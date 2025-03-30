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

    # atribuo o valor inserido pelo usuário para a variável 'deslocamento', já que ela será a responsável por delimitar quantos caracteres serão pulados
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
    
modo = input('Positivo ou negativo? (p/n) ').strip().lower()
mensagem_cifrada = ""

if modo == 'n':
    deslocamento = -deslocamento

mensagem_s_acento = unidecode(mensagem)

for letra in mensagem_s_acento:
    if 'a' <= letra <= 'z':
        numero = ord(letra) + deslocamento

        if numero > ord('z'):
            numero -= 26

        nova_letra = chr(numero)
        mensagem_cifrada += nova_letra
    else:
        mensagem_cifrada += letra

print(f'--------------------------------------------'
      f'\nEntrada: {mensagem}'
      f'\nSaída: {mensagem_cifrada}') 
