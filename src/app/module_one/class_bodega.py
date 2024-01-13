import pickle
from scripts.script1 import *
from .class_usuario import *
from .class_sucursal import *
from .class_empleado import *


class Bodega:
    def __init__(self) -> None:
        self.usuarios: dict[str:Usuario] = {}
        self.sucursales: dict[int:Sucursal] = {}
        self.empleados: dict[int:Empleado] = {}

    # Funcionalidades
    def visualizar_usuarios(self) -> str:
        usuarios = [print(usuario) for usuario in self.usuarios.values()]
        return

    def visualizar_sucursales(self) -> str:
        sucursales = [print(sucursal) for sucursal in self.sucursales.values()]
        return

    def visualizar_empleados(self) -> str:
        empleados = [print(empleado) for empleado in self.empleados.values()]
        return

    # Ayudas
    def existe_usuario(self, usuario) -> bool:
        if usuario in self.usuarios:
            return True
        else:
            return False

    def existe_sucursal(self, codigo) -> bool:
        if codigo in self.sucursales:
            return True
        else:
            return False

    def existe_empleado(self, cedula) -> bool:
        if cedula in self.empleados:
            return True
        else:
            return False

    def cargar_historial(self):
        with open("data\historial.txt", "rb") as file:
            # bodega = pickle.load(file)
            usuarios = migrar_usuarios()
            sucursales = migrar_sucursales()
            empleados = migrar_empleados()
            self.usuarios = usuarios
            self.sucursales = sucursales
            self.empleados = empleados
        return
