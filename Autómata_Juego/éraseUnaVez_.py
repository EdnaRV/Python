Q=['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21','q22','q23','q24','q25','q26']
Sigma=['a','b']
F=['q26']
s='q0'
#diccionario
delta= { ('q0','a') : 'q1',
	 ('q0','b') : 'q1',
	 ('q1','a') : 'q2',
	 ('q1','b') : 'q2',
	 ('q2','a') : 'q3',
	 ('q2','b') : 'q3',
	 ('q3','a') : 'q4',
	 ('q3','b') : 'q4',
	 ('q4','a') : 'q5',
	 ('q4','b') : 'q5',
	 ('q5','a') : 'q6',
	 ('q5','b') : 'q6',
	 ('q6','a') : 'q7',
	 ('q6','b') : 'q7',
	 ('q7','a') : 'q8',
	 ('q7','b') : 'q8',
	 ('q8','a') : 'q9',
	 ('q8','b') : 'q9',
	 ('q9','a') : 'q10',
	 ('q9','b') : 'q10',
	 ('q10','a') : 'q11',
	 ('q10','b') : 'q11',
	 ('q11','a') : 'q12',
	 ('q11','b') : 'q12',
	 ('q12','a') : 'q13',
	 ('q12','b') : 'q13',
	 ('q13','a') : 'q14',
	 ('q13','b') : 'q14',
	 ('q14','a') : 'q15',
	 ('q14','b') : 'q15',
	 ('q15','a') : 'q16',
	 ('q15','b') : 'q16',
	 ('q16','a') : 'q17',
	 ('q16','b') : 'q17',
	 ('q17','a') : 'q18',
	 ('q17','b') : 'q18',
	 ('q18','a') : 'q19',
	 ('q18','b') : 'q19',
	 ('q19','a') : 'q20',
	 ('q19','b') : 'q20',
	 ('q20','a') : 'q21',
	 ('q20','b') : 'q21',
     ('q21','b') : 'q22',
	 ('q21','b') : 'q22',
	 ('q22','a') : 'q23',
	 ('q22','b') : 'q23',
	 ('q23','a') : 'q24',
	 ('q23','b') : 'q24',
	 ('q24','a') : 'q25',
	 ('q24','b') : 'q25',
	 ('q25','a') : 'q26',
	 ('q25','b') : 'q26',
     ('q26','a') : 'q26',
	 ('q26','b') : 'q26',
       
     }
fin = 30

