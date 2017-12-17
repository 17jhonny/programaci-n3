ingles = ["I","AM","VERY","TIRED","JESUS","LOVE","YOU"]
espanol = ["YO","ESTOY","MUY","CANSADO","JESUS","AMA","TE"]
dicho = raw_input("INGRESE LA FRASE\n")
lista=dicho.split()
traducido=[]
for i in range(len(lista)):
	traducido.append(ingles[espanol.index(lista[i])])
palabra_traducida1 =' '.join(traducido)	

dicho2 = raw_input("INGRESE LA FRASE2\n")
lista2=dicho2.split()
traducido2=[]
for i in range(len(lista2)):
	traducido2.append(ingles[espanol.index(lista2[i])])
palabra_traducida2 =' '.join(traducido2)
print "TRADUCIDO EN INGLES"	
print(palabra_traducida1)
print(palabra_traducida2)