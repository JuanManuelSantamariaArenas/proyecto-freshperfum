class Usuario:
    def __init__(self, usuario, contraseña) -> None:
        self.usuario: str = usuario
        self.contraseña: str = contraseña

    def __str__(self) -> str:
        return f"Usuario: {self.usuario}  -  Contraseña: {self.contraseña}"
