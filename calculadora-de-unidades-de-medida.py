CONSTANTE_BASE_CONVERSÃO = 1024

#funções de conversão:

def converterStringParaFloat(valor):
    print('Valor convertido de string para float.')
    return float(valor)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte:')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit:')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def byteParaKByte(valorASerConvertido):
    print('Valor convertido de byte para quilobyte:')
    Kbytes1Calculado = valorASerConvertido / CONSTANTE_BASE_CONVERSÃO
    return Kbytes1Calculado

def kbyteParaByte(valorASerConvertido):
    print('Valor convertido de quilobyte para byte:')
    bytes2Calculado = valorASerConvertido * CONSTANTE_BASE_CONVERSÃO
    return bytes2Calculado

def kbyteParaMByte(valorASerConvertido):
    print('Valor convertido de byte para quilobyte:')
    kbytes2Calculado = valorASerConvertido / CONSTANTE_BASE_CONVERSÃO
    return kbytes2Calculado

def mbyteParaKbyte(valorASerConvertido):
    print('Valor convertido de quilobyte para byte:')
    mbytes1Calculado = valorASerConvertido * CONSTANTE_BASE_CONVERSÃO
    return mbytes1Calculado

#prints das conversões acima:

print('Insira o valor a ser convertido (byte para bit):')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
print(valorConvertido)

print('Insira o valor a ser convertido (bit para byte):')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido2 = bitParaByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido2)

print('Insira o valor a ser convertido (byte para quilobyte):')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido3 = byteParaKByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido3)

print('Insira o valor a ser convertido (quilobyte para byte):')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido4 = kbyteParaByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido4)

print('Insira o valor a ser convertido (quilobyte para megabyte):')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido5 = kbyteParaMByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido5)

print('Insira o valor a ser convertido (megabyte para quilobyte):')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido6 = mbyteParaKbyte(entradaDoTecladoValorASerConvertido)
print(valorConvertido6)