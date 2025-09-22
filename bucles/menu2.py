
# Utilizamos una variable tipo Booleana -> una bandera
control = True

while True:
    print('1. Entradas\n2. Platos fuertes\n3. Bebidas\n4. Postres\n5. Salir\n')
    opcion = int(input('Elija una opcion: '))
    match opcion:
        case 1:
            print('1. Patacon con hogao')
            print('2. Yuca con chicharrón')
            print('3. yuca con queso')
        case 2:
            print('1. Solomito')
            print('2. Hamburguesa')
            print('3. Suchi')
        case 3:
            print('1. Coca cola')
            print('2. Jugos natural')
            print('3. Cervezas')
        case 4:
            print('1. Tarta de chocolate')
            print('2. El cheesecake')
            print('3. Frutas frescas con crema')
        case 5:
            break
        case _:
            print('Opcion invalida')
