# LONGITUD DE UNA FRASE

# Sección de bienvenida al usuario.
print('¡Vamos a crear una contraseña!')
print()
print("A continuación, ingresa 3 palabras diferentes que contengan entre 4 y 8 caracteres")
print()

# Variables a utilizar.
registros = 0
palabras = 3

# Bloque de lógica y comparación.
while palabras > 0 :

    if palabras == 3 :
          
        palabra1 = input("Ingresa la primera palabra: ")
        longitud1 = len(palabra1)
        if longitud1 <= 4 or longitud1 >9 :
          print("La palabra es correcta.")
        elif longitud1 < 4:
          print(f"La palabra que has ingresado no cuenta con el mínimo requerido, tiene {longitud1} caractéres.")
          continue
        elif longitud1 > 8:
          print(f"La palabra que has ingresado excede el máximo permitido, tiene {longitud1} caractéres.")
          continue
        palabras -= 1
        registros += 1
    
    elif palabras == 2 :
       
        palabra2 = input("Ingresa la segunda palabra: ")
        longitud2 = len(palabra2)
        if longitud1 <= 4 or longitud1 >9:
          print("La palabra es correcta.")
        elif longitud2 < 4:
          print(f"La palabra que has ingresado no cuenta con el mínimo requerido, tiene {longitud2} caractéres.")
          continue
        elif longitud2 > 8:
          print(f"La palabra que has ingresado excede el máximo permitido, tiene {longitud2} caractéres.")
          continue
        palabras -= 1
        registros += 1

    elif palabras == 1 :
    
       palabra3 = input("Ingresa la tercera palabra: ")

       longitud3 = len(palabra3)
       if longitud1 <= 4 or longitud1 >9:
        print("La palabra es correcta.")
       elif longitud3 < 4:
        print(f"La palabra que has ingresado no cuenta con el mínimo requerido, tiene {longitud3} caractéres.")
        continue
       elif longitud3 > 8:
        print(f"La palabra que has ingresado excede el máximo permitido, tiene {longitud3} caractéres.")
        continue
       palabras -= 1
       registros += 1

while registros == 3 :
  password = palabra1 [1] + palabra2 [3] + palabra3 [2] + palabra1 [3] + palabra2 [0] + palabra3 [1]
  print('la contraseña es: ', password)
  registros = 0
  contraseña = password  
for _ in range (3):
       print('Tu contraseña son las letras: P1(1), P2(3), P3(2), P4(3), P5(0), P6(1) de tus palabras ingresadas')
       print()
       contraseña_usuario = input('Favor de ingresar la contraseña creada: ')   
       if contraseña_usuario == contraseña:
        print('Lograste descifrar la contraseña con éxito', '😀')
        exit()
       elif contraseña_usuario != contraseña:
        print('Lo sentimos, inténtalo nuevamente', '☹️')  
print('fin')    

################################################################################################################

# ENCUENTRA EL CUADRANTE

# Sección de bienvenida y opción a participar.
print('¡Encuentra el cuadrante!')

# Variable a utilizar.
opcion = 0

opcion = int(input('¿Desea participar? 1(si)/ Otro(no): '))

print('Usted ha seleccionado', (opcion))

while opcion == 1:
    print('¡Bienvenido!')
    print('A continuación seleccionarás un valor para X y uno para Y, ¡Puedes introducir valores con punto decimal y negativos!')
    
    # Se da la opción de ingresar valores para los 4 cuadrantes; al terminar se cierra el programa.
    for _ in range (4):
        x = float(input("Ingrese X: "))
        y = float(input("Ingrese Y: "))
        if x == 0 or y == 0:
          print("Una o ambas valores ingresados son cero; ingresa valores diferentes.")
        else:
          if x > 0 and y > 0:
            print("Este punto se encuentra en el cuadrante I.")
          elif x < 0 and y > 0:
            print("Este punto se encuentra en el cuadrante II.")
          elif x < 0 and y < 0:
            print("Este punto se encuentra en el cuadrante III.")
          else:
            print("Este punto se encuentra en el cuadrante IV.")
          opcion = 0 
else :
  print('¡Que tenga un excelente día!')