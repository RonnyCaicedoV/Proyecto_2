from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesUnemi import *
from datetime import date
import time

# Procesos de las Opciones del Menu Mantenimiento
def carreras():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(13,5);print("Descripcion Carrera: ")
   gotoxy(33,5)
   descarrera = input()
   archiCarrera = Archivo("carrera.txt",";")
   carreras = archiCarrera.leer()
   if carreras : idSig = int(carreras[-1][0])+1
   else: idSig=1
   carrera = Carrera(idSig,descarrera)
   datos = carrera.getCarrera()
   datos = ';'.join(datos)
   archiCarrera.escribir([datos],"a")
   
   
def matricula():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula : ")
   gotoxy(15,6);print("Titulo : ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   gotoxy(25,4);nom = input()
   gotoxy(25,5);ced = input()
   gotoxy(25,6);tit = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,8);print(entCarrera.descripcion)
      else: 
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiProfesor = Archivo("profesor.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Profesor(idSig,nom,ced,entCarrera,tit,tel)
        datos = entProfesor.getProfesor()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")    


def materias():
    pass

def profesores():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula  : ")
   gotoxy(15,6);print("Titulo  : ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   gotoxy(25,4);nom = input()
   gotoxy(25,5);ced = input()
   gotoxy(25,6);tit = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,8);print(entCarrera.descripcion)
      else: 
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiProfesor = Archivo("profesor.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Profesor(idSig,nom,ced,entCarrera,tit,tel)
        datos = entProfesor.getProfesor()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     

def estudiantes():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE ESTUDIANTES")
   gotoxy(15,4);print("Nombres completos : ")
   gotoxy(15,5);print("Cedula  : ")
   gotoxy(15,6);print("Direccion: ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(34,4);nom = input()
   gotoxy(25,5);ced = input()
   gotoxy(27,6);dire = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   archiEstudiante = Archivo("Estudiantes.txt",";")
   estudiantes = archiEstudiante.leer()
   if estudiantes : idSig = int(estudiantes[-1][0])+1
   else: idSig=1
   estudiantes = Estudiante(idSig,nom,ced,dire,tel)
   datos = estudiantes.getEstudiante()
   datos = ';'.join(datos)
   archiEstudiante.escribir([datos],"a")
   gotoxy(15,10);print("Esta seguro de Grabar El Registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiEstudiante = Archivo("Estudiantes.txt")
        lisEstudiante = archiEstudiante.leer()
        if lisEstudiante : idSig = int(lisEstudiante[-1][0])+1
        else: idSig=1
        entEstudiante = Estudiante(idSig,nom,ced,dire,tel)
        datos = entEstudiante.getEstudiante()
        datos = ';'.join(datos)
        archiEstudiante.escribir([datos],"a")                 
        gotoxy(15,11);input("El Registro se ha Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado Correctamente\n presione una tecla para continuar...")     
     
     
     
     
def matricula():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("Matricula")
   gotoxy(15,4);print("Estudiante ID[    ]  : ")
   gotoxy(15,5);print("Carrera ID[   ] : ")
   gotoxy(15,6);print("Periodo  : ")
   gotoxy(15,7);print("Valor a pagar: ")
   gotoxy(25,4);nom = input()
   gotoxy(25,5);ced = input()
   gotoxy(25,6);tit = input()
   Valor=validar.solo_numeros("Error: Solo numeros",25,7)
   lisEstudiante,entEstudiante = [],None
   while not lisEstudiante:
      gotoxy(27,8);id = input().upper()
      archiEstudiante = Archivo("Estudiantes.txt")
      lisEstudiante = archiEstudiante.buscar(id)
      if lisEstudiante:
          entEstudiante= Carrera(lisEstudiante[0],lisEstudiante[1]) 
          gotoxy(33,8);print(entEstudiante.descripcion)
      else: 
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("Carreras.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,8);print(entCarrera.descripcion)
      else: 
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiProfesor = Archivo("profesor.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Profesor(idSig,nom,ced,entCarrera,tit,Valor)
        datos = entProfesor.getProfesor()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
# Menu Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Matriculacion","3) Notas","4) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='6':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Carrera","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                carreras()
            elif opc1 == "4":
                profesores()
            if opc1 == "5":
                estudiantes()
                        
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Matriculacion",["1) Matricula","2) Salir"],15,5)
            opc2 = menu2.menu()
            if opc2 == "1":
                matricula()
             
                pass
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                pass
                
            
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

