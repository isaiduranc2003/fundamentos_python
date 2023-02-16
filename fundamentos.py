#comentarios
#´´´cometarios 
#varias lineas´´´
#pass para que la funcion no realize nada
def nuevoTema(tema):
    print("\n-------",tema,"-------")

print("hola mundo python")

print("---- Operadores aritmeticos----")

print("operador division entero (10 // 3) =",10//3)
print("operador potencia (5 ** 3): ",5**3)


print("---- Operadores logicos----")
print("operador and (True and False) =",True and False)

#Actividad 1: imprimir la tabla de verdad de los operadores logicos
print(" ")
print("Actividad 1: imprimir la tabla de verdad de los operadores logicos")

#tabla and
print("tabla and:")
print("operador and (True and True) =",True and True)
print("operador and (True and False) =",True and False)
print("operador and (False and True) =",False and True)
print("operador and (False and False) =",False and False)

#tabla not
print("tabla not:")
print("operador and (not True) =",not True)
print("operador and (not False) =",not False)

#tabla or
print("tabla or:")
print("operador and (True or True) =",True or True)
print("operador and (True or False) =",True or False)
print("operador and (False or True) =",False or True)
print("operador and (False or False) =",False or False)


#print("---operadores decomparacion---")
#print("2 == 3", 2 == 3)

#Actividad 2: Agregar los demas operadores de comparacion
print(" ")
nuevoTema("operadores de comparacion")
#print("-----operadores de comparacion-----")
print("Actividad 2: Agregar los demas operadores de comparacion")
print("2 == 3", 2 == 3)
print("2 != 3", 2 != 3)
print("2 < 3", 2 < 3)
print("3 <= 3", 3 <= 3)
print("2 > 3", 2 > 3)
print("7 >= 3", 7 >= 3)

#variables validas
#las variables son sensibles a las mayusculas
nuevoTema("variables")
variable1 = 10
variable2 = 6.2456
variable3 = "swerkd"
dosPalabras = "hola"
dos_palabras = "hello"

print(variable1,variable2,variable3,dosPalabras,dos_palabras)

a,b,c=15,5.16,"Una palabra"
print(a,b,c)

nuevoTema("Enteros")
w=165
x=8367386328748237
y=765
z=0b00110011
h=0xffa

print(w,type(w))
print(x,type(x))
print(y,type(y))
print(z,type(z))
print(h,type(h))

nuevoTema("Flotantes")
x=1297.50
print(x,type(x))
y=0.50594
print(y,type(y))

nuevoTema("Numeros complejos")
x=-46j
y= 12+45j
z= 2j
print(x,type(x))
print(y,type(y))
print(z,type(z))

#bool regresara si tiene un dato valido
nuevoTema("Booleanos")
lis=[]
print(lis,"es",bool(lis))

t=()
print(t,"es",bool(t))

new="Hello"
print(new,"es",bool(new))

num=99
print(num,"es",bool(num))

comp= 0+0j
print(comp,"es",bool(comp))

val= None #None equivale a Null
print(val,"es",bool(val))


nuevoTema("listas en python") #no son arreglos
a = [10,20.5,"lista de ptyhon"]
print(a)
print(a[1]) #para imprimir solo la posicion deseada
a[0]="Q onda"
print(a)

nuevoTema("Tuplas") #es lo mismo que las listas pero no se pueden modificar los datos (son inmutables)

t=(25,"Tupla",1+20j,3.1416)
print(t)
print("t[1]",t[1])
print("t[0:3]",t[0:3])
#t[1]=28 no se puede realizar en tuplas



#tarea
nuevoTema("Conjuntos")
t = {50,20,30,40,10}
print("Conjunto t=", t)

nuevoTema("Diccionarios")
d = {1:"valor1","valor2":2j}
print(d, type(d))

nuevoTema("Cadenas")
cadena1 = "Cadena con comillas dobles"
cadena2 = 'Cadena con comillas simples'

print(cadena1, type(cadena1))
print(cadena2, type(cadena2))
