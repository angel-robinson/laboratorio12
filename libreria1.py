# validar un numero entero
def validar_entero(numero):
    # el numero tiene que tener digitos
    if (isinstance(numero,int)):
        if (numero>=0):
            # el numero tiene que ser entero positivo
            return True
        else:
            return False

    # si no tiene digitos retorna False
    else:
        return False

########################################################

# validar un real

def validar_real(numero):
    # el numero tiene que tener digitos
    if (isinstance(numero,float)):
        if (numero>=0.0):
            # el numero tiene que ser entero positivo
            return True
        else:

            if (isinstance(numero,int)):
                return False

    # si no tiene digitos retorna False
    else:
        return False


def validar_cadena(cadena):
    # la cadena tiene que estar de letras
    if (isinstance(cadena,str) and cadena.isdigit()==False):
        if (len(cadena)>0):
            # la cadena tiene que ener mas de una palabra
            return True
        else:
            return False

    # si no es del tipo str devuelve False
    else:
        return False

def validar_booleano(msg):
    if(msg==bool(msg)):
        return True
    else:
        return False

def validar_fecha(fecha):

    # la fecha tiene que tener numeros enteros
    if (isinstance(fecha,str)):
        if (len(fecha)==10):

            if (int(fecha[0:4])>=2000):

                return True
            if (int(fecha[6:8])>0 and int(fecha[6:8])<13):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    # la longitud de la fecha es 10
    # la fecha tiene formato "YYYY-MM-DD"

def validar_dni(dni):
    # verificar si es un numero
    if(isinstance(dni,int) or isinstance(dni,str)):
        if(dni>9999999 and dni<888888888):
            return True
    else:
        return False
    # tiene que tener 8 digitos

#######################################
# pedir sexo
def validar_sexo(sexo):
    if(sexo==0):
        return "mujer"
    if(sexo==1):
        return "hombre"
    else:
        return False

def pedir_sexo(msg):
    n=-1
    while(validar_sexo(n)==False):
        n=input(msg)
        if(int(n)==0):
            return "mujer"
        if(int(n)==1):
            return "hombre"

        if(isinstance(n,str)):
            return False








def validar_nombre(nombre):
    # tiene que ser un str
    if(isinstance(nombre,str) and len(nombre)>=3):
        if(nombre.isalnum()==True):
            return False
        else:
            return True
    else:
        return False

def validar_nota(nota):
    if(isinstance(nota,float)):
        if(nota>=0.0 and nota<=20.0):
            return True
        else:
            return False

    else:
        return False
###################################################
# pedir real
def pedir_real(msg):
    n=-1
    while(validar_real(n)==False):

        n=float(input(msg))
        while(n<0):
            n=float(input(msg))
        return n

#################################################
# pedir cadena

def pedir_cadena(cadena):
    cadena_invalida=True
    while(cadena_invalida):
        cadena_invalida=str(input(cadena))
        while(len(cadena_invalida)<=3):
            cadena_invalida=str(input(cadena))
        return cadena_invalida
    return float(cadena)

#####################################################
# pedir booleanno
def pedir_boolean(msg):
    boolean_invalido=True
    n=""
    while(boolean_invalido):
        n=input(msg)
        if(n=="True" or n=="False"):
            return True
        else:
            return False
    return n
#######################################################
# pedir nombre
def validar_nombres(msg):
    if(isinstance(msg,str)):
        if(len(msg)>=3):
            return True
        else:
            return False

    else:
        return False
def pedir_nombre(msg):
    n=-1
    while(validar_nombres(n)==False):
        n=input(msg)
        return n
########################################################
#pedir telefono
def validar_telefono(msg):
    if (isinstance(msg,str)):

        return True
    else:
        return False


def pedir_telefono(msg):
    n=-1
    while(validar_telefono(n)==False):
        n=input(msg)
        if (len(n)==9 and n.isdigit()==True):
            return n
        else:
            return "nooo es:"

##############################################
# pedir nota

def validar_notas(nota):
    if(isinstance(nota,float) or isinstance(nota,int)):
        if(nota>=0 and nota<=20):
            return True
        else:
            return False
    else:
        return False
##############################################################
# calcular el precio de un producto
def calcular_precio(precio_u,cantidad):
    if(isinstance(precio_u,float) and isinstance(cantidad,int)):

        if(float(precio_u)>0 and int(cantidad)>0):
            return float(precio_u)*int(cantidad)
        else:
            return False
    else:
        return False

def calcular_precio_t(msg1,msg2):
    n=-1
    m=-1
    while(calcular_precio(n,m)==False):
        n=input(msg1)
        m=input(msg2)
        return calcular_precio(n,m)





