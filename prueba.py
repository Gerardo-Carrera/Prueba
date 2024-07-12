import os,random,statistics,csv
os.system("cls")
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]

def asignar_sueldos_aleatorios():
    if len(sueldos)==10:
        for a in sueldos:
            a["Sueldo"]=random.randint(300000,2500000)
        return
    for a in range(len(trabajadores)):
        sueldos.append({"Nombre":trabajadores[a],"Sueldo":random.randint(300000,2500000)})

def clasificar_sueldos():
    if len(sueldos)==0 : 
        print("No hay sueldos registrados")
        input()
        return
    t1=[]   
    t2=[]
    t3=[]
    total1=0
    total2=0
    total3=0
    for a in sueldos:
        if a["Sueldo"]<800000:
            t1.append({"Nombre":a["Nombre"],"Sueldo": a["Sueldo"]})
            total1+=1
        elif a["Sueldo"]<2000000:
            t2.append({"Nombre":a["Nombre"],"Sueldo": a["Sueldo"]})
            total2+=1
        elif a["Sueldo"]>2000000:
            t3.append({"Nombre":a["Nombre"],"Sueldo": a["Sueldo"]})
            total3+=1
    print(f"Sueldos menores a $800.000\tTotal={total1}\n\nNombre Empleado\t\tSueldo")
    for a in t1:
        print(f"{a["Nombre"]}\t\t${a["Sueldo"]}")
    print("")
    print(f"Sueldos entre $800.000 y $2.000.000\tTotal={total2}\n\nNombre Empleado\t\tSueldo")
    for a in t2:
        print(f"{a["Nombre"]}\t\t${a["Sueldo"]}")
    print("")
    print(f"Sueldos superiores a $2.000.000\tTotal={total3}\n\nNombre Empleado\t\tSueldo")
    for a in t3:
        print(f"{a["Nombre"]}\t\t${a["Sueldo"]}")
    input()
    os.system("cls")


def ver_estadísticas():
    if len(sueldos)==0 : 
        print("No hay sueldos registrados")
        input()
        return
    medialista=[]
    minimo=min(sueldos,key=lambda x:x["Sueldo"])
    maximo=max(sueldos,key=lambda x:x["Sueldo"])
    promedio=0
    for a in sueldos:
        promedio+=a["Sueldo"]
    promedio=promedio/len(trabajadores)
    for a in sueldos:
        medialista.append(a["Sueldo"])
    media=statistics.geometric_mean(medialista)
    print(f"Sueldo mas bajo: ${minimo["Sueldo"]}\nSueldo mas alto: ${maximo["Sueldo"]}\nPromedio sueldos: {promedio}\nMedia geometrica: {media}")
    input()
    
def reporte_de_sueldos():
    if len(sueldos)==0 : 
        print("No hay sueldos registrados")
        input()
        return
    with open("sueldos.csv","w",newline="",encoding="utf8") as archvo:
        print("Nombre Empleado\t\tSueldo Base\tDescuento Salud\t\tDescuento AFP\tSueldo Liquido")
        escribir=csv.writer(archvo)
        escribir.writerow(["Nombre Empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
        for a in sueldos:
            desc_salud=int(a["Sueldo"]*0.07)
            desc_afp=int(a["Sueldo"]*0.12)
            sueldo_liquido=a["Sueldo"]-desc_salud-desc_afp
            print(f"{a["Nombre"]}\t\t{a["Sueldo"]}\t\t{desc_salud}\t\t\t{desc_afp}\t\t{sueldo_liquido}")
            escribir.writerow([a["Nombre"],a["Sueldo"],desc_salud,desc_afp,sueldo_liquido])
            
    input()

while True:
    op=input("Menu\n1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadísticas.\n4. Reporte de sueldos\n5. Salir del programa\n")
    match op:
        case "1":
            asignar_sueldos_aleatorios()
            os.system("cls")
        case "2":
            os.system("cls")
            clasificar_sueldos()
        case "3":
            os.system("cls")
            ver_estadísticas()
            os.system("cls")
        case "4":
            os.system("cls")
            reporte_de_sueldos()
            os.system("cls")
        case "5":
            os.system("cls")
            print("Finalizando Programa...\nDesarrollado por Gerardo Carrera\nRut 21.967.226-8")
            break
        case _:
            os.system("cls")
            print("ERROR")