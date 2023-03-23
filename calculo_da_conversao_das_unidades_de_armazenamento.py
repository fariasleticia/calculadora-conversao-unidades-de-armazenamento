CONSTANTE_BASE_CONVERSÃO = 1024

def converterStringParaFloat(valor):
    return float(valor)

def bitParaByte(valorASerConvertido):
    print('Valor convertido:')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

def byteParaBit(valorASerConvertido):
    print('Valor convertido:')
    bitsCalculado = valorASerConvertido * 8
    return bitsCalculado

def byteParaKByte(valorASerConvertido):
    print('Valor convertido:')
    Kbytes1Calculado = valorASerConvertido / CONSTANTE_BASE_CONVERSÃO
    return Kbytes1Calculado

def kbyteParaByte(valorASerConvertido):
    print('Valor convertido:')
    bytes2Calculado = valorASerConvertido * CONSTANTE_BASE_CONVERSÃO
    return bytes2Calculado

def kbyteParaMByte(valorASerConvertido):
    print('Valor convertido:')
    kbytes2Calculado = valorASerConvertido / CONSTANTE_BASE_CONVERSÃO
    return kbytes2Calculado

def mbyteParaKbyte(valorASerConvertido):
    print('Valor convertido:')
    mbytes1Calculado = valorASerConvertido * CONSTANTE_BASE_CONVERSÃO
    return mbytes1Calculado

def mbyteParaGByte(valorASerConvertido):
    print('Valor convertido:')
    gbytes1Calculado = valorASerConvertido / CONSTANTE_BASE_CONVERSÃO
    return gbytes1Calculado

def gbyteParaMbyte(valorASerConvertido):
    print('Valor convertido:')
    mbytes2Calculado = valorASerConvertido * CONSTANTE_BASE_CONVERSÃO
    return mbytes2Calculado

def gbyteParaTByte(valorASerConvertido):
    print('Valor convertido:')
    tbytes1Calculado = valorASerConvertido / CONSTANTE_BASE_CONVERSÃO
    return tbytes1Calculado

def tbyteParaGbyte(valorASerConvertido):
    print('Valor convertido:')
    gbytes2Calculado = valorASerConvertido * CONSTANTE_BASE_CONVERSÃO
    return gbytes2Calculado

def tbyteParaPByte(valorASerConvertido):
    print('Valor convertido:')
    pbytesCalculado = valorASerConvertido / CONSTANTE_BASE_CONVERSÃO
    return pbytesCalculado

def pbyteParaTbyte(valorASerConvertido):
    print('Valor convertido:')
    tbytes2Calculado = valorASerConvertido * CONSTANTE_BASE_CONVERSÃO
    return tbytes2Calculado
