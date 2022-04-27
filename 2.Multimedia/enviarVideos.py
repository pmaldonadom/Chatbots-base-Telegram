
from telegram import Update,ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler

def start(update: Update, context: CallbackContext):
    # Envía un mensaje cuando se emite el comando /start
    update.message.reply_text('Enviar audio: \n  - /video')

def video(update: Update, context: CallbackContext):
     # Enviar video desde ubicacion local
     update.message.reply_video(open("video.mp4", "rb"), 
                                caption="Video de paisaje nevado")


def main():

    # Creacion del updater pasandole el token del bot
    updater = Updater(token='introducir-token-aqui')

    # Se obtiene el despachador (dispatcher) para registrar los negociadores (handlers)
    dp = updater.dispatcher
    
    #Se añade el negociador CommandHlander al distpatcher con el comando start
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('video', video))


    # Pregunta constantemente a nuestro bot si hay nuevos mensajes
    updater.start_polling()

    # Permite finalizar el bot con ctrl + C
    updater.idle()

if __name__ == '__main__':

    main()



