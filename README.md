# Chatbots-base-Telegram
## Tabla de contenidos :

- [Chatbots-base-Telegram](#chatbots-base-telegram)
  - [Tabla de contenidos :](#tabla-de-contenidos-)
  - [Descripcion y contenido:](#descripcion-y-contenido)
    - [Descripción :](#descripción-)
    - [Contenido :](#contenido-)
  - [Requerimientos:](#requerimientos)
  - [Manual de ejecución:](#manual-de-ejecución)


## Descripcion y contenido:

### Descripción :

Ejemplos básicos sobre bots de telegram realizados con la libreria - python-telegram-bot
 

### Contenido :

- **[1.PrimerBot\primerBot.py](./1.PrimerBot/primerBot.py)**: Bot básico hola mundo.
- **[2.Multimedia](./2.Multimedia)**: Directorio que contiene ejemplos de bots para enviar diferentes archivos.
- **[3.Conversacion](./3.Conversacion)**: Conversacion interactuando a traves de teclado


## Requerimientos:
- Instalar telegram
- Generar el Token de nuestro Bot con @Botfather

 - Lenguaje python 3.7
 - Libreria python-telegram-bot
 - Opcional pero recomendable crear entorno virtual con python 3.7 e instalar la libreria.

  **Instalación con entorno virtual Anaconda**

  1. Descargar Anaconda
		https://www.anaconda.com/products/distribution

  1. Crear entorno virtual 
   
		 conda create --bot python=3.7

  3. Activar entorno de anaconda
  
		 conda activate bot

  4. Instalar la libreria python-telegram-bot 

		 pip install  python-telegram-bot

   **Crear bot con bothfather**
    Mediante botfather se crea el bot y se genera el token.

1. Buscamos botfather en telegram
2. Iniciamos la conversación /start.
    A continuación, se nos mostrará un listado con todos los comandos disponibles para interactuar con BotFather.
3. Para crear un nuevo bot es ejecutaremos el comando /newbot, le daremos un un nombre y un nombre de usuario que obligatoriamente tiene que acabar con la palabra bot. 
4. Automáticamente Telegram nos dará un token de seguridad único. Este código es necesario para que pueda usar la API Bot de la app de mensajería.

## Manual de ejecución:


1. Actualizar el token 

   		token = 'introducir-token-aqui'

2. Ejecutar el bot

   		python nombre_archivo.py
   	 
