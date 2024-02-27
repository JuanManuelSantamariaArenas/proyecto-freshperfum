def existe_empleado(cedula) -> bool:
    empleados = {"Juan": 1, "Luis": 3, "Carmen": 4}
    # for cedulas_actuales in self.empleados.keysdef existe_empleado(cedula) -> boo:         return True
    # return False
    if cedula in empleados:
        print("YES")
    else:
        print("NO")


existe_empleado("Juan")
existe_empleado(2)
existe_empleado(3)
existe_empleado(5)
existe_empleado(4)
