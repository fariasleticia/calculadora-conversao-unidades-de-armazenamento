from calculo_da_conversao_das_unidades_de_armazenamento import converterStringParaFloat, bitParaByte, byteParaBit, byteParaKByte, kbyteParaByte, kbyteParaMByte, mbyteParaKbyte, mbyteParaGByte, gbyteParaMbyte, gbyteParaTByte, tbyteParaGbyte, tbyteParaPByte, pbyteParaTbyte  

print ('- Insira 1 para converter de Bit (b) para Byte (B)\n- Insira 2 para converter de Byte (B) para Bit (b)\n- Insira 3 para converter de Byte (B) para Quilobyte (KB)\n- Insira 4 para converter de Quilobyte (KB) para Byte (B)\n- Insira 5 para converter de Quilobyte (KB) para Megabyte (MB)\n- Insira 6 para converter de Megabyte (MB) para Quilobyte (KB)\n- Insira 7 para converter de Megabyte (MB) para Gigabyte (GB)\n- Insira 8 para converter de Gigabyte (GB) para Megabyte (MB)\n- Insira 9 para converter de Gigabyte (GB) para Terabyte (TB)\n- Insira 10 para converter de Terabyte (TB) para Gigabyte (GB)\n- Insira 11 para converter de Terabyte (TB) para Petabyte (PB)\n- Insira 12 para converter de Petabyte (PB) para Terabyte (TB)')

funcEscolha = input()

if(funcEscolha == '1'):
    print('\nInsira o valor a ser convertido (byte para bit):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido = byteParaBit(entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    print('\nInsira o valor a ser convertido (bit para byte):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido2 = bitParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido2)

elif(funcEscolha == '3'):
    print('\nInsira o valor a ser convertido (byte para quilobyte):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido3 = byteParaKByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido3)

elif(funcEscolha == '4'):
    print('\nInsira o valor a ser convertido (quilobyte para byte):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido4 = kbyteParaByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido4)

elif(funcEscolha == '5'):
    print('\nInsira o valor a ser convertido (quilobyte para megabyte):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido5 = kbyteParaMByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido5)

elif(funcEscolha == '6'):
    print('\nInsira o valor a ser convertido (megabyte para quilobyte):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido6 = mbyteParaKbyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido6)

elif(funcEscolha == '7'):
    print('\nInsira o valor a ser convertido (megabyte para gigabyte):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido7 = mbyteParaGByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido7)

elif(funcEscolha == '8'):
    print('\nInsira o valor a ser convertido (gigabyte para megabyte):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido8 = gbyteParaMbyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido8)

elif(funcEscolha == '9'):
    print('\nInsira o valor a ser convertido (gigabyte para terabyte):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido9 = gbyteParaTByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido9)

elif(funcEscolha == '10'):
    print('\nInsira o valor a ser convertido (terabyte para gigabyte):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido10 = tbyteParaGbyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido10)

elif(funcEscolha == '11'):
    print('\nInsira o valor a ser convertido (terabyte para petabyte):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido11 = tbyteParaPByte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido11)

elif(funcEscolha == '12'):
    print('\nInsira o valor a ser convertido (petabyte para terabyte):')
    entradaDoTecladoValorASerConvertido  = converterStringParaFloat(input())
    valorConvertido12 = pbyteParaTbyte(entradaDoTecladoValorASerConvertido)
    print(valorConvertido12)
