from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesUnemi import *
from datetime import date
import time

# Procesos de las Opciones del Menu Mantenimiento
def carreras():
   borrarPantalla() 
   validar=Valida()        
   gotoxy(20,2);print("Registro de notas")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(13,5);print("Descripcion Carrera: ")
   gotoxy(33,5)
   descarrera = validar.solo_letras("Error: Escriba solo letras",33,5)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiCarrera = Archivo("carrera.txt")
        lisCarreras = archiCarrera.leer()
        if lisCarreras : idSig = int(lisCarreras[-1][0])+1
        else: idSig=1
        entCarrera = Carrera(idSig,descarrera)
        datos = entCarrera.getCarrera()
        datos = ';'.join(datos)
        archiCarrera.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     

def materias():
   borrarPantalla() 
   validar=Valida()    
   gotoxy(20,2);print("Registro de Materias")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(10,5);print("Nombre De la materia: ")
   gotoxy(33,5)
   desmateria = input()
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiMateria = Archivo("Materias.txt")
        lisMaterias = archiMateria.leer()
        if lisMaterias : idSig = int(lisMaterias[-1][0])+1
        else: idSig=1
        entMateria = Materia(idSig,desmateria)
        datos = entMateria.getMateria()
        datos = ';'.join(datos)
        archiMateria.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
   
   
def periodo():
   borrarPantalla()     
   gotoxy(20,2);print("Registro de periodo")
   gotoxy(15,4);print("Periodo: ")
   gotoxy(9,5);print("Descripcion del periodo: ")
   gotoxy(23,4)
   Peri= input()
   gotoxy(33,5)
   desperiodo = input()
   archiPeriodo = Archivo("Periodos.txt",";")
   periodo = archiPeriodo.leer()
   periodo = Periodo(Peri,desperiodo)
   datos = periodo.getPeriodo()
   datos = ';'.join(datos)
   archiPeriodo.escribir([datos],"a")
   

