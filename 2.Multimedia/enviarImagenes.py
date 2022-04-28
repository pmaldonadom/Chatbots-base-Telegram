
from telegram import Update,ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler

def start(update: Update, context: CallbackContext):
    # Envía un mensaje cuando se emite el comando /start
    update.message.reply_text('Enviar imagenes: \n  - /imagen \n - /imagen2')

def imagen(update: Update, context: CallbackContext):
    # Se envia una imagen que obtiene desde una url
    update.message.reply_photo("https://d500.epimg.net/cincodias/imagenes/2021/09/30/lifestyle/1633021452_008267_1633022893_noticia_normal.jpg", 
                                caption="Imagen del logo de telegram")

def imagen2(update: Update, context: CallbackContext):
    # Se envia una imagen desde una ubicacion con lectura en modo binario (rb)
     update.message.reply_photo(open("../static/imagenBot.png", "rb"), 
                                reply_to_message_id= update.message.message_id,
                                caption="Imagen bot telegram")

def main():

    # Creacion del updater pasandole el token del bot
    updater = Updater(token='introducir-token-aqui')

    # Se obtiene el despachador (dispatcher) para registrar los negociadores (handlers)
    dp = updater.dispatcher
    
    #Se añade el negociador CommandHlander al dispatcher con el comando start
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('imagen', imagen))
    dp.add_handler(CommandHandler('imagen2', imagen2))

    # Pregunta constantemente a nuestro bot si hay nuevos mensajes
    updater.start_polling()

    # Permite finalizar el bot con ctrl + C
    updater.idle()

if __name__ == '__main__':

    main()



