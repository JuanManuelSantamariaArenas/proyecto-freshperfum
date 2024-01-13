class Empleado:
    def __init__(self, cedula, nombre) -> None:
        self.cedula: int = cedula
        self.nombre: str = nombre

    def __str__(self) -> str:
        return f"Cedula: {self.cedula}  -  Nombre: {self.nombre}"
