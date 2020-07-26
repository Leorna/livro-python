def box_print(symbol: str, width: int, height: int):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)

    for _ in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


for symbol, width, height in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(symbol, width, height)
    except Exception as error:
        print(f'An exception happened: {error}')