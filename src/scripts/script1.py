from app.module_one.class_usuario import *
from app.module_one.class_empleado import *
from app.module_one.class_sucursal import *


def migrar_usuarios():
    with open("data/usuarios.csv") as file:
        datos_iniciales = [linea.strip("\n") for linea in file]
        usuarios_finales = [linea.split(",") for linea in datos_iniciales]
        del usuarios_finales[0]
        usuarios = {
            int(usuario[0]): Usuario(usuario[0], usuario[1])
            for usuario in usuarios_finales
        }
    return usuarios


def migrar_sucursales():
    with open("data\sucursales.csv") as file:
        datos_iniciales = [linea.strip("\n") for linea in file]
        sucursales_finales = [linea.split(",") for linea in datos_iniciales]
        del sucursales_finales[0]
        sucursales = {
            int(sucursal[0]): Sucursal(sucursal[0], sucursal[1])
            for sucursal in sucursales_finales
        }
    return sucursales


def migrar_empleados():
    with open("data\empleados.csv") as file:
        datos_iniciales = [linea.strip("\n") for linea in file]
        empleados_finales = [linea.split(",") for linea in datos_iniciales]
        del empleados_finales[0]
        empleados = {
            int(empleado[0]): Empleado(empleado[0], empleado[1])
            for empleado in empleados_finales
        }
    return empleados
