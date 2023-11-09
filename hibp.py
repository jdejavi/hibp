#!/usr/bin/env python3

from sys import *
from time import *
import requests
from urllib.parse import quote
from progress.bar import *
'''
Script que te dice que usuarios de un dominio en concreto se han visto comprometidos en alguna brecha de seguridad
	--> Ralizado por Javier Matilla Martín aka m4t1
'''

#Variables globales
lista_dominios = []
header_api_key = {
	"hibp-api-key": "[API_KEY]"
}
base_url = f'https://haveibeenpwned.com/api/v3/breacheddomain/'
correos_breached = []

banner = """
 ____  ____  _____  ______   _______   
|_   ||   _||_   _||_   _ \ |_   __ \  
  | |__| |    | |    | |_) |  | |__) | 
  |  __  |    | |    |  __'.  |  ___/  
 _| |  | |_  _| |_  _| |__) |_| |_     
|____||____||_____||_______/|_____|    
"""                                       


def extraeDatosBrechas(lista_correos):

	base_url_acc = f'https://haveibeenpwned.com/api/v3/breachedaccount/'
	bar = Bar('Tratando correos', max=len(lista_correos))
	
	for i in range(len(lista_correos)):
		bar.next()
		url_acc = f'{base_url_acc}{quote(lista_correos[i])}?truncateResponse=false'
		res = requests.get(url_acc, headers=header_api_key)
		
		if res.status_code == 200:
			with open("resultados_hibp.txt","a") as resultados:
				resultados.write(lista_correos[i].strip() + '\n')
				
				for j in range(len(res.json())):
					cadena_nombre = f'Nombre de la brecha\t\t\t\t\t   --> {res.json()[j]["Name"]}'
					cadena_brecha = f'Fecha de la brecha\t\t\t\t   --> {res.json()[j]["BreachDate"]}'
					cadena_add = f'Fecha de adición la brecha\t\t\t--> {res.json()[j]["AddedDate"]}'
					
					data='Datos filtrados\t\t\t\t\t   --> '
					for d in res.json()[j]["DataClasses"]:
						data += f'{d},'
						
					if data.endswith(','):
						data = data[:-1]
					
					resultados.write('\t'+cadena_nombre.strip() + '\n')
					resultados.write('\t\t'+cadena_brecha.strip() + '\n')
					resultados.write('\t\t'+cadena_add.strip() + '\n')
					resultados.write('\t\t'+data.strip() + '\n')	
					resultados.write('\n')
					
				resultados.write('\n\n')
		sleep(1.5)
	bar.finish()
	
if __name__ == "__main__":
	if len(argv) != 2:
		print(banner)
		print(f'El modo de uso es el siguiente:')
		print(f'\t --> python3 hibp.py dominios.txt')
		exit(1)
	else:
		arch_dom = argv[1]
		try:
			with open(arch_dom, 'r') as archive:
				for dominio in archive:
					lista_dominios.append(dominio.strip())
		except FileNotFoundError:
			print(f"Archivo {arch_dom} no existe")
	
	print(banner)
	contador=1
	bar1 = Bar('Tratando dominios', max=len(lista_dominios))
	for i in range(len(lista_dominios)):
		bar1.next()
		url_breached_domains = f'{base_url}{lista_dominios[i]}'
		response = requests.get(url_breached_domains, headers=header_api_key)
		
		if response.status_code == 200:
			for usuario,datab in response.json().items():
				correo = f'{usuario}@{lista_dominios[i]}'
				correos_breached.append(correo.strip())
		else:
			not_breached_domain = f'{lista_dominios[i]}'
			with open("not_breached.txt","a") as nb:
				nb.write(not_breached_domain.strip() + '\n')
		sleep(1.5)
		contador+=1
	bar1.finish()
	print(f'\nSe encontraron {len(correos_breached)} correos\n')
	extraeDatosBrechas(correos_breached)
