import sys
from unidecode import unidecode

print('--------------------------------------------'
        '\nIniciando Cifra de César'
        '\n--------------------------------------------')
mensagem = input('Insira uma frase: ').lower()

try:
    deslocamento = int(input('Deslocamento: '))

    if deslocamento > 25:
        print('--------------------------------------------'
                '\nPor favor, insira um número entre 0 e 25.'
                '\n--------------------------------------------'
                '\nEncerrando programa.')
        sys.exit()
except ValueError:
    print('Por favor, insira um número.')
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