class Procesador:
    @staticmethod
    def procesar(Numero01: float, Numero02: float, Numero03: float) -> float:
        """
        Realiza la operación a * b + c.
        """
        if not all(isinstance(i, (int, float)) for i in [Numero01, Numero02, Numero03]):
            raise ValueError("Todos los parámetros deben ser números.")
        return Numero01 * Numero02 + Numero03

    @staticmethod
    def ejecutar(Resultado: float) -> float:
        """
        Eleva al cuadrado el valor de d.
        """
        if not isinstance(Resultado, (int, float)):
            raise ValueError("El parámetro debe ser un número.")
        return Resultado ** 2