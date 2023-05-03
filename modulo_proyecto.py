import csv 
import random
#Listas para randomizar los horarios2,asientos y puerta
archivo= 'proyecto.csv'
horarios=["4:00","7:00","11:30","15:45","18:30","21:00","0:45"]
asientos_r=["A3","B4","C5","A7","B15","C22","B2"]
puerta=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]

def check_in():
    #función para hacer al check in
 with open(archivo,'a', newline='') as check_in:
    #usamos el modo append
    #pedimos cada dato necesario para el check in 
    pasaporte = input("Pasaporte: ")
    nom = input("Nombre: ")
    nom = nom.capitalize()
    last_name= input("Apellido: ")
    last_name=last_name.capitalize()
    num_vuelo = input("Numero de vuelo: ")
    door = random.choice(puerta)
    asiento= random.choice(asientos_r)
    hora_del_vuelo = random.choice(horarios)
    aerolinea = input("Aerolinea : ")
    aerolinea = aerolinea.capitalize()
    destino=input("Destino: ")
    destino=destino.capitalize()
    escala=random.choice([True,False])
    if escala==True:
        escala="SI"
    else:
        escala="NO"
    
    writer = csv.writer(check_in, delimiter=",")
    #escribimos cada variable en separada por comas 
    writer.writerow([pasaporte, nom,last_name, num_vuelo, door, asiento, hora_del_vuelo, aerolinea, destino,escala])
    with open(archivo,'r') as idk:
        lec=csv.reader(idk)
        lista=list(lec)
    with open(archivo,'w',newline='') as data:
        writer=csv.writer(data)
        writer.writerows(lista)
        print("Datos guardados, ya puedes imprimir tu boleto")
        print("Revisa tus datos con la opción dos para verificar que todo este bien antes de imprimir")

def vista_previa(pregunta):
    with open (archivo,'r') as vista:
        lec=csv.reader(vista)
        lista=list(lec)
        for i in range(len(lista)):
            if lista[i][0]==pregunta:
                print("PASAPORTE:",lista[i][0],"|","NOMBRE:",lista[i][1],"|","APELLIDO:",lista[i][2],"|","NO.VUELO:",lista[i][3],"|","PUERTA",lista[i][4],"|","ASIENTO:",lista[i][5],"|","HORA DE SALIDA:",lista[i][6],"|","AEROLINEA:",lista[i][7],"|","DESTINO:",lista[i][8],"|","ESCALA:",lista[i][9])
            else:
                print("El nombre no se encontró, quizás lo escribiste mal")
                break
def mod_pas(nuevo,nuevo_pas):
    with open(archivo, 'r') as new:
        #leemos
        lec = csv.reader(new)
        #hacemos una lista de lo que leimos
        lista = list(lec)
    for i in range(len(lista)):
        #si el nuevo es igual al elemento 1 de alguna liena de la lista cambiamos el elemento 0 por el nuevo_pas (estos datos los pedimos en el main)
        if lista[i][1] == nuevo:
            lista[i][0] = nuevo_pas
            #escribimos otra vez la lista que tenemos con los datos actualizados
            with open(archivo, 'w', newline="") as rename:
                writer = csv.writer(rename)
                writer.writerows(lista)
                print("Datos actualizados")
        else:

            print("El nombre no se encontró,quizas lo escribiste mal")
            break



def cambio_nom(nombre, nuevo_nom):
    with open (archivo, 'r') as nuevo:
        #Leer el archivo
        lec = csv.reader(nuevo)
        lista = list(lec)
    for i in range(len(lista)):
        #Buscar en la lista el nombre dado, si se encuentra, cambiar ese nombre por el nuevo nombre ingresado
        if lista[i][0] == nombre:
            lista[i][1] = nuevo_nom
        #Actualizar los datos
            with open(archivo, 'w', newline="") as nomnuevo:
                writer = csv.writer(nomnuevo)
                writer.writerows(lista)
                print("Nombre actualizado exitosamente")   
        else:
           print("No se encontró el pasaporte,quizas lo escribiste mal") 
           break     

def cambio_ape(apellido, nuevo_ape):
    with open (archivo, 'r') as last_name:
        lec = csv.reader(last_name)
        lista = list(lec)
    for i in range(len(lista)):
        #Buscar en la lista el nombre dado, si se encuentra, cambiar ese nombre por el nuevo nombre ingresado
        if lista[i][1] == apellido:
            lista[i][2] = nuevo_ape
        #Actualizar los datos
            with open(archivo, 'w', newline="") as apenuevo:
                writer = csv.writer(apenuevo)
                writer.writerows(lista)
                print("Apellido actualizado exitosamente")
        else:
            print("No se encontró el nombre,quizas lo escribiste mal")
            break
