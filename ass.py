import libreria2
assert (libreria2.validar_nota(12)==False)
assert (libreria2.validar_nota(5.8)==True)
assert (libreria2.validar_nota("hola")==False)
assert (libreria2.validar_nota("12")==False)
assert (libreria2.validar_nota(24)==False)