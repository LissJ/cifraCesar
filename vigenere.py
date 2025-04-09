# criando um alfabeto local completo, com 92 caracteres, para realizar a cifra de vigenere
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0123456789!@#$%&*()-_=+{}[],.<>:;/?\\|\"'"

# a variável 'modo' armazenará a informação se o usuário deseja codificar ou decodificar
modo = input('Você deseja codificar ou decodificar? (c/d) ')

# a variável 'mensagem' armazenará a mensagem inserida pelo usuário
mensagem = input('Insira a mensagem: ')

# a variável 'chave' armazenará a mensagem inserida pelo usuário
chave = input('Insira a chave: ')

# variável que armazena a chave com a mesma quantidade de caracteres que a mensagem que o usuário escreveu
chave_expandida = ''

# variável que armazena um contador que irá informar qual letra da chave usar a cada passo
indice = 0

# se a pessoa decidir codificar
if modo == 'c':
    # para cada caractere em mensagem
    for caractere in mensagem:
        # se o caractere estiver dentro do alfabeto local
        if caractere in alfabeto:
            # pega a letra certa da chave (com a repetição automática se acabar)
                # e adiciona isso na 'chave_expandida', que agora terá o mesmo tamanho da mensagem no final
            chave_expandida += chave[indice % len(chave)]
            # adiciona mais um número no contador
                # que fará com que passe para a próxima letra
            indice += 1
        # caso o caractere não esteja no alfabeto local
        else:
            # esse caractere só vai ser adicionado direto em 'chave_expandida'
            chave_expandida += caractere

    # variável vazia que irá armazenar a mensagem cifrada depois
    mensagem_codificada = ''

    # para cada letra da mensagem, esse 'for' irá percorrer sua posição
        # como por exemplo: 'amor'
                        #   range(4)
                        #   (0, 1, 2, 3)
    for i in range(len(mensagem)):
        # pegando uma letra da mensagem com base na posição dela
        caractere = mensagem[i]

        # se o caractere estiver presente no alfabeto local
        if caractere in alfabeto:
            # encontrando a posição desse caractere dentro do alfabeto local
            pos = alfabeto.index(caractere)
            # fazendo o mesmo para cada letra da 'chave_expandida' (a chave que foi expandida previamente)
            pos_chave = alfabeto.index(chave_expandida[i])
            # somando a posição da letra da mensagem com a posição da letra da chave
                # utilizando o módulo para dar a volta no alfabeto e reiniciar, caso ele atinja o final
            nova_pos = (pos + pos_chave) % len(alfabeto)
            # pegando a letra da nova posição calculada e adicionando na variável 'mensagem_codificada'
            mensagem_codificada += alfabeto[nova_pos]
        # se não estiver no alfabeto local
        else:
            # apenas adicionar o caractere na 'mensagem_codificada' direto 
            mensagem_codificada += caractere

    # imprimindo a mensagem já codificada
    print('-------------------------------------------------------'
          '\nMensagem codificada:\n', mensagem_codificada)

# se a pessoa decidir decodificar
elif modo == 'd':
    # para cada caractere em mensagem
    for caractere in mensagem:
        # se o caractere estiver dentro do alfabeto local
        if caractere in alfabeto:
            # pega a letra certa da chave (com a repetição automática se acabar)
                # e adiciona isso na 'chave_expandida', que agora terá o mesmo tamanho da mensagem no final
            chave_expandida += chave[indice % len(chave)]
            # adiciona mais um número no contador
                # que fará com que passe para a próxima letra
            indice += 1
        # caso o caractere não esteja no alfabeto local
        else:
            # esse caractere só vai ser adicionado direto em 'chave_expandida'
            chave_expandida += caractere

    # variável vazia que irá armazenar a mensagem decifrada depois
    mensagem_decodificada = ''

    # para cada letra da mensagem, esse 'for' irá percorrer sua posição
    for i in range(len(mensagem)):
        # pegando uma letra da mensagem com base na posição dela
        caractere = mensagem[i]

        # se o caractere estiver presente no alfabeto local
        if caractere in alfabeto:
            # # encontrando a posição desse caractere dentro do alfabeto local
            pos = alfabeto.index(caractere)
            # fazendo o mesmo para cada letra da 'chave_expandida' (a chave que foi expandida previamente)
            pos_chave = alfabeto.index(chave_expandida[i])
            # subtraindo (oposto ao codificador) a posição da letra da mensagem com a posição da letra da chave
                # utilizando o módulo para dar a volta no alfabeto e reiniciar, caso ele atinja o final
            nova_pos = (pos - pos_chave) % len(alfabeto)
            # pegando a letra da nova posição calculada e adicionando na variável 'mensagem_codificada'
            mensagem_decodificada += alfabeto[nova_pos]
        # se não estiver no alfabeto local
        else:
            # apenas adicionar o caractere na 'mensagem_codificada' direto 
            mensagem_decodificada += caractere

    # imprimindo a mensagem decodificada
    print('-------------------------------------------------------'
          '\nMensagem decodificada:\n', mensagem_decodificada)

# caso o usuário não tenha digitado nenhuma das duas opções
else:
    # imprimindo um aviso de que a opção não existe
    print('Opção inválida.')