#FUNCIONES 
"""
SON UN BLOQUE DE SINTAXIS QUE HACEN TAREAS QUE SE PUEDEN
DIVIDIR A OTRAS SUBTAREAS.
LAS FUNCIONES SON METODOS QUE ESTAN DEFINADAS DENTRO DE 
UNA CLASE.
SU PRINCIPAL USO ES REUTILIZAR EL CODIGO CUANDO SEA NECESARIO.

"""
#SINTAXIS DE UNA FUNCION

"""
def nombre_funcion():
    -instruciiones de la funcion 
    -return(opcional)
def nombre_funcion(parametros)
    -introducciones de la funcion.
    -return(opcional)
#EJECUCION
-nombre_funcion()
-nombre_funcion(parametros)
"""
#utilidade de una funcion (reutilizacion)
"""
existen funciones predefinidad y funciones propias
"""
print("texto de prueba.")
print("texto de prueba.")
print("texto de prueba.")
print("texto de prueba.\n")

'''
mediante el uso de una funcion 
hacemos que se ejecute n veces 
'''

def texto(): #DECLARACION DE LA FUNCION

    print("texto de prueba.")#CUERPO
    print("texto de prueba.")#DE
    print("texto de prueba.")#LA
    print("texto de prueba.")#FUNCION

texto()# LLAMADA DE LA FUNCION
print("CODIGO FUERA DE FUNCION")
texto()