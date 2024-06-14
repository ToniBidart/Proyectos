import random

'TODOS LOS TEST ESTAN AL FINAL'

token=[',',' ',':','!','?','.','*','>','1','2','3','4','5','6','7','8','9','0','-','/','\n','"']
archivo_a_usar="ChatTDB.txt" #Poner el nombre de tu archivo acá, recordar tener este archivo y el de chat en la misma carpeta(LA TERMINAL TAMBIEN, debes estar "parado" en esa carpeta)


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

def año_mas_activo(file)->dict[str,int]:
    archivo=open(file,'r', encoding='utf8')
    archivo_legible=archivo.readlines()
    año=0
    res={}
    dict_con_errores={}
    for lineas in archivo_legible:
        año=0
        if len(lineas)>7:
            año=lineas[6]+lineas[7]
            if  año not in dict_con_errores.keys():
                dict_con_errores[año]=1
            else:
                dict_con_errores[año]+=1
    for ano, cantidad in dict_con_errores.items():
        if cantidad>25:
            res[ano]=cantidad
    return res

#print(top(año_mas_activo(archivo_a_usar)))
'Minimo 5msjs se puede cambiar'
def mes_mas_activo(file)->dict[str,int]:
    archivo=open(file,'r', encoding='utf8')
    archivo_legible=archivo.readlines()
    mes=0
    res={}
    dict_con_errores={}
    for lineas in archivo_legible:
        mes=0
        if len(lineas)>7:
            mes=lineas[3]+lineas[4]+lineas[5]+lineas[6]+lineas[7]
            if  mes not in dict_con_errores.keys():
                dict_con_errores[mes]=1
            else:
                dict_con_errores[mes]+=1
    for dias, cantidad in dict_con_errores.items():
        if cantidad>1000:
            res[dias]=cantidad
    return res

#print(top(mes_mas_activo(archivo_a_usar)))

'Minimo 50msjs se puede cambiar'
def dia_mas_activo(file)->dict[str,int]:
    archivo=open(file,'r', encoding='utf8')
    archivo_legible=archivo.readlines()
    dia=0
    res={}
    dict_con_errores={}
    for lineas in archivo_legible:
        dia=0
        if len(lineas)>7:
            dia=lineas[0]+lineas[1]+lineas[2]+lineas[3]+lineas[4]+lineas[5]+lineas[6]+lineas[7]
            if  dia not in dict_con_errores.keys():
                dict_con_errores[dia]=1
            else:
                dict_con_errores[dia]+=1
    for dias, cantidad in dict_con_errores.items():
        if cantidad>500:
            res[dias]=cantidad
    return res

#print(top(dia_mas_activo(archivo_a_usar)))

def dias_de_asistencia(file)->dict:
    archivo=open(file,'r', encoding='utf8')
    archivo_legible=archivo.readlines()
    arc=[]
    lista_del_dia=[]
    lista_de_personas=persona_que_mas_habla(file).keys()
    cantidad_de_dias=0
    numeros=['0','1','2','3','4','5','6','7','8','9']
    res={}

    for lineas in archivo_legible:
        arc.append(lineas.lower())

    for i in range(len(arc)-1):
        if len(arc[i]) >7  and len(arc[i+1]) > 7:
            if (arc[i][0]+arc[i][1]+ arc[i][2]+arc[i][3]+ arc[i][4]+arc[i][5]+ arc[i][6]+arc[i][7] ) == (arc[i+1][0]+arc[i+1][1]+ arc[i+1][2]+arc[i][3]+ arc[i+1][4]+arc[i+1][5]+ arc[i+1][6]+arc[i+1][7]):
                for persona in lista_de_personas:
                        if persona in arc[i] and persona not in lista_del_dia:
                            lista_del_dia.append(persona)
            else:
                if arc[i-1][0] in numeros:
                    cantidad_de_dias+=1
                    for nombres in lista_del_dia:
                        if nombres in lista_de_personas and nombres in res.keys():
                            res[nombres]+=1
                            lista_del_dia=[]
                        elif nombres in lista_de_personas and nombres not in res.keys():
                            res[nombres]=1
                            lista_del_dia=[]

    return res

#print(top(dias_de_asistencia(archivo_a_usar)))


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
#print(contador_de_palabra(archivo_a_usar,"hola"))
#print(mensaje_random(archivo_a_usar,5))
#print(top(mensajes_mas_largos(archivo_a_usar)))
#print(top(cantidad_de_veces_que_lo_dijo(archivo_a_usar,"sparvoli")))
''''''''''''''''''''''''''''''''''''''''''
'Si queres verlo en orden, sacar el "top()"'
#print(top(año_mas_activo(archivo_a_usar)))
#print(top(mes_mas_activo(archivo_a_usar)))
#print(top(dia_mas_activo(archivo_a_usar)))

#print(top(dias_de_asistencia(archivo_a_usar)))
