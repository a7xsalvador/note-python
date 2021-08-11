def run_note():
    print('ingresa la nota')
    nota = str(input())
        print('quieres guardar la nota?')

def run():
    print('0 para salir')
    print('1 para ingresar una nota ')
    opcion = int(input('selecciona el numero '))

    if opcion == 0 :
        print('chao')
        exit()
    elif opcion == 1:
        run_note()


if __name__=='__main__':
    run()