def foreing_exchange_calculator(ammount):
    mex_to_col_rate = 145.97
    return mex_to_col_rate * ammount

def run():
    print('CALCULADORA DE AMOR')
    print('Convierte tu cariño al cariño de tu novio.')
    print('')

    ammount = float(input('Ingresa la cantidad de cariño que le tienes a tu novio: '))

    result = foreing_exchange_calculator(ammount)

    final_exchange = round(result, 2)

    print('{} unidades de amor de Zai es {} amor de Dalai'.format(ammount, final_exchange))
    print('')
if __name__ == '__main__':
    run()