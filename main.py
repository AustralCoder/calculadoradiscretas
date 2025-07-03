def factorial(n):

    res_factorial = 1
    for i in range(1, n + 1):
        res_factorial = res_factorial * i
    return res_factorial


def variacion_no_rep(n, r):
    n_fact = factorial(n)
    n_menos_r = factorial(n - r)

    resultado = n_fact / n_menos_r

    return resultado


bandera = 1

while bandera == 1:
    try:
        opcion = int(input("Ingrese una opción:\n1 - Permutación\n2 - variacion sin repetición\n3 - salir\nUsted elige opción: "))
        print("Okay")
        if opcion == 1:

            valor = int(input("Ingrese el valor que desea permutar: "))
            if valor > 0:
                resultado = factorial(valor)
                print(f"{valor} se puede permutar de {resultado} formas")
            elif valor == 0:
                print("Factorial de 0 es 1")
            else:
                print("Indefinido: intente con un valor mayor a 0")

        elif opcion == 2:

            valor_n = int(input("Ingrese el valor n: "))
            valor_r = int(input("Ingrese el valor de r: "))

            if valor_n > valor_r:

                resultado = variacion_no_rep(valor_n, valor_r)
                print(f"{valor_n} de {valor_r} se puede variar {int(resultado)} veces ")
            else:
                print("R no puede ser mayor que N")



        elif opcion == 3:
            print("Hasta pronto!")
            break
        else:
            print("Ingrese un valor del 1 al 3")


        try:
            continuar = int(input("Desea continuar? Ingrese 1 para seguir o ingrese 0 para salir del programa: "))

            if continuar == 1:
                bandera = 1
            elif continuar == 0:
                print("Hasta Pronto!")
                bandera = 0
            else:
                print("---------------- Valor fuera de rango vuelva a intentar ---------------- ")

        except ValueError:
            print("---------------- ERROR: solo ingrese 1 o 0 ----------------")

    except ValueError:
        print("---------------- ERROR: Ingrese un valor numerico del 1 al 3 ----------------")
