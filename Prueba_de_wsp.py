import random

'TODOS LOS TEST ESTAN AL FINAL'

token=[',',' ',':','!','?','.','*','>','1','2','3','4','5','6','7','8','9','0','-','/','\n','"']
archivo_a_usar="ChatElectronica.txt" #Poner el nombre de tu archivo acá, recordar tener este archivo y el de chat en la misma carpeta(LA TERMINAL TAMBIEN, debes estar "parado" en esa carpeta)


def top(diccio:dict)->dict:
    lista=[]
    for tuplas in diccio.items():
        lista.append(tuplas)
    lista_ordenada = sorted(lista, key=lambda tupla: tupla[1], reverse=True)
    
    return lista_ordenada



def mensajes_totales(file)->int:
    archivo=open(file,'r', encoding='utf8')
    archivo_legible=archivo.readlines()

    return len(archivo_legible)


#print(mensajes_totales(archivo_a_usar))

'da una lista de las personas con mas mensajes(está seteado en mas de 100, se puede bajar o subir)'
def persona_que_mas_habla(file:str)->dict[str,int]:
    archivo=open(file,'r', encoding='utf8')
    archivo_legible=archivo.readlines()
    archivo_limpio:str=""
    lineas_limpias:list[str]=[]
    nombre=''
    i=17

    dict_con_errores={}
    res={}


    for lineas in archivo_legible:
        i=17
        while i < len(lineas):
            if lineas[i]!= '\n':
                archivo_limpio+=lineas[i]
            else:
                archivo_limpio+=lineas[i]
                lineas_limpias.append(archivo_limpio)
                archivo_limpio=""
            i+=1

    for lineas in lineas_limpias:
        for caracter in lineas:
            if caracter != ':' and  caracter != '\n':
                nombre+=caracter
            elif caracter == '\n':
                nombre=""
            else:
                if nombre not in dict_con_errores.keys():
                    dict_con_errores[nombre]=1
                else:
                    dict_con_errores[nombre]+=1
                nombre=""

    for persona , mensaje  in dict_con_errores.items():
        if mensaje > 100:
            res[persona.lower()]=mensaje

    return res
      
#print(top(persona_que_mas_habla(archivo_a_usar)))

def separar_palabra(linea:str, token:list[str])->list[int]:
    res:list[str]=[]
    palabra:str=""
    for i in linea:
        if i not in token:
            palabra+=i
        else:
            if len(palabra)>0:
                res.append(palabra.lower())
                palabra=""
    if palabra != " ":
        res.append(palabra.lower())
    return res


def miembros(file)->list[str]:
    lista=[]
    nombre_completo=persona_que_mas_habla(file).keys()
    for nombre in nombre_completo:
        lista += (separar_palabra(nombre,token))

    return lista


'lista de palabras mas escritas(steado en 50, podes cambiarlo dependiendo del tamano de tu chat)'
def palabra_mas_dicha(file:str)->dict[str,int]:
    miembros_del_chat:list[str]=miembros(file)    +['<multimedia','omitido']
    archivo=open(file,'r', encoding='utf8')
    archivo_legible=archivo.read()
    lista_de_palabras=separar_palabra(archivo_legible,[',',' ',':','!','?','.','*','>','1','2','3','4','5','6','7','8','9','0','-','/','\n','"'])
    dict_con_errores={}
    res={}


    for palabra in lista_de_palabras:
        if len(palabra)>3 and palabra not in dict_con_errores.keys():
            dict_con_errores[palabra]=1
        elif len(palabra)>3 and palabra in dict_con_errores.keys():
            dict_con_errores[palabra]+=1
  
    for palabras , cantidad  in dict_con_errores.items():
        if cantidad > 50 and palabras not in miembros_del_chat:
            res[palabras]=cantidad
    return res


#print(top(palabra_mas_dicha(archivo_a_usar)))

'Cuantas veces se dijo una unica palabra?'
def contador_de_palabra(file, palabra:str)->int:
    archivo=open(file,'r', encoding='utf8')
    archivo_legible=archivo.read()
    lista_de_palabras=separar_palabra(archivo_legible,[',',' ',':','!','?','.','*','>','1','2','3','4','5','6','7','8','9','0','-','/','\n','"','@'])
    res=0

    for palabras in lista_de_palabras:
        if palabras==palabra:
            res+=1
    return (f"La palabra {palabra}, fue dicha {res} veces")

#print(contador_de_palabra(archivo_a_usar,"toni"))

'Quien dijo mas veces x palabra?'
def cantidad_de_veces_que_lo_dijo(file,palabra:str)->dict:
    archivo=open(file,'r', encoding='utf8')
    archivo_legible=archivo.readlines()
    archivo_en_minusculas=[]
    largo={}
    cantidad={}
    res ={}



    for linea in archivo_legible:
        archivo_en_minusculas.append(linea.lower())

    for persona in persona_que_mas_habla(file).keys():
        for lineas in archivo_en_minusculas:
            if palabra in lineas and persona in lineas:
                if persona not in res.keys():
                    res[persona]=1
                else:
                    res[persona]+=1

    return	res    


#print(top(cantidad_de_veces_que_lo_dijo(archivo_a_usar,"hola")))

'una lista de x cantidad de mensajes random'
def mensaje_random(file,numero)->list[str]:
    archivo=open(file,'r', encoding='utf8')
    archivo_legible=archivo.readlines()
    lineas_limpias=[]
    archivo_limpio=[]
    lista=[]

    for lineas in archivo_legible:
        i=17
        while i < len(lineas):
            if lineas[i]!= '\n':
                archivo_limpio+=lineas[i]
            else:
                lineas_limpias.append(archivo_limpio)
                archivo_limpio=""
            i+=1




    while numero > len(lista):
        i=random.randint(0,len(lineas_limpias))
        if len(lineas_limpias[i])>20:
            lista.append(lineas_limpias[i])
    return lista

#print(mensaje_random(archivo_a_usar,20))

'Promedio de caracteres utilizado por mensaje'
def mensajes_mas_largos(file)->dict:
    archivo=open(file,'r', encoding='utf8')
    archivo_legible=archivo.readlines()
    archivo_en_minusculas=[]
    largo={}
    cantidad={}
    res ={}



    for linea in archivo_legible:
        archivo_en_minusculas.append(linea.lower())

    for persona in persona_que_mas_habla(file).keys():
        for lineas in archivo_en_minusculas:
            if persona in lineas:
                if persona not in largo.keys():
                    largo[persona]=len(lineas)-17-len(persona)
                else:
                    largo[persona]+=len(lineas)-17-len(persona)
                if persona not in cantidad.keys():
                    cantidad[persona]=1
                else:
                    cantidad[persona]+=1
    for integrante in largo.keys():
        res[integrante]=round(largo[integrante]/cantidad[integrante], 2)

    return	res    

#print(top(mensajes_mas_largos(archivo_a_usar)))




# 
# 
# 
# 
# 
'Para usar, solo borrar los # y cambiar las entradas que quieras(archivo_a_usar ya lo seteaste en un comienzo)'
# 
#
#print(mensajes_totales(archivo_a_usar))
#print(top(persona_que_mas_habla(archivo_a_usar)))
#print(top(palabra_mas_dicha(archivo_a_usar)))
#print(contador_de_palabra(archivo_a_usar,"toni"))
#print(mensaje_random(archivo_a_usar,20))
#print(top(mensajes_mas_largos(archivo_a_usar)))
#print(top(cantidad_de_veces_que_lo_dijo(archivo_a_usar,"hola")))