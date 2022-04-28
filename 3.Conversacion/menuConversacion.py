
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler,CallbackQueryHandler,ConversationHandler

MENU_PRINCIPAL, ENLACE, AUDIO, IMAGEN, VIDEO, DOCUMENTO = range (6)

teclado_menu_principal = [
				[InlineKeyboardButton(text='🔗 enlace ', callback_data=str(ENLACE)),
				InlineKeyboardButton(text='🔊 audio ', callback_data=str(AUDIO)),
                InlineKeyboardButton(text=' 🖼  imagen ', callback_data=str(IMAGEN))],
				[InlineKeyboardButton(text='🎥 video ', callback_data=str(VIDEO)),
				InlineKeyboardButton(text='📓 documento ', callback_data=str(DOCUMENTO))],
			  ]


def start(update: Update, context: CallbackContext):
    reply_markup  = InlineKeyboardMarkup(teclado_menu_principal)
    update.message.reply_text(
		text="Bievenido, selecione un botón",
		parse_mode= ParseMode.HTML,
		reply_markup=reply_markup
	)

    return MENU_PRINCIPAL

def enlace(update: Update, context: CallbackContext):
    query = update.callback_query
     #Para enviar un enlace necesitamos el argumento parse_mode
    context.bot.send_message(text="<a href='www.google.es'>Enlace a Google</a>", 
                                chat_id = query.message.chat_id,
                                parse_mode = ParseMode.HTML) 

def audio(update: Update, context: CallbackContext):
    query = update.callback_query
    #Se envia un audio ique obtiene desde una url
    context.bot.send_audio( audio="https://www.elongsound.com/images/mp3/trueno04.mp3", 
                                title="Sonido truenos",
                                chat_id = query.message.chat_id,
                                caption="Truenos")

    context.bot.send_audio(audio=open("../static/la-atmosfera_4.mp3", "rb"), 
                                title="Sonido de pajaros",
                                chat_id = query.message.chat_id,
                                caption="Pajaros")
                                
def imagen(update: Update, context: CallbackContext):
    query = update.callback_query
    #Se envia una imagen desde una ubicacion con lectura en  modo binario (rb)
    context.bot.send_photo(photo=open("../static/imagenBot.png", "rb"), 
                                chat_id = query.message.chat_id,
                                caption="Imagen bot telegram")

def video(update: Update, context: CallbackContext):
     query = update.callback_query
     # Enviar video desde ubicacion local
     context.bot.send_video(video=open("../static/video.mp4", "rb"), 
                                chat_id = query.message.chat_id,
                                caption="Video de paisaje nevado")

def documento(update: Update, context: CallbackContext):
    query = update.callback_query
    context.bot.send_document(document =open("../static/trazabilidad.pdf", "rb"), 
                                chat_id = query.message.chat_id,
                                caption="PDF sobre la trazabilidad")
                                


def main():

    # Creacion del updater pasandole el token del bot
    updater = Updater(token='introducir-token-aqui')

    # Se obtiene el despachador (dispatcher) para registrar los negociadores (handlers)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
		entry_points=[CommandHandler('start', start)],
		states={
                MENU_PRINCIPAL: [CallbackQueryHandler(documento, pattern=str(DOCUMENTO)),
                                CallbackQueryHandler(audio, pattern=str(AUDIO)),
                                CallbackQueryHandler(imagen, pattern=str(IMAGEN)),
                                CallbackQueryHandler(video, pattern=str(VIDEO)),
                                CallbackQueryHandler(enlace, pattern=str(ENLACE))],

	    },
	    fallbacks=[CommandHandler('start', start)]
	
	)


	# Add ConversationHandler to dispatcher that will be used for handling
	# updates
    dp.add_handler(conv_handler)


    # Pregunta constantemente a nuestro bot si hay nuevos mensajes
    updater.start_polling()

    # Permite finalizar el bot con ctrl + C
    updater.idle()

if __name__ == '__main__':

    main()