def imprimir_boleto():   
    import csv
    import turtle
    datos_pasajeros = 'proyecto.csv'

    window = turtle.Screen()
    window.setup(1000, 350, 0, 0)
    window.bgcolor("white")
    window.title("AEROPUERTO INTERNACIONAL LA AURORA - BOARDING PASS")
    t = turtle.Turtle()
    t.speed(0.5)
        
    #Hacer el borde del boleto
    t.penup()
    t.hideturtle()
    t.goto(-480, 160)
    t.pendown()
    t.color("black")
    t.pensize(3)
    for i in range(2):
        t.forward(960)
        t.right(90)
        t.forward(320)
        t.right(90)
    t.penup()

    #Hacer el espacio para el titulo del boleto
    t.right(90)
    t.forward(45)
    t.left(90)
    t.pendown()
    t.pensize(2)
    t.forward(960)
    t.penup()

    #Hacer el título del Boarding Pass
    header = turtle.Turtle()
    header.hideturtle()
    header.penup()
    header.speed(0.5)
    header.goto(-400, 125)
    header.write("B O A R D I N G  P A S S", False, "left", ("Arial", 18, "italic bold"))
    #Escribir el titulo del arrancable del boleto
    header.penup()
    header.forward(690)
    header.pendown()
    header.write("BOARDING PASS", False, "left", ("Arial", 11, ""))





    #Escribir los datos en la parte PRINCIPAL del boleto a partir del CSV
    with open(datos_pasajeros, 'r') as archivo:
        #Guardar los datos del archivo csv en un diccionario
        lec = csv.DictReader(archivo)
        t.goto(-440, 50)
        for fila in lec:
            t.pendown()
            t.write(f"NOMBRE: {fila['Nombre del pasajero']}", font=("Arial", 10, 'normal'))
            t.penup()
            t.right(90)
            t.forward(25)
            t.pendown()
            t.write(f"APELLIDO: {fila['Apellido del pasajero']}", font=("Arial", 10, 'normal'))
            t.penup()
            t.forward(25)
            t.write("ORIGEN: Guatemala", font=("Arial", 10, 'normal'))
            t.left(90)
            t.forward(150)
            t.write(f"DESTINO:{fila['Destino']}", font=("Arial", 10, 'normal'))
            t.right(180)
            t.forward(150)
            t.left(90)
            t.forward(25)
            t.write(f"HORA DE SALIDA:{fila['Hora del vuelo']}", font=("Arial", 10, 'normal'))
            t.left(8)
            t.forward(25)
            t.write(f"PUERTA:{fila['Puerta']}", font=("Arial", 10, 'normal'))
            t.left(90)
            t.forward(150)
            t.write(f"ASIENTO:{fila['Numero de asiento']}", font=("Arial", 10, 'normal'))
            t.left(90)
            t.forward(-30)
            t.left(90)
            t.forward(3)
            t.write(f"ESCALA:{fila['Escala']}", font=("Arial", 10, 'normal'))
            t.left(90)
            t.forward(-108)
            t.right(90)
            t.forward(-10)
            t.write(f"NO.PASAPORTE:{fila['Pasaporte']}", font=("Arial", 10, 'normal'))
            t.left(90)
            t.forward(25)
            t.write(f"AEROLINEA:{fila['Aerolinea']}",font=("Arial",10,"normal"))

    #Linea punteada del arrancable 
    guiones = turtle.Turtle()
    guiones.speed(0.05)
    guiones.penup()
    guiones.goto(225, 160)
    guiones.right(90)
    for i in range(32):
        guiones.pendown()
        guiones.forward(5)
        guiones.penup()
        guiones.forward(5)

    window.exitonclick()


    
def restaurantes(tipo_comida):
    lista_de_comidas=["Hamburguesas","Pizza","Comida saludable","Pollo frito","Café","Steak","Sushi", "Bar"]
    if tipo_comida in lista_de_comidas:
        import pandas as pd
        df=pd.read_csv('restaurantes.csv')
        rest=df[df["Tipo de comida"]==tipo_comida]
        print(rest)
    else:
        print("ERROR:No existe esa categoría")
def borrar():
    with open(archivo,'w',newline="")as borrador:
        writer=csv.writer(borrador,delimiter=",")
        writer.writerow(["Pasaporte","Nombre del pasajero","Apellido del pasajero","Numero de vuelo","Puerta","Numero de asiento","Hora del vuelo","Aerolinea","Destino","Escala"])






    
  




