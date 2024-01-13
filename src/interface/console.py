import sys
from app.module_one.class_bodega import *


class Console:
    def __init__(self) -> None:
        self.bodega = Bodega()
        self.bodega.cargar_historial()

        # MENU # 1
        self.opciones_menu_principal = {
            "1": self.general,
            "2": self.inventario,
        }

        # MENU # 1.1
        self.opciones_menu_general = {
            "1": self.administrar_usuarios,
            "2": self.visualizar_sucursales,
            "3": self.visualizar_empleados,
        }

        # MENU # 1.2
        self.opciones_menu_inventario = {
            "1": "",
        }

    def autenticar_usuario(self):
        print("Autenticar Administrador")

    # MENU # 1
    def mostrar_menu_principal(self):
        print(
            """
        \n
        MENU PRINCIPAL
        |||||||||||||||||||||||||||||||||||
        Menú de opciones:\n
        1. General
        2. Inventario
        
        |||||||||||||||||||||||||||||||||||
        """
        )

    # MENU # 1.1
    def mostrar_menu_general(self):
        print(
            """
        \n
        MENU GENERAL
        |||||||||||||||||||||||||||||||||||
        Menú de opciones:\n
        1. Administrar Usuarios
        2. Visualizar Sucursales
        3. Visualizar Empleados
        
        |||||||||||||||||||||||||||||||||||
        """
        )

    def ejecutar_programa(self):
        while True:
            self.autenticar_usuario()
            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción del menu: ")
            accion = self.opciones_menu_principal.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f"\n * INFO: {opcion} NO ES UNA OPCIÓN VALIDA")

    def general(self):
        print("Menu General")

    def administrar_usuarios(self):
        print("Administrar Usuarios")

    def visualizar_sucursales(self):
        print("Visulaizar Sucursales")

    def visualizar_empleados(self):
        print("Visulaizar Empleados")

    def inventario(self):
        print("Menu Inventario")
