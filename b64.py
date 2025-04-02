def codificar_base64(texto):
    ascii_vals = [ord(c) for c in texto]

    binarios = [bin(n)[2:].zfill(8) for n in ascii_vals]

    binario_completo = "".join(binarios)
    
    blocos = [binario_completo[i:i+6] for i in range(0, len(binario_completo), 6)]

    blocos[-1] = blocos[-1].ljust(6, "0")

    valores = [int(b, 2) for b in blocos]
    
    tabela_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_codificado = [tabela_base64[v] for v in valores]

    while len(base64_codificado) % 4 != 0:
        base64_codificado.append('=')
    
    return ''.join(base64_codificado)

def descodificar_base64(base64_texto):

    base64_texto = base64_texto.rstrip("=")

    tabela_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    valores = [tabela_base64.index(c) for c in base64_texto]

    binario_completo = "".join([bin(v)[2:].zfill(6) for v in valores])

    blocos_8bits = [binario_completo[i:i+8] for i in range(0, len(binario_completo), 8)]

    texto_original = "".join([chr(int(b, 2)) for b in blocos_8bits])
    
    return texto_original