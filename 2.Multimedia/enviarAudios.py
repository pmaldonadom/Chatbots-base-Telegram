
from telegram import Update,ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler

def start(update: Update, context: CallbackContext):
    # Envía un mensaje cuando se emite el comando /start
    update.message.reply_text('Enviar audio: \n  - /audio \n - /audio2')

def audio(update: Update, context: CallbackContext):
    #Se envia una imagen ique obtiene desde una url
    update.message.reply_audio("https://www.elongsound.com/images/mp3/trueno04.mp3", 
                                title="Sonido truenos",
                                caption="Truenos")

def audio2(update: Update, context: CallbackContext):

    #Enviar sonido desde ubicacion local en modo de lectura binaria (rb)
    update.message.reply_audio(open("../static/la-atmosfera_4.mp3", "rb"), 
                                reply_to_message_id= update.message.message_id,
                                title="Pajaros",
                                caption="Sonido de pajaros")


def main():

    # Creacion del updater pasandole el token del bot
    updater = Updater(token='introducir-token-aqui')

    # Se obtiene el despachador (dispatcher) para registrar los negociadores (handlers)
    dp = updater.dispatcher
    
    #Se añade el negociador CommandHlander al distpatcher con el comando start
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('audio', audio))
    dp.add_handler(CommandHandler('audio2', audio2))

    # Pregunta constantemente a nuestro bot si hay nuevos mensajes
    updater.start_polling()

    # Permite finalizar el bot con ctrl + C
    updater.idle()

if __name__ == '__main__':

    main()



