
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler,CallbackQueryHandler,ConversationHandler,MessageHandler,Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)


MENU_PRINCIPAL, ENLACE, AUDIO, IMAGEN, VIDEO, DOCUMENTO, OBTENER_NOMBRE, VOLVER_MENU = range (8)



teclado_menu_principal = [
				[InlineKeyboardButton(text='🔗 enlace ', callback_data=str(ENLACE)),
				InlineKeyboardButton(text='🔊 audio ', callback_data=str(AUDIO)),
                InlineKeyboardButton(text=' 🖼  imagen ', callback_data=str(IMAGEN))],
				[InlineKeyboardButton(text='🎥 video ', callback_data=str(VIDEO)),
				InlineKeyboardButton(text='📓 documento ', callback_data=str(DOCUMENTO))],
			  ]


teclado_volver_menu = [[InlineKeyboardButton(text='🔙 Volver', callback_data=str(VOLVER_MENU))]]


def start(update: Update, context: CallbackContext):
    datos_user = update.message.from_user
    nombre_usuario =  update.message.from_user.first_name
    id_usuario =  update.message.from_user.id
    alias =  update.message.from_user.username
    context.user_data['alias']= alias
    logger.info("El usuario %s ha iniciado el bot", alias)
    reply_markup  = InlineKeyboardMarkup(teclado_menu_principal)
    update.message.reply_text(
		text="Hola " + nombre_usuario + " " + alias,
		parse_mode= ParseMode.HTML,
        reply_markup=reply_markup
	)

    return MENU_PRINCIPAL

def volver_menu_principal(update: Update, context: CallbackContext):
    logger.info("El usuario %s ha vuelto al menu principal", context.user_data['alias'])
    query = update.callback_query
    reply_markup  = InlineKeyboardMarkup(teclado_menu_principal)
    context.bot.send_message(
		text="Elija una opcion del menú",
	    chat_id = query.message.chat_id,
		reply_markup=reply_markup
	)

    return MENU_PRINCIPAL

def enlace(update: Update, context: CallbackContext):
    logger.info("El usuario %s ha pulsado el boton de enlace", context.user_data['alias'])
    query = update.callback_query
    reply_markup  = InlineKeyboardMarkup(teclado_volver_menu)
     #Para enviar un enlace necesitamos el argumento parse_mode
    context.bot.send_message(text="<a href='www.google.es'>Enlace a Google</a>", 
                                chat_id = query.message.chat_id,
                                parse_mode = ParseMode.HTML,
                                reply_markup=reply_markup
                               )

def audio(update: Update, context: CallbackContext):
    logger.info("El usuario %s ha pulsado el boton de audio", context.user_data['alias'])
    query = update.callback_query
    reply_markup  = InlineKeyboardMarkup(teclado_volver_menu)
    #Se envia una imagen ique obtiene desde una url
    context.bot.send_audio(audio="https://www.elongsound.com/images/mp3/trueno04.mp3", 
                                chat_id = query.message.chat_id,
                                caption="Truenos",
                                reply_markup=reply_markup
                               )

def imagen(update: Update, context: CallbackContext):
    logger.info("El usuario %s ha pulsado el boton de imagen", context.user_data['alias'])
    query = update.callback_query
    reply_markup  = InlineKeyboardMarkup(teclado_volver_menu)
    #Se envia una imagen desde una ubicacion con lectura en  modo binario (rb)
    context.bot.send_photo(photo=open("../static/imagenBot.png", "rb"), 
                                chat_id = query.message.chat_id,
                                caption="Imagen bot telegram",
                                reply_markup=reply_markup
                               )

def video(update: Update, context: CallbackContext):
     logger.info("El usuario %s ha pulsado el boton de video", context.user_data['alias'])
     query = update.callback_query
     reply_markup  = InlineKeyboardMarkup(teclado_volver_menu)
     # Enviar video desde ubicacion local
     context.bot.send_video(video=open("../static/video.mp4", "rb"), 
                                chat_id = query.message.chat_id,
                                caption="Video de paisaje nevado",
                                reply_markup=reply_markup
                               )

def documento(update: Update, context: CallbackContext):
    logger.info("El usuario %s ha pulsado el boton de video", context.user_data['alias'])
    query = update.callback_query
    reply_markup  = InlineKeyboardMarkup(teclado_volver_menu)
    # Enviar documento desde ubicacion local
    context.bot.send_document(document =open("../static/trazabilidad.pdf", "rb"), 
                                chat_id = query.message.chat_id,
                                caption="PDF sobre la trazabilidad",
                                reply_markup=reply_markup
                               )
    return MENU_PRINCIPAL
								 

def error(update, context):
    # Muestra en el log el error obtenido tras una actualización del bot
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():

    # Creacion del updater pasandole el token del bot
    updater = Updater(token='introducir-token-aqui')

    # Se obtiene el despachador (dispatcher) para registrar los manejadores (handlers)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
		entry_points=[CommandHandler('start', start)],
		states={
                MENU_PRINCIPAL: [CallbackQueryHandler(documento, pattern=str(DOCUMENTO)),
                                CallbackQueryHandler(audio, pattern=str(AUDIO)),
                                CallbackQueryHandler(imagen, pattern=str(IMAGEN)),
                                CallbackQueryHandler(video, pattern=str(VIDEO)),
                                CallbackQueryHandler(enlace, pattern=str(ENLACE)),
                                CallbackQueryHandler(volver_menu_principal, pattern=str(VOLVER_MENU))
                                ],
	    },
	    fallbacks=[CommandHandler('start', start)]
	
	)
    


	# Add ConversationHandler to dispatcher that will be used for handling
	# updates
    dp.add_handler(conv_handler)

    # Gestiona y muestra todos los errores
    # dp.add_error_handler(error)

    # Pregunta constantemente a nuestro bot si hay nuevos mensajes
    updater.start_polling()

    # Permite finalizar el bot con ctrl + C
    updater.idle()

if __name__ == '__main__':

    main()



