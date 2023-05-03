import modulo_proyecto
import csv
seguir=True
archivo= 'proyecto.csv'
while seguir:
    print("Hola soy Tripbud, tu asistente")
    menu=input(""" ¿En que puedo ayudarte?
1.Hacer Check-in (realizar solo una vez)
2.Ver datos antes de imprimir
3.Imprimir Boleto 
4.Modificar pasaporte
5.Modificar nombre
6.Modificar apellido 
7.Encontrar restaurantes 
8.Salir
"""
)
    if  menu.isdigit() and 1<= int(menu) <=8:
        menu=int(menu)
        if menu==1:
            modulo_proyecto.check_in()
        elif menu==2:
            pregunta=input("Ingresa su nombre : ")
            pregunta=pregunta.capitalize()
            modulo_proyecto.vista_previa(pregunta)
            print("RECUERDA SOLO IMPRIMIR TU BOLETO CUANDO ESTES SEGURO DE TUS DATOS")
        elif menu==3:
            modulo_proyecto.imprimir_boleto()
            print("SI NO NECESITAS NADA MAS PRESIONA 8 PARA SALIR")
            
           
        elif menu==4:
            nuevo=input("Escriba su nombre: ")
            nuevo=nuevo.capitalize()
            nuevo_pas=input("Ahora escriba de nuevo su pasaporte:")
            modulo_proyecto.mod_pas(nuevo,nuevo_pas)
            
        elif menu==5:
            nombre = input("Escriba su numero de pasaporte: ")
            nombre = nombre.capitalize()
            nuevo_nom = input("Escriba el nuevo nombre : ")
            nuevo_nom = nuevo_nom.capitalize()
            modulo_proyecto.cambio_nom(nombre, nuevo_nom)
           
        elif menu==6:
            apellido = input("Escriba su nombre: ")
            apellido = apellido.capitalize()
            nuevo_ape = input("Escriba el nuevo apellido para el pasaporte: ")
            nuevo_ape = nuevo_ape.capitalize()
            modulo_proyecto.cambio_ape(apellido, nuevo_ape)
           
        elif menu==7:
            tipo_comida=input("""¿Que tipo de comida busca? 
        Categorias:(hamburguesas,pizza,Saludable,pollo,café,steak,sushi y bar)

        """)
            tipo_comida=tipo_comida.capitalize()
            if tipo_comida.isalpha()==True:
                if tipo_comida=="Cafe":
                    tipo_comida="Café"
                modulo_proyecto.restaurantes(tipo_comida)
            else:
                print("ERROR: Escribe una categoria ")
        elif menu==8:
            print("¡Feliz Viaje!")
            modulo_proyecto.borrar()
            break
    else:
        print("ERROR:Ingresa un numero del 1 al 7")
