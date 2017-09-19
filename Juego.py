#Juego Text-Based RPG#
print ("""

Buenos días, usuario. Mi nombre es Minerva y soy un software especializado en interacción con humanos.
En esta ocasión, estoy actualizada para la versión 3.1.2 y estoy programada para guiar los primeros estímulos de personas que han sido
puestas en estado de hibernación entre los años 2010 y 2040. Por esta razón, he adoptado el lenguaje de tu tiempo.
Mi objetivo principal es lograr que estos primeros momentos luego de su despertar sean amenos y lo menos confusos que sea posible.

Primero, cuéntame, ¿cuál es tu nombre?""")
Nombre = input()
if Nombre == "Santiago":
    print ("\nOhh. Hmmm. Eso trae muchos recuerdos... En todo caso, tienes un nombre bonito, " + Nombre + ".")
else:
    if len(Nombre) > 15:
        print ("\n¡Wow! Ese es un nombre largo. Espero que no me estés trolleando. Jajajaja. En cualquier caso, me gusta tu nombre " + Nombre + ".")
    else:
        print ("\nTienes un nombre muy bonito, " + Nombre + ".")
print ("""OK. Dejémonos de coqueteos. Recuerda que tu programador te dijo que debes ser profesional, Minerva. Bueno, para ser sincera
""")
