import random
import csv
import statistics

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajadores_sueldos = {}

def asignar_sueldo(trabajadores):
    for trabajador in trabajadores:
        sueldos = random.randint(300000,2500000)
        trabajadores_sueldos[trabajador]=sueldos
        for trabajador, sueldos in trabajadores_sueldos.items():
            print (f"{trabajador}, {sueldos}")

def clasificar_sueldo():
    menor=[]
    medio=[]
    alto=[]
    for i in trabajadores_sueldos:
        if float (i) < (800000):
            menor=i
            print(menor)
        elif float (i) == (800000,2000000):
            medio=i
            print(medio)
        elif float (i) > 2000000:
            alto=i
            print(alto)
    total_sueldos= menor+medio+alto

        
def estadisticas():
        listasueldos=[]
        for i in trabajadores_sueldos():
            listasueldos.append(sueldos)

        sueldo_mas_alto=max(sueldos)
        print(f"El sueldo más alto es: {sueldo_mas_alto}")
        sueldo_mas_bajo=min(sueldos)
        print(f"El sueldo más bajo es: {sueldo_mas_bajo}")
        promedio_sueldos=round(sum(sueldos.values())/len(sueldos),2)
        #media_geometrica

def reporte_sueldos(sueldos):
    with open('Sueldos.csv','a',newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=";")
        escritor_csv.writerow([" Nombre empleado "," Sueldo Base ","Descuento Salud:","Descuento AFP:","Sueldo Líquido"])

Trabajadores = ["Juan Pérez",
                "María García",
                "Carlos López",
                "Ana Martínez",
                "Pedro Rodríguez",
                "Laura Hernández",
                "Miguel Sánchez",
                "Isabel Gómez",
                "Francisco Díaz",
                "Elena Fernández"]
sueldos = {}


def salir():
    print("Finalizando programa…")
    print("Desarrollado por Paulina Campusano")
    print("RUT 18.165.530-5")
    exit()

import math
def main():
   
    while True:
        menu=int(input("""Ingrese una opción:
               1. Asignar sueldos
               2. Clasificar Sueldos
               3. Ver Estadistica
               4. Reporte de Sueldos
               5. Salir del Programa
              """))
        if menu == 1:
            print("Ingresando a Asignación de Sueldos")
            asignar_sueldo()
        elif menu == 2:
            print("Ingresando a Clasificar Sueldos")
            clasificar_sueldo()
        elif menu == 3:
            estadisticas()
            print("Ver Estadistica")
        elif menu == 4:
            print("Reporte de Sueldos")
            reporte_sueldos(sueldos)
        elif menu == 5:
            print("Saliendo del Programa")   
main ()

       