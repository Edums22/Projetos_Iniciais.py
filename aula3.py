primeiro_valor = input('Digite Um Valor: ')
segundo_valor = input('Digite Outro Valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} é maior '
        f'do que {segundo_valor=}'   
    )
else:
    print(f'{segundo_valor=}é maior do que '
          f'do que {primeiro_valor=}')