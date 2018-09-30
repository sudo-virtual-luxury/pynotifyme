# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

def main():
	#req = requests.get("https://www.itescam.edu.mx/portal/avisos.php")
	req = requests.get("http://localhost:8080/xd/notifyme/avisos.php")
	html = BeautifulSoup(req.text, "html.parser")
	avisos = html.find_all('div',{'class':'panel panel-warning'})

	newnotifications = open('newnotifications.txt','w')
	for i, avisos in enumerate(avisos):
		titulo = avisos.find('font').getText().encode('ascii', 'ignore')
		newnotifications.write(titulo + '\n')
	newnotifications.close()

	nn = [''] #Lista con las nuevas notificaciones
	with open('newnotifications.txt') as lineas:
	    for linea in lineas:
			nn.append(linea)

	on = [''] #Lista con las viejas notificaciones
	with open('oldnotifications.txt') as lineas:
	    for linea in lineas:
			on.append(linea)

	contador = 0
	if nn[1]==on[1]:
		contador = 0
	else:
		a = 1
		for i in range(len(nn)):
			if nn[i]!=on[a]:
				contador = contador + 1
			else:
				a = a + 1
		contador = contador - 1


	news = open('new.txt','w')
	news.write("[Announcements: "+ str(contador) + "]")
	news.close()

	oldnotifications = open('oldnotifications.txt','w')
	for i in range(len(nn)):
		titulo = nn[i]
		oldnotifications.write(titulo)
	oldnotifications.close()


main()
