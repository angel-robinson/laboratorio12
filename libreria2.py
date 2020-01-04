########################################
def validar_entero(entero):
    if (isinstance(entero,int)):
        if(entero>=0):
            return True
        else:
            return False
    else:
        return False

def pedir_entero(msg):
    n=-1
    while(validar_entero(n)==False):
        n=int(input(msg))
        while(n<0):
            n=int(input(msg))
        return n

##########################################

def validar_booleano(msg):
    if(msg==bool(msg)):
        return True
    else:
        return False

#def pedir_booleano(booleano):
#    b=True
#    while(b):
#        b=bool(input(booleano))
#        return bool(b)

#############################################
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
def validar_nota(msg):
    if(isinstance(msg,float)):
        if(msg>=0.0 and msg<=20.0):
            return msg
        else:
            return False
    else:
        return False