def profesores():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula  : ")
   gotoxy(15,6);print("Titulo  : ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   gotoxy(25,4);nom = validar.solo_letras("Error: Escriba solo letras",25,4)
   gotoxy(25,5);ced = validar.solo_numeros("Error: Solo numeros",25,5)
   gotoxy(25,6);tit = validar.solo_letras("Error: Escriba solo letras",25,6)
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
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula  : ")
   gotoxy(15,6);print("Direccion: ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(30,4);nom = validar.solo_letras("Error: Escriba solo letras",30,4)
   gotoxy(25,5);ced = validar.solo_numeros("Error: Solo numeros",25,5)
   gotoxy(27,6);dire = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   archiEstudiante = Archivo("Estudiantes.txt",";")
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
    
# Procesos de la opcion del Menu Matricula    
    
def matricula():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("Matricula")
   gotoxy(15,4);print("Estudiante ID[    ]  : ")
   gotoxy(15,5);print("Carrera ID[   ] : ")
   gotoxy(15,6);print("Periodo [     ] : ")
   gotoxy(15,7);print("Valor a pagar: ")
   lisEstudiante,entEstudiante = [],None
   while not lisEstudiante:
      gotoxy(30,4);id = input().upper()
      archiEstudiante = Archivo("Estudiantes.txt")
      lisEstudiante = archiEstudiante.buscar(id)
      if lisEstudiante:
          entEstudiante= Estudiante(lisEstudiante[0],lisEstudiante[1],lisEstudiante[2],lisEstudiante[3],lisEstudiante[4]) 
          gotoxy(35,4);print(entEstudiante.nombre,entEstudiante.cedula,entEstudiante.direccion,entEstudiante.telefono)
      else: 
         gotoxy(33,8);print("No existe Estudiante con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,5);id = input().upper()
      archiCarrera = Archivo("carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(32,5);print(entCarrera.descripcion)
      else: 
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   lisPeriodo,entPeriodo = [],None
   while not lisPeriodo:
      gotoxy(25,6);peri = input().upper()
      archiPeriodo = Archivo("Periodos.txt")
      lisPeriodo = archiPeriodo.buscar(peri)
      if lisPeriodo:
          entPeriodo = Periodo(lisPeriodo[0],lisPeriodo[1]) 
          gotoxy(32,6);print(entPeriodo.descripcion)
      else: 
         gotoxy(33,8);print("No existe Periodo [{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
    
      valor=validar.solo_decimales("Error: Solo numeros",29,7)     
    
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiMatricula = Archivo("Matriculas.txt")
        lisMatricula = archiMatricula.leer()
        if lisMatricula : idSig = int(lisMatricula[-1][0])+1
        else: idSig=1
        entMatricula = Matricula(idSig,entEstudiante,entCarrera,entPeriodo,valor)
        datos= entMatricula.getEstudiante()
        datos = ';'.join(datos)
        archiMatricula.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     


# Procesos de la Opcion del Menu Notas
      
def notas():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print(" NOTAS ")
   gotoxy(15,4);print("Estudiante ID[    ]  : ")
   gotoxy(15,5);print("Materia ID[   ] : ")
   gotoxy(15,6);print("Periodo [     ] : ")
   gotoxy(15,7);print("Profesor ID[   ]: ")
   gotoxy(15,8);print("Nota1: ")
   gotoxy(15,9);print("Nota2: ")
   
   
   lisEstudiante,entEstudiante = [],None
   while not lisEstudiante:
      gotoxy(30,4);id = input().upper()
      archiEstudiante = Archivo("Estudiantes.txt")
      lisEstudiante = archiEstudiante.buscar(id)
      if lisEstudiante:
          entEstudiante= Estudiante(lisEstudiante[0],lisEstudiante[1],lisEstudiante[2],lisEstudiante[3],lisEstudiante[4]) 
          gotoxy(35,4);print(entEstudiante.nombre,entEstudiante.cedula,entEstudiante.direccion,entEstudiante.telefono)
      else: 
         gotoxy(33,8);print("No existe Estudiante con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   lisMateria,entMateria = [],None
   while not lisMateria:
      gotoxy(27,5);id = input().upper()
      archiMateria = Archivo("Materias.txt")
      lisMateria = archiMateria.buscar(id)
      if lisMateria:
          entMateria = Materia(lisMateria[0],lisMateria[1]) 
          gotoxy(32,5);print(entMateria.descripcion)
      else: 
         gotoxy(33,8);print("No existe Materia con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   lisPeriodo,entPeriodo = [],None
   while not lisPeriodo:
      gotoxy(25,6);peri = input().upper()
      archiPeriodo = Archivo("Periodos.txt")
      lisPeriodo = archiPeriodo.buscar(peri)
      if lisPeriodo:
          entPeriodo = Periodo(lisPeriodo[0],lisPeriodo[1]) 
          gotoxy(32,6);print(entPeriodo.descripcion)
      else: 
         gotoxy(33,8);print("No existe Periodo [{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
         
   lisProfesor,entProfesor = [],None
   while not lisProfesor:
      gotoxy(28,7);id = input().upper()
      archiProfesor = Archivo("profesor.txt")
      lisProfesor = archiProfesor.buscar(id)
      if lisProfesor:
          entProfesor= Profesor(lisProfesor[0],lisProfesor[1],lisProfesor[2],lisProfesor[3],lisProfesor[4],lisProfesor[5]) 
          gotoxy(35,7);print(entProfesor.nombre,entProfesor.cedula,entProfesor.titulo,entProfesor.telefono,entProfesor.carrera)
      else: 
         gotoxy(33,8);print("No existe Profesor con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   
    
      Nota1=validar.solo_decimales("Error: Solo numeros",29,8)     
      Nota2= validar.solo_decimales("Error: Solo numeros",29,9)
      
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiNotas = Archivo("Notas.txt")
        lisNotas = archiNotas.leer()
        if lisNotas : idSig = int(lisNotas[-1][0])+1
        else: idSig=1
        entNotas = Notas(idSig,entPeriodo,entEstudiante,entMateria,entProfesor,Nota1,Nota2)
        datos= entNotas.getEstudiante()
        datos = ';'.join(datos)
        archiNotas.escribir([datos],"a")                 
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
            if opc1 == "2":
                materias()
            if opc1 == "3":
                periodo()
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
            
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                notas()
            
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita, vuelva cuando quiera....")
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

