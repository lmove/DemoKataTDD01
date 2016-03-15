class Calculadora:

    def sumar(self, cadena):
        if len(cadena) == 0:
            return 0
        elif len(cadena) == 1:
            return 1
        else:
            if "," in cadena:
                return int(cadena[0]) + int(cadena[2])