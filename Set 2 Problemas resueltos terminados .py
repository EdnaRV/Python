w = "ornitorrinco"
w2 = 'especial'

print("#1")
tam= print('tamaño de cadena', len(w))

'''
print("#2")

#por cada letra en cadena ->  agrega a set y cuenta si hace match con otro recorrido

freq= {}
for x in range(0, len(w)):
    freq.count(w[x])
    
print(freq)
elements= w.split()
print(elements)   

wUnica= set()
c= list()
for i in w:
    wUnica.add(i)
print(wUnica)

#cuantas veces esta letra en string
c= w.count(wUnica[0])
print(wUnica[0] + c)

from collections import Counter

def split_word(word):
    w_new = []
    for i in w:
        w_new.append(i)
    return w_new

w_new= split_word('ornitorrinco')
print(w_new)

Counter(w_new)
print(Counter)

for leter in w:
    for i in w:
        if leter == i:
            count =+ 1

print()


print("-------------2-------------------")
repetition = dict()
for i in w:
    for j in w:
        if i == j:
            c =+ 1
            repetition[i] = (c)
print(repetition)
            #print(i, count)
'''
print("#2")
wlist= list(w)
print(wlist)     
      

print("#3")
w_new= w[:2] + w[-2:]
if len(w_new) <= 2:    
    print('cadena vacia')
else:
    print(w_new)

print("#4")
begin= w[0]
new_word2= begin

for c in w:
    if c == begin and w[0] != begin:
        new_word2 += '$' 
    elif c != begin:
        new_word2 += c 
              
print(new_word2)

print("#5")

wCont= w+ '_' + w2
print(wCont)

print("#6")

fruta="coco";
cacho=fruta[0];

if cacho in fruta:
	print(fruta.replace(cacho,"$"))
#----------------------------------
def short_word():
    if len(w) >= len(w2):
        return w 
    else:
        return w2

sw= short_word()
print(sw , " is longer")

print("#7")
w_new = []
c_position = 2
for c in range(0, len(w)):
    if c != c_position:
        w_new += w[c]
    else:
        w_new == ' '
print(w_new)

print("#8")
w_new= []
w_first = w2[ : 1 ]
w_last = w2[-1 : ]
print(w_first, w_last)
for i in w2:
    if i == w_first:
        w_new += w_last
    elif i == w_last:
        w_new += w_first
    else: 
        w_new += i
print(w_new)

print("#9")
cadena="politecnico"
tam=len(cadena)

for x in range(0,tam):
	num=x%2
	if num==0:
		print(cadena[x],end = '')

print("#10")
phrase = 'What does one person give to another? He gives of himself, of the most precious he has, he gives of his life. This does not necessarily mean that he sacrifices his life for the other—but that he gives him of that which is alive in him; he gives him of his joy, of his interest, of his understanding, of his knowledge, of his humor, of his sadness—of all expressions and manifestations of that which is alive in him. In thus giving of his life, he enriches the other person, he enhances the others sense of aliveness by enhancing his own sense of aliveness. He does not give in order to receive; giving is in itself exquisite joy. But in giving he cannot help bringing something to life in the other person, and this which is brought to life reflects back to him.'
tokens = phrase.split(' ')
count = 0
for i in tokens:
    if i == 'person':
        count += 1
print('give was written ', count, 'times')
        




print("#11")
frase=input("hola, ingrese una frase \n")

m=frase.lower()
M=frase.upper()
print(m)
print(M)

print("#12")
days ='lunes, martes, miercoles, jueves, viernes, sabado, domingo'
tokens = days.split(",")
set_tokens= list(set(tokens))
set_tokens.sort()
print(set_tokens)

print("#13")
cadena = 'kiwi'
r= cadena[-2:]
final=r+r+r+r
print(final)

print("#14")
cad1="parangaricutirimicuaro"
cad2="ola"
tc2=len(cad2)
principio=cad1[3:]

if(tc2 < 4):
	print(cad2)
else:
	print(principio)
    
print("#15")
frase="hola"
tam=len(frase)
num= tam%2

if num==0:
	print(frase[:2])

print("#16")
c1="piano"
c2="guitarra"
c3="flauta"
c4="conquistando!"

tam=len(c4)
print(tam)
if tam%13 ==0:
	print(c4[::-1])
    
print("#17")
w = 'ReinoUnido'

def w_upper(w):
    cont = 0
    for i in range(0, len(w)):
        if w[i].isupper() == True :
            cont += 1
            if cont >= 2:
                print('mayus')
                return w.upper()

w_upper = w_upper(w) 
print(w_upper)

print("#18")
abc="alga"

ordenado=sorted(abc)
print(ordenado)

print("#19")
inicio="a"

cadena="alfabeto"

check=cadena[:1]

if check in inicio:
	print("La palabra inicia con 'a'")
else:
	print("La palabra no inicia con 'a'")


print("#20")
abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
code=["lunesjuevestorrelatino"]
size=len(code)
step=range(3,size,1)

print(code[3:])

for i in code:
	print(abc)
	print("hi")
	
print("sali")

for i in range(0,3):
	for j in range(0,3):
		if j==2:
			print(i,j)
	
print("21")
words=["Luna","Felicidad","Brisa",]
for ob in words:
	print("La "+ob +".")
print("22")
lista=0.234354657,34.234,214
for rec in lista:
	print("%.2f" %rec)

print("23")

num=12.3,-452,435254.342

for ob in num:
	print(f'Signo: {ob:+}')

print("24")
lista=0.234354657,34.234,214
for rec in lista:
	print("%.0f" %rec)

print("25")

print("---------------------------------------------")
w = 'institucion'
cad = 'a,e,i,o,u'
new =""
for c in w:
    if not(c in cad):
        new += c
print(new)
'''
#******************************* M
#25
ceros = range(0,100)
n= 500
new_n = list(map(int, str(n)))
print(new_n)
for i in range(0,100):
    final_n = new_n.insert(0,7)
    
    final_n = ['0'] + [new_n +1]
print(final_n)

#26
ancho = [4]
ast = 5
s= []
for i in range(0, ast):
    s = ancho.append['*']
print(s)

'''


print("41")#. Escriba un programa de Python para dividir una cadena en la última aparición del delimitador dado.  

w = 'ornitorrinco' 
caracter = 't' 
for i in range(0,len(w)): 
    if w[i] == caracter: 
        print(w[i: ]) 

 

print("42")#Escriba un programa Python para obtener la última parte de una cadena antes de un carácter especificado.  

w = 'ornitorrinco' 
caracter = 'n' 
for i in range(0,len(w)): 
    if w[i] == caracter: 
        print(w[i-1 : i+1]) 

print("43")
#incluye cadena vacia
w= 'ESCOM'
for i in range(len(w)):
        print(w[:i])
        print(w[i:])
        print(w[1:i])



















