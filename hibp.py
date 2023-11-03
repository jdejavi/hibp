#!/usr/bin/env python3

from sys import *
from time import *
import requests


'''
Script que te dice que usuarios de un dominio en concreto se han visto comprometidos en alguna brecha de seguridad
	--> Ralizado por Javier Matilla Martín aka m4t1
'''

#Variables globales
lista_dominios = []
header_api_key = {
	"hibp-api-key": "API_KEY"
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
	for domain in lista_dominios:
		url_breached_domains = f'{base_url}{domain}'
		response = requests.get(url_breached_domains, headers=header_api_key)
		
		if response.status_code == 200:
			with open("resultados_hibp.txt","a") as resultado:
			
				for usuario,datab in response.json().items():
				
					correo = f'{usuario}@{domain}'
					breaches = ''
					correos_breached.append(correo.strip())
					
					for d in datab:
						breaches += f'{d},'
						
					if breaches.endswith(','):
						breaches = breaches[:-1]
						
					cadena_completa = f'{correo:<35} --> {breaches}'
					resultado.write(cadena_completa.strip()+'\n')
		else:
			print(f'El dominio {dominio} no tiene correos en brechas de datos, el codigo de estado es {response.status_code}')
