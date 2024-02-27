import sys
from app.module_one.class_bodega import *


class Console:
    def __init__(self) -> None:
        self.bodega = Bodega()
        self.bodega.cargar_historial()
        self.autenticacion = False
        self.menu_anterior = ""
        # MENU # 1
        self.opciones_menu_principal = {
            "1": self.general,
            "2": self.inventario,
            "C": self.cerrar_aplicacion,
        }

        # MENU # 1.1
        self.opciones_menu_general = {
            "1": self.administrar_usuarios,
            "2": self.visualizar_sucursales,
            "3": self.visualizar_empleados,
            "R": self.regresar_menu_anterior,
        }

        # MENU # 1.2
        self.opciones_menu_inventario = {
            "1": "",
            "R": self.regresar_menu_anterior,
        }

    def autenticar_usuario(self):
        if self.autenticacion:
            return
        else:
            self.autenticacion = True
            while True:
                print("BIENVENIDO\n")
                usuario = input("USUARIO: ")
                contraseña = input("CONTRASEÑA: ")
                if self.bodega.existe_usuario(usuario):
                    contraseña_usuario = self.bodega.usuarios[usuario].contraseña
                    if contraseña_usuario == contraseña:
                        break
                    else:
                        print(f"\n * INFO: USUARIO O CONTRASEÑA NO ES VALIDA\n")
                else:
                    print(f"\n * INFO: USUARIO O CONTRASEÑA NO ES VALIDA\n")

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
        F. Cerrar Aplicación
        
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
        R. Regresar
        
        |||||||||||||||||||||||||||||||||||
        """
        )

    def ejecutar_programa(self):
        self.autenticar_usuario()
        self.menu_anterior = self.menu_anterior
        while True:
            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción del menu: ")
            accion = self.opciones_menu_principal.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f"\n * INFO: {opcion} NO ES UNA OPCIÓN VALIDA")

    def general(self):
        self.menu_anterior = self.ejecutar_programa
        while True:
            self.mostrar_menu_general()
            opcion = input("Seleccione una opción del menu: ")
            accion = self.opciones_menu_general.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f"\n * INFO: {opcion} NO ES UNA OPCIÓN VALIDA")

    def administrar_usuarios(self):
        print("Administrar Usuarios")

    def visualizar_sucursales(self):
        print("Visulaizar Sucursales")

    def visualizar_empleados(self):
        print("Visulaizar Empleados")

    def regresar_menu_anterior(self):
        self.menu_anterior()

    def inventario(self):
        print("Menu Inventario")

    def cerrar_aplicacion(self):
        print("\nMUCHAS GRACIAS POR USAR LA APLICACIÓN 👍👍👍")
        self.bodega.guardar_historial()
        sys.exit(0)
