class Sucursal:
    def __init__(self, codigo, nombre) -> None:
        self.codigo: int = codigo
        self.nombre: int = nombre

    def __str__(self) -> str:
        return f"Código: {self.codigo}  -  Nombre: {self.nombre}"
