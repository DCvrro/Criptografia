from ctypes import sizeof


def readUsuarios():
    usuarios = list()
    arc = open("user.txt")
    lineas = arc.readlines()
    i = 0
    for lineas in lineas:
        usuarios.append(lineas)
    return usuarios






data = readUsuarios()


#print(data) 
#
#for correos in data:
#    for letra in correos:
#        print(letra)
#        if(letra == ' \n ' or letra == "\n" or letra == " "):
#            letra = ""
#print(data)
