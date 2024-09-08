import aritmetica

def test_sumar():
    errores = []
    try:
        assert round(aritmetica.sumar(1.234, 2.345), 2) == 3.58, \
            "1.234 + 2.345 debe ser aproximadamente 3.58"
    except AssertionError as error:
        errores.append(f"Error en la primera aserción: {error}")
    try:
        assert round(aritmetica.sumar(-1.0, 1.0), 2) == 0.00, \
            "-1.0 + 1.0 debe ser aproximadamente 0.00"
    except AssertionError as error:
        errores.append(f"Error en la segunda aserción: {error}")
    try:
        assert round(aritmetica.sumar(0, 0), 2) == 0.00, \
            "0 + 0 debe ser aproximadamente 0.00"
    except AssertionError as error:
        errores.append(f"Error en la tercera aserción: {error}")

    if errores:
        for error in errores:
            print(error)
    else:

        print("\n➤ test_sumar pasó sin errores.")
def test_restar():
    errores = []
    try:
        assert round(aritmetica.restar(5.5, 2.2), 2) == 3.30, \
            "5.5 - 2.2 debe ser aproximadamente 3.30"
    except AssertionError as error:
        errores.append(f"Error en la primera aserción: {error}")
    try:
        assert round(aritmetica.restar(1.0, 1.0), 2) == 0.00, \
            "1.0 - 1.0 debe ser aproximadamente 0.00"
    except AssertionError as error:
        errores.append(f"error en la segunda aserción: {error}")
    try:
        assert round(aritmetica.restar(0, 0), 2) == 0.00, \
            "0 - 0 debe ser aproximadamente 0.00"
    except AssertionError as error:
        errores.append(f"Error en la tercera aserción: {error}")

    if errores:
        for error in errores:
            print(error)
    else:
        print("\n➤ test_restar pasó sin errores.")

def test_dividir():
    errores = []
    try:
        assert round(aritmetica.dividir(10.0, 2.0), 2) == 5.00, \
            "10.0 / 2.0 debe ser aproximadamente 5.00"
    except AssertionError as error:
        errores.append(f"Error en la primera aserción: {error}")
    try:
        assert aritmetica.dividir(1.0, 0) == "Error: División por cero.", \
            "La división por cero debería devolver un mensaje de error"
    except AssertionError as error:
        errores.append(f"Error en la segunda aserción: {error}")
    try:
        assert round(aritmetica.dividir(0, 1.0), 2) == 0.00, \
            "0 / 1.0 debe ser aproximadamente 0.00"
    except AssertionError as error:
        errores.append(f"Error en la tercera aserción: {error}")

    if errores:
        for error in errores:
            print(error)
    else:
        print("\n➤ test_dividir pasó sin errores.")

def test_multiplicar():
    errores = []
    try:
        assert round(aritmetica.multiplicar(3.0, 2.0), 2) == 6.00, \
            "3.0 * 2.0 debe ser aproximadamente 6.00"
    except AssertionError as error:
        errores.append(f"Error en la primera aserción: {error}")
    try:
        assert round(aritmetica.multiplicar(-1.0, 1.0), 2) == -1.00, \
            "-1.0 * 1.0 debe ser aproximadamente -1.00"
    except AssertionError as error:
        errores.append(f"Error en la segunda aserción: {error}")
    try:
        assert round(aritmetica.multiplicar(0, 1.0), 2) == 0.00, \
            "0 * 1.0 debe ser aproximadamente 0.00"
    except AssertionError as error:
        errores.append(f"Error en la tercera aserción: {error}")

    if errores:
        for error in errores:
            print(error)
    else:
        print("\n➤ test_multiplicar pasó sin errores.")

def test_sumar_n():
    errores = []
    try:
        assert round(aritmetica.sumar_n(1.0, 2.0, 3.0), 2) == 6.00, \
            "1.0 + 2.0 + 3.0 debe ser aproximadamente 6.00"
    except AssertionError as error:
        errores.append(f"Error en la primera aserción: {error}")
    try:
        assert round(aritmetica.sumar_n(0, 0, 0), 2) == 0.00, \
            "0 + 0 + 0 debe ser aproximadamente 0.00"
    except AssertionError as error:
        errores.append(f"Error en la segunda aserción: {error}")
    try:
        assert round(aritmetica.sumar_n(1.1, 2.2, 3.3, 4.4), 2) == 11.00, \
            "1.1 + 2.2 + 3.3 + 4.4 debe ser aproximadamente 11.00"
    except AssertionError as error:
        errores.append(f"Error en la tercera aserción: {error}")

    if errores:
        for error in errores:
            print(error)
    else:
        print("\n➤ test_sumar_n pasó sin errores.")

def test_promedio_n():
    errores = []
    try:
        assert round(aritmetica.promedio_n(1.0, 2.0, 3.0), 2) == 2.00, \
            "El promedio de 1.0, 2.0 y 3.0 debe ser aproximadamente 2.00"
    except AssertionError as error:
        errores.append(f"Error en la primera aserción: {error}")
    try:
        assert round(aritmetica.promedio_n(0, 0, 0), 2) == 0.00, \
            "El promedio de 0, 0 y 0 debe ser aproximadamente 0.00"
    except AssertionError as error:
        errores.append(f"Error en la segunda aserción: {error}")
    try:
        assert round(aritmetica.promedio_n(1.1, 2.2, 3.3, 4.4), 2) == 2.75, \
            "El promedio de 1.1, 2.2, 3.3 y 4.4 debe ser aproximadamente 2.75"
    except AssertionError as error:
        errores.append(f"Error en la tercera aserción: {error}")

    if errores:
        for error in errores:
            print(error)
    else:
        print("\n➤ test_promedio_n pasó sin errores.")

if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_dividir()
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
    print("\n➤ Todos los tests han sido ejecutados.")