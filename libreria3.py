def pedir_igv(precio):
    if(isinstance(precio,float) or isinstance(precio,int)):
        if(precio>0):
            return (precio/1.18)*(18/100)
        else:
            return False
    else:
        return False

def calcular_igv(msg):
    n=-1
    while(pedir_igv(n)==False):
        n=input(msg)
        return pedir_igv(n)
