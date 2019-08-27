
def getMCD(numbOne,numTwo):
    if numbOne % numTwo == 0:
        return numTwo
    return getMCD(numTwo, numbOne % numTwo )

def begin():
    try:
        numbOne = int(input('Primer Número: '))
        numTwo = int(input('segundo Número: '))
        print('El MCD de %i y %i es = %i'%(numbOne, numTwo, getMCD(numbOne,numTwo)))    
    except:
        print('Error en la entrada de datos')

if __name__ == '__main__':
    begin()