# HIBP searcher

Esta es una herramienta simple escrita en Python para buscar en las brechas de datos de la web Have I Been Pwned y ver si algún correo de un dominio está comprometido

Se debe de tener una cuenta de Have I Been Pwned con licencia y tener registrado en ella un dominio sobre el que tengas propiedad para su uso

**Recuerda que debes cambiar el valor de la variable API_KEY por tu api key de Have I Been Pwned**

## Autor

**Nombre del Autor:** Javier Matilla Martín aka m4t1

## Uso

Asegúrate de tener Python 3 instalado en tu sistema antes de utilizar esta herramienta.

1. Clona el repositorio o descarga el archivo `hibp.py` directamente en tu sistema.

2. Ejecuta el script `hibp.py` en la línea de comandos, especificando el archivo de entrada que contiene los IoCs que deseas convertir:

   ```bash
   python3 hibp.py <archivo_con_dominios.txt>
   ```
Por ejemplo:
   ```bash
   python3 hibp.py dominios.txt
   ```
Esto generará un archivo de texto llamado resultados_hibp.txt que contiene los correos encontrados junto con las brechas en los que fue descubierto.

## Formato de Entrada
El archivo de entrada debe seguir un formato específico con cada dominio en una línea separada.
