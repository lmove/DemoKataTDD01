class Calculadora:

    def sumar(self, cadena):
        if len(cadena) == 0:
            return 0
        elif len(cadena) == 1:
            return 1
        else:
            if "," in cadena or ":" in cadena or "&" in cadena:
                cadena = cadena.replace(":", ",")
                cadena = cadena.replace("&", ",")
                array = cadena.split(",")
                cont = 0

                for a in array:
                    cont += int(a)

                return cont