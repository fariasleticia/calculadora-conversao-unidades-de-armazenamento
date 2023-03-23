CONSTANTE_BASE_CONVERSÃO = 1024

def converterStringParaFloat(value):
    print('Valor convertido de string para float')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido de byte para bit:')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

print('Insira o valor a ser convertido:')
entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)

print(valorConvertido)