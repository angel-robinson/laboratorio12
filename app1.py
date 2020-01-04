# validar un numero entero positivo

import libreria1

numero_e=libreria1.validar_entero(2)
print(numero_e)
numero_e=libreria1.validar_entero(-2)
print(numero_e)
numero_e=libreria1.validar_entero("hola")
print(numero_e)
#########################################
# validar un numero real

numero_e=libreria1.validar_real(2.0)
print(numero_e)
numero_e=libreria1.validar_real("hola")
print(numero_e)
numero_e=libreria1.validar_real(2)
print(numero_e)

############################################
# validar una cadena de texto

numero_e=libreria1.validar_cadena("hola")
print(numero_e)
numero_e=libreria1.validar_cadena("10")
print(numero_e)
numero_e=libreria1.validar_cadena(10)
print(numero_e)

##############################################
# validar si el valor enviado es un booleano
text=libreria1.validar_booleano("angel")
print(text)
text=libreria1.validar_booleano(False)
print(text)
text=libreria1.validar_booleano(True)
print(text)

###############################################
# validar fecha
fechas=libreria1.validar_fecha("2000-10-80")
print(fechas)

###############################################
# validar dni
dn=libreria1.validar_dni(74286646)
print(" el dn ",dn)

################################################
# validar sexo
sex=libreria1.validar_sexo("masculino")
print(sex)
sex=libreria1.validar_sexo(23)
print(sex)
sex=libreria1.validar_sexo("femenino")
print(sex)

################################################
# validar nombre
nom=libreria1.validar_nombre("ana")
print(nom)
############################################
# validar nota
nota=libreria1.validar_nota(5)
print("la nota es :",nota)

##############################################
# pedir real
real=libreria1.pedir_real("ingrese un numero real:")
print(real)

###############################################
# pedir cadena

cad=libreria1.pedir_cadena("ingrese una cadena:")
print(cad)

#################################################
# pedir booleano
bol=libreria1.pedir_boolean("ingrese un bool:")
print(bol)

#################################################
# pedir sexo
sex=libreria1.pedir_sexo("ingrese(0==mujer o 1==hombre)")
print(sex)

##################################################
# pedir nombre
nom=libreria1.pedir_nombre("ingrese el nombre: ")
print(nom)

##################################################
# pedir telefono
tel=libreria1.pedir_telefono("ingrese el telefono:")
print(tel)

##################################################
# calcular el precio de un producto

precio=libreria1.calcular_precio(2,3)
print(precio)

p=libreria1.calcular_precio_t("Ingrse precio: ","ingrese cantidad: ")
print(p)

###################################################