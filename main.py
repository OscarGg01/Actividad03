class Procesador:
    @staticmethod
    def procesar(a: float, b: float, c: float) -> float:
        """
        Realiza la operación a * b + c.
        """
        if not all(isinstance(i, (int, float)) for i in [a, b, c]):
            raise ValueError("Todos los parámetros deben ser números.")
        return a * b + c

    @staticmethod
    def ejecutar(d: float) -> float:
        """
        Eleva al cuadrado el valor de d.
        """
        if not isinstance(d, (int, float)):
            raise ValueError("El parámetro debe ser un número.")
        return d ** 2
