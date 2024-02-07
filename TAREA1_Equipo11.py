#AUTOR: Equipo 11
#FECHA: 06/02/2024
import math
import os

#Diccionario de los valores definidos para A --> F
#"Valor decimal": "Valor hexadecimal"
decimal_hexadecimal = {
  10: "A",
  11: "B",
  12: "C",
  13: "D",
  14: "E",
  15: "F",
}

#"Valor hexadecimal": "Valor decimal"
hexadecimal_decimal = {
  "A": 10,
  "B": 11,
  "C": 12,
  "D": 13,
  "E": 14,
  "F": 15,
}

#Declaracion variables
base_origen = 0
valor_origen = ""
base_destino = 0
valor_intermedio = []

#FUNCIONES
#se realizan las peticiones de datos, y se comprueba la integridad de los valores ingresados
def recibir_datos():
    global base_origen
    global valor_origen
    global base_destino

    print("\n\n /// CONVERSION DE BASE A BASE ///\n")
    try:
      
      #Pedir y verificar la base de origen
      while(True):
        base_origen= int(input("\nDame la base de origen (2-16): "))
        if ((base_origen < 2) or (base_origen > 16)):
          print("\nError: Valor de base incorrecto\n")
        else: break
          
      #Pedir y verificar el valor de la base de origen
      bandera = 1
      while(bandera == 1):
        bandera = 0
        valor_origen = str(input("\nDame el valor de la base de origen (Acepta 0,...,9,A,...,F): "))
        #Revisar que los valores son validos
        for x in valor_origen:
          if ((x > 'F') and (x != '.')):
            bandera = 1
            print("\nError: Valor incorrecto\n")
            break
        if bandera != 1:
          #Revisar que los valores son validos
          for x in valor_origen:
            #Si no encuentra el valor, regresa '1'
            if (x != '.') and (((hexadecimal_decimal.get(x, 1) == 1) and (int(x) >= base_origen)) or (hexadecimal_decimal.get(x, 1) >= base_origen)):
              bandera = 1
              print("\nError: Valor incorrecto\n")
              break
      
      #Pedir y verificar la base de destino
      while(True):
        base_destino= int(input("\nDame la base de destino (2-16): "))
        if ((base_destino < 2) or (base_destino > 16)):
          print("\nError: Valor de base incorrecto\n")
        elif base_destino == base_origen:
          print("\nError: Mismas bases (origen y destino)\n")
        else: break
      
      return True
    except ValueError:
        return False
  
def decimal_base(valor_intermedio):
  global base_origen
  global valor_origen
  global base_destino
  
  #Parte entera
  sumatoria = ""
  cociente_residuo = divmod(int(valor_intermedio[0]), base_destino)
  if decimal_hexadecimal.get(cociente_residuo[1],1) !=1:
    sumatoria = sumatoria+str(decimal_hexadecimal.get(cociente_residuo[1],1))
  else: sumatoria = sumatoria+str(cociente_residuo[1])
  #sumatoria = sumatoria+str(cociente_residuo[1])
  
  while cociente_residuo[0] != 0:
    cociente_residuo = divmod(cociente_residuo[0], base_destino)
    if decimal_hexadecimal.get(cociente_residuo[1],1) !=1:
      sumatoria = sumatoria+str(decimal_hexadecimal.get(cociente_residuo[1],1))
    else: sumatoria = sumatoria+str(cociente_residuo[1])
  sumatoria = sumatoria[::-1]

  #Parte decimal
  contador_decimal = 0
  parte_decimal = float("0."+valor_intermedio[1])*base_destino
  sumatoria = sumatoria+"."
  while contador_decimal < 2 and int(valor_intermedio[1]) != 0:
    
    if decimal_hexadecimal.get(math.trunc(parte_decimal),1) !=1:
      sumatoria = sumatoria+str(decimal_hexadecimal.get(math.trunc(parte_decimal),1))
    else: sumatoria = sumatoria+str(math.trunc(parte_decimal))
    
    #sumatoria = sumatoria+str(math.trunc(parte_decimal))
    if math.trunc(parte_decimal) >= 1:
      contador_decimal = contador_decimal+1
    parte_decimal = parte_decimal - math.trunc(parte_decimal)
    parte_decimal = parte_decimal*base_destino

  return str(sumatoria)

def base_decimal():
  global base_origen
  global valor_origen
  global base_destino
  global valor_intermedio
  
  #Parte entera
  sumatoria = 0
  i = 0
  valor_intermedio[0] = valor_intermedio[0][::-1]
  for x in valor_intermedio[0]:
    
    if hexadecimal_decimal.get(x,1) !=1:
      sumatoria += (hexadecimal_decimal.get(x,1))*(base_origen**i)
    else:
      sumatoria += (int(x))*(base_origen**i)
    
    i = i+1
  
  #Parte decimal
  i = -1
  for x in valor_intermedio[1]:
    
    if hexadecimal_decimal.get(x,1) !=1:
      sumatoria += (hexadecimal_decimal.get(x,1))*(base_origen**i)
    else:
      sumatoria += (int(x))*(base_origen**i)
    
    i = i-1
  
  return str(sumatoria)

menu = 0
while (menu == 0):
  if recibir_datos() == False:
    print("\nError: No se aceptan valores no enteros")
    menu = 0
  elif base_origen == 10:
    valor_intermedio = valor_origen.split('.')
    valor_intermedio.append("0")
    print("\n\n EL VALOR CONVERTIDO A BASE {} ES: {}".format(base_destino, decimal_base(valor_intermedio)))
    menu = 1
  elif base_destino == 10:
    valor_intermedio = valor_origen.split('.')
    valor_intermedio.append("0")
    print("\n\n EL VALOR CONVERTIDO A BASE {} ES: {}".format(base_destino, base_decimal()))
    menu = 1
  else:
    valor_intermedio = valor_origen.split('.')
    valor_intermedio.append("0")
    valor_intermedio = base_decimal().split('.')
    valor_intermedio.append("0")
    print("\n\n EL VALOR CONVERTIDO A BASE {} ES: {}".format(base_destino, decimal_base(valor_intermedio)))
    menu = 1
  while menu == 1:
    try:
      menu = int(input("\n¿Deseas ingresar otro valor? (1 = SI, 0 = NO): "))
      if menu == 0: 
        menu = 1
        break
      elif menu == 1:
        menu = 0
        os.system ("cls")
        break
    except ValueError:
      print("\nError: solo se acepta '1' o '0'")
  