def transicion(estado, sigma):
    global Sigma, delta

    STATUS = True
    if sigma not in Sigma:
        STATUS = False 
        return '',STATUS

    if (estado,sigma) not in delta.keys():
        STATUS=False
        return '',STATUS

    elif ('q0','a') == (estado, sigma): 
        print("Me hará bien para terminar mis últimos reportes para la escuela￼\n")
        print("Es hora de dormir un poco aprovechando la silenciosa noche, así que:\n")
        print("a. Antes alimentaré a mis peces\n")
        print("b. Antes cenaré algo\n")
        estado_siguiente = delta[(estado,sigma)]
        return estado_siguiente, STATUS
        
    
    elif ('q0','b') == (estado, sigma): 
        print("Es rico pero no creo que me mantenga alerta para todas las tareas que tengo que terminar￼\n")
        print("Es hora de dormir un poco aprovechando la silenciosa noche\n")
        print("a. Antes alimentaré a mis peces\n")
        print("b. Antes cenaré algo\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS 
    
    elif ('q1','a') == (estado, sigma): 
        print("Se ven felices")
        print("Después de una semana, estamos la última noche para al fin terminar este curso") 
        print("para concentrarme mejor iré a:")
        print("a. biblioteca")
        print("b. mi escritorio")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q1','b') == (estado, sigma): 
        print("Es mejor cenar que dormir con el estómago vacío") 
        print("Después de una semana, estamos la última noche para al fin terminar este curso") 
        print("para concentrarme mejor iré a:")
        print("a. biblioteca")
        print("b. mi escritorio")
        estado_siguiente = delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q2','a') == (estado, sigma): 
        print("Finalmente a las dos de la mañana terminé y pude dirigirme a mi cuarto a descansar")
        print("a. Dirigirse al cuarto")
        print("b. ir por agua y despues volver al cuarto")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q2','b') == (estado, sigma): 
        print("Finalmente a las dos de la mañana terminé,menos mal que mi cama esta a un lado")
        print("a. Meterse a la cama")
        print("b. Leer un libro y después dormir")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q3','a') == (estado, sigma): 
        print("...en el agua puedo ver las estrellas y puedo dirigirme hacia esa sombra humana, amigable que por alguna razón pareciera que tiene los brazos abiertos .Antes en mis sueños aparecía una silueta que me daba la espalda pero ahora es diferente")
        print("-Sólo fué un sueño: Me repito al levantarme, sin embargo, volviendo a la realidad-")
        print("pude entregar todos mis trabajos a tiempo y tuve muy buenas calificaciones\n")
        print("Sin embargo en esta tarde soleada podré \n")
        print("a. ver a mi amiga")
        print("b. estar sola ")

        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    
    elif ('q3','b') == (estado, sigma): 
        print("pude entregar todos mis trabajos a tiempo y tuve muy buenas calificaciones\n")
        print("Sin embargo en esta tarde soleada podré \n")
        print("a. ver a mi amiga")
        print("b. estar sola ")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q4','a') == (estado, sigma): 
        print("Ha sido una tarde Super divertida con ella")
        print("Ha caído la noche y es hora de descansar\n")
        print("->\n Presiona 'a'")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q4','b') == (estado, sigma): 
        print("No hay tanto que hacer en el cuarto así que solamente me moveré￼ algunas cosas Y aprovecharé para comer algo rico mientras veo una película")
        print("Ha caído la noche y es hora de descansar\n")
        print("->\nPresiona 'a'")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q5','a') == (estado, sigma): 
        print("un libro de empastado azul, Por alguna razón en mi sueño esta silueta me lo dio y ahora que recuerdo creo que tengo un libro parecido que pedí prestado en la biblioteca, entonces al despertar: ")
        print("a. Revisar escritorio\n")
        print("b. revisar repisa\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q5','b') == (estado, sigma): 
        print("un libro de empastado azul, Por alguna razón en mi sueño esta silueta me lo dio y ahora que recuerdo creo que tengo un libro parecido que pedí prestado en la biblioteca")
        print("No hay nada en el escritorio\n")
        print("a. Revisar escritorio\n")
        print("b. revisar repisa\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q6','a') == (estado, sigma): 
        print("No hay nada en el escritorio, buscaré en la repisa... y aquí está")
        print("a.Hojear libro\n")
        print("b.Sacudir libro\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q6','b') == (estado, sigma): 
        print("Bingo! aquí está el libro")
        print("a.Hojear libro\n")
        print("b.Sacudir libro\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q7','a') == (estado, sigma): 
        print("No he visto nada en especial, pero lo agito un poco y cae una hoja")
        print("a.Revisar el reverso de la carta")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q7','b') == (estado, sigma): 
        print("Cayó una hoja que estaba entre sus páginas, tiene nombre de una dirección Y una ubicación")
        print("a.Revisar el reverso de la carta")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q8','a') == (estado, sigma): 
        print("Al parecer dice con un bolígrafo no muy visible. Deje algo para ti en el lugar donde solíamos jugar juntos￼￼, KJ")
        print("... KJ!? Son las iniciales con las que solíamos identificarnos, mi pequeño amigo y yo")
        print("a .Buscar en internet la ubicación")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q8','b') == (estado, sigma): 
        print("Al parecer dice con un bolígrafo no muy visible. Deje algo para ti en el lugar donde solíamos jugar juntos￼￼, KJ ")
        print("... KJ!? Son las iniciales con las que solíamos identificarnos, mi pequeño amigo y yo")
        print("a. Buscar en internet la ubicación")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q9','a') == (estado, sigma): 
        print("recuerdo que mi madre solía visitar a su hermana en aquel pueblo cuando yo tenía siete años￼🟣 Y también tenía una amiga que tenía un hijo y nosotros nos hicimos buenos amigos hasta que se mudaron un día y no le dijeron nada a nadie")
        print("\nMe llena de nostalgia saber que aunque yo ya me había olvidado esos recuerdos por alguna razón él se acuerda de mí, me llena de curiosidad y cómo es que él me encontró después de tanto tiempo")
        print("Presiona 'a' para continuar")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q9','b') == (estado, sigma): 
        print("recuerdo que mi madre solía visitar a su hermana en aquel pueblo cuando yo tenía siete años￼🟣 Y también tenía una amiga que tenía un hijo y nosotros nos hicimos buenos amigos hasta que se mudaron un día y no le dijeron nada a nadie")
        print("\nMe llena de nostalgia saber que aunque yo ya me había olvidado esos recuerdos por alguna razón él se acuerda de mí, me llena de curiosidad y cómo es que él me encontró después de tanto tiempo")
        print("Presiona 'a' para continuar")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q10','a') == (estado, sigma): 
        print("He ahorrado lo suficiente todo este tiempo, Al parecer necesito comprar un boleto de tren para llegar a esa dirección")
        print("a. pedir boletos por internet\n")
        print("b.ir a la estación a comprar boletos\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q10','b') == (estado, sigma): 
        print("He ahorrado lo suficiente todo este tiempo, Al parecer necesito comprar un boleto de tren para llegar a esa dirección")
        print("a. pedir boletos por internet\n")
        print("b.ir a la estación a comprar boletos\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS

    elif ('q11','a') == (estado, sigma): 
        print("Creo que hay oferta, los compraré ahora. \nYa es de mañana así que: ")
        print("\na. Tomé una pequeña maleta con ruedas y salí de casa")
        print("\nCon mi celular es suficiente y quizás un paraguas por si llueve")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q11','b') == (estado, sigma): 
        print("La estacion está cerrada! Buscaré en internet\nYa es de mañana así que:")
        print("\na. Tomé una pequeña maleta con ruedas y salí de casa")
        print("\nCon mi celular es suficiente y quizás un paraguas por si llueve")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q12','a') == (estado, sigma): 
        print("mi tren sale a las ocho am. Miro hacia la ventana la ciudad está tan tranquila. Regresaré lo más pronto posible")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q12','b') == (estado, sigma):
        print("mi tren sale a las ocho am. Miro hacia la ventana la ciudad está tan tranquila. Regresaré lo más pronto posible")
        print("\nhace frío y no empaquemos suerte.")
        print("Presiona 'a' para continuar")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q13','a') == (estado, sigma): 
        
        print("Caminando a un lado del camino encuentro un pequeño gato negro")
        print("a.Buscar unas galletas dentro de mi mochila\n")
        print("b.Acariciarlo\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q13','b') == (estado, sigma): 
        print("Caminando a un lado del camino encuentro un pequeño gato negro")
        print("a.Buscar unas galletas dentro de mi mochila\n")
        print("b.Acariciarlo\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q14','a') == (estado, sigma): 
        print("Al parecer le gustaron")
        print("\ndejé las galletas en el suelo y seguí mi camino pero después de unas cuantas calles me percato que está ahí")
        print("a. Pobrecillo, pero no lo obligaré a ir conmigo asi que continuaré el camio")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q14','b') == (estado, sigma): 
        print("Se ha asustado mejor busco unas galletas dentro de mi mochila")
        print("\ndeje las galletas en el suelo y seguí mi camino pero después de unas cuantas calles me percato que está ahí")
        print("Se ve que es amigable, pero voy a continuar el camino")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q15','a') == (estado, sigma): 
        print("Al parecer hay un puente")
        print("a. Pasar por el puente")
        print("b. Rodear el puente")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q15','b') == (estado, sigma): 
        print("Al parecer hay un puente")
        print("a. Pasar por el puente")
        print("b. Rodear el puente")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q16','a') == (estado, sigma): 
        print("Hay un lago debajo pero está muy alto y entonces me río (estoy asustada)")
        print("a. Continuar caminando")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q16','b') == (estado, sigma): 
        print("Me dan miedo los puentes, es mejor rodearlo")
        print("a. Continuar caminando)
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q17','a') == (estado, sigma): 
        print("ahora solamente tengo que seguir las indicaciones que decía la carta. Después de cruzar ese pueblito me percato que hay más vegetación")
        print("a. Atravesar el camino")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q17','b') == (estado, sigma): 
        print("ahora solamente tengo que seguir las indicaciones que decía la carta. Después de cruzar ese pueblito me percato que hay más vegetación")
        print("a. Atravesar el camino")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q18','a') == (estado, sigma): 
        print("me detengo en una tienda para comprar algo de comer. El camino se ve un poco lejano pero hay árboles por los que puedo caminar sin que me del sol, Después de un rato creo que￼￼a un lado del camino está lleno de girasoles así que continúo")
        print("a. Caminar a lado del camino")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q18','b') == (estado, sigma): 
        print("me detengo en una tienda para comprar algo de comer, El camino se ve un poco lejano pero hay árboles por los que puedo caminar sin que me del sol, Después de un rato creo que￼￼a un lado del camino está lleno de girasoles así que continúo")
        print("a. Caminar derecho")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q19','a') == (estado, sigma): 
        print("finalmente estoy llegando al lugar y por suerte también tengo mi mapa en el celular. Veo que el camino está llegando a su fin y está rodeado por árboles solamente hay algunas piedras￼￼ así que sigo el camino hasta que veo el reflejo de lo que parece ser un lago bastante amplio ")
        print("a.revisar mapa\n")
        print("b.seguir caminando￼￼￼\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q19','b') == (estado, sigma): 
        print("finalmente estoy llegando al lugar y por suerte también tengo mi mapa en el celular. Veo que el camino está llegando a su fin y está rodeado por árboles solamente hay algunas piedras￼￼ así que sigo el camino hasta que veo el reflejo de lo que parece ser un lago bastante amplio ")
        print("a.revisar mapa\n")
        print("b.acercarme caminando por los alrededores\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q20','a') == (estado, sigma): 
        print("Estoy cerca puedo dirigirme a la izquierda￼")
        print("\nhe llegado a lo que parece ser un pequeño pueblo en una pequeña colina. Y ahí está la casa")
        print("a.\n")
        print("b.Tocar la puerta\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q20','b') == (estado, sigma): 
        print("creo que no sé por dónde voy")
        print("\nhe llegado a lo que parece ser un pequeño pueblo en una pequeña colina. Y ahí está la casa")
        print("a.\ntocar la puerta￼")
        print("b.Asomarse por la ventana￼￼￼￼￼\n")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS

    elif ('q21','a') == (estado, sigma): 
        print("al Parecer nadie abre￼")
        print("Hay unas escaleras que llevan más a￼rriba")
        print("a.caminar por las escaleras\n")
        print("b.\nsensentarse a descansar￼￼￼")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q21','b') == (estado, sigma): 
        print("Está cubierta por cortinas￼")
        print("Hay unas escaleras que llevan más a￼rriba")
        print("a.caminar por las escaleras\n")
        print("b.\nsensentarse a descansar￼￼￼")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q22','a') == (estado, sigma): 
        print("Estoy un poco cansada pero subir tal vez me de un panorama más amplio￼")
        print("Entre unos arbustos y piedras está la fuente de agua")
        print("a.\ncaminar rodeando￼￼")
        print("b.\nmeterse al agua")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q22','b') == (estado, sigma): 
        print("￼Al parecer ya no tengo tanta agua así que buscar un lugar para comprar más tarde")
        print("Entre unos arbustos y piedras está la fuente de agua")
        print("a.\ncaminar rodeando￼￼")
        print("b.\nmeterse al agua")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q23','a') == (estado, sigma): 
        print("Es más seguro￼")
        print("\nen la orilla me doy cuenta que el agua está muy cristalina")

        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q23','b') == (estado, sigma): 
        print("Creo que a mi gatito le da miedo así que lo voy a cargar￼")
        print("\nen la orilla me doy cuenta que el agua está muy cristalina")
        print("Presiona 'a' para continuar")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q24','a') == (estado, sigma): 
        print("\nMe inclino para ver mi reflejo cuando siento Una mano qué toca mi hombro")
        print("a.\ngritar")
        print("b.\nlevantarse y correr")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q24','b') == (estado, sigma): 
        print("\nMe inclino para ver mi reflejo cuando siento Una mano qué toca mi hombro")
        print("a.\ngritar")
        print("b.\nlevantarse y correr")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q25','a') == (estado, sigma): 
        print("La persona tapa mi boca y me dice que me￼ Tranquilice y después me suelta￼")
        print("\nOigo que se queja y después me agarra de mis brazos y me dice que todo está bien￼, Soy K")
        print("\nAbro mis ojos sorprendida￼, puedo reconocer esa mirada aún después de tanto tiempo")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q25','b') == (estado, sigma): 
        print("La persona alcanza tomar mi mano￼")
        print("\nOigo que se queja y después me agarra de mis brazos y me dice que todo está bien￼, Soy K")
        print("\nAbro mis ojos sorprendida￼, puedo reconocer esa mirada aún después de tanto tiempo")
        estado_siguiente= delta[(estado,sigma)]
        return estado_siguiente, STATUS

    elif ('q26','a') == (estado, sigma): 
        print("Continuará...")
        estado_siguiente = delta[(estado,sigma)]
        return estado_siguiente, STATUS
    
    elif ('q26','b') == (estado, sigma): 
        print("Continuará...")
        estado_siguiente = delta[(estado,sigma)]
        return estado_siguiente, STATUS    
              
def zero():
    print("Bienvenido, disfruta de esta historia.\n Puedes elegir las acciones correspondientes según las opciones mostradas. Buena Suerte!")
    print("\nEsta tarde la pasamos genial cerca del mar y viendo la puesta de sol espero ver pronto a mis amigos el ciclo escolar que viene￼")
    print("\nLlego a mi cuarto por la noche y aun me faltan unos trabajos.\nPara estudiar podría servirme: \n")
    print("a. Una taza de café \n")
    print("b. una taza de té\n")
    w = input("^-^ ->  ")
    return w

def recorrido(w): 
    estado = s
    while True:
        estado, STATUS = transicion(estado, w)
        if not STATUS:
            break
        if estado == F:
            break
        w = input("^-^ ->  ")
        
    if STATUS != True:
        print("Se ha introducido una cadena incorrecta")
            
            
#w = zero()
#print(w)

if(fin != 0):
    w = zero()
    recorrido(w)
