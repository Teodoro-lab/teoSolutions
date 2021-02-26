#nombre = input("Ingrese el nombre del empleado: ")
"""
while False:
    try:
        sueldo = int(input(f"Ingrese el sueldo del empleado {nombre} por hora: "))
    except Exception as Err:
        print("Ingreso un número erróneo: Intente de nuevo")
    else:
        break
while False:
    try:
        horas = int(input("Ingrese la cantidad de horas trabajadas: "))
    except Exception as Err:
        print("Ingreso un número erróneo: Intente de nuevo")
    else:
        break
"""       


#pago = sueldo * horas
#print(pago)
#descuento = (pago / 100) * 20
#sueldoNeto = pago - descuento



class Empleado:
    def __init__(self, nombre, sueldoXHora, horas):
        self.nombre = nombre
        self.sueldoXHora = sueldoXHora
        self.horas = horas
        
    def sueldoTotal(self):
        sTotal = self.sueldoXHora * self.horas
        return sTotal

    def descuento(self):
        descuento = self.sueldoTotal() / 100 * 20
        return descuento
    
    def sueldoNeto(self):
        sueldoNeto = self.sueldoTotal() - self.descuento()
        return sueldoNeto
    
    def mensaje(self):
        reporte = f"""El sueldo neto del empleado {self.nombre} es igual a
{self.sueldoNeto()} MXN con un pago orginial de {self.sueldoTotal()} MXN y un
descuento del 20% igual a {self.descuento()} MXN"""
        return reporte

class Plantilla:
    def __init__(self):
        self.numEmploy = 0
        self.Employes = []
        
    def crearPlantilla(self):
        addEmployes = int(input("Ingrese cuántos empleados va a agregar a platilla: "))
        for i in range(addEmployes):
            nameEmpleado = input("Ingrese el nombre del empleado: ")
            sueldoXhoras = int(input("Ingrese el sueldo por hora del empleado: "))
            jornadaLaboral = int(input("Ingrese la jornada laboral: "))
            self.Employes.append(Empleado(nameEmpleado, sueldoXhoras, jornadaLaboral))

plantilla_1_0 = Plantilla()
plantilla_1_0.crearPlantilla()
for employe in plantilla_1_0.Employes:
    print(employe.mensaje(), "\n")

finish = input("Si quiere terminar el programa presione 1 y enter: ")
if finish == 1:
    pass



