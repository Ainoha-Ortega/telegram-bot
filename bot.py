from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
import os
from datetime import datetime, timedelta

# Token del Bot (Método 1: directo)
TOKEN = '7822441535:AAEU0WjQYyQ8Gz_1-FIM1vNvVRwVfspNoyU'

# Diccionario de usuarios con nombres y apellidos
usuarios = {
    123456789: {"nombre": "Ainoha Ortega"},
    987654321: {"nombre": "Daniel Ortega"},
    567890123: {"nombre": "Nuria Ortega"},
    234567890: {"nombre": "Ana Paula Montes"},
    345678901: {"nombre": "Manuel Ibáñez"},
    456789012: {"nombre": "Rafael Gutiérrez"},
    567890234: {"nombre": "María Dolores"}
}

# Diccionario para guardar la fecha del último mensaje de cada usuario
ultima_actividad = {}

# Mensajes automáticos
def saludo_nuevo_usuario():
    return '''¡Hola! 👋

Este es nuestro teléfono de oficina técnica, cuyo equipo son los siguientes especialistas:
- *Ainoha Ortega*: ainoha@grupoespejo.net
- *Daniel Ortega*: daniel@grupoespejo.net
- *Nuria Ortega*: nuria@grupoespejo.net
- *Ana Paula Montes*: anapaula@grupoespejo.net
- *Manuel Ibáñez*: manuel@grupoespejo.net
- *Rafael Gutiérrez*: rafa@grupoespejo.net
- *María Dolores*: mariadolores@grupoespejo.net

¡Que tengas un excelente día! 😊'''

def mensaje_ausencia():
    return '''¡Hola! 👋  

Gracias por escribirnos a P. Espejo. Actualmente, estamos fuera de nuestro horario laboral, pero hemos recibido tu mensaje y lo atenderemos en cuanto volvamos a estar disponibles.

Nuestro horario de atención es:
- *Lunes a jueves*: 9:00h a 13:00h y 15:30h a 18:30h.
- *Viernes*: 8:00h a 14:00h.

Te responderemos a la brevedad posible dentro de estos horarios. ¡Gracias por tu comprensión! Que tengas un excelente día. 😊'''

def saludo_cliente(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    nombre_usuario = usuarios.get(user_id, {}).get("nombre", "Cliente")
    
    # Si el usuario es nuevo o ha pasado más de 14 días desde la última actividad, enviamos un saludo
    if user_id not in ultima_actividad or datetime.now() - ultima_actividad[user_id] > timedelta(days=14):
        ultima_actividad[user_id] = datetime.now()  # Actualizamos la última actividad
        mensaje = f'''¡Hola! 👋

Gracias por contactarnos. Nos pondremos en contacto contigo lo antes posible.
- *{nombre_usuario}*: {usuarios[user_id]["email"]}

¡Que tengas un excelente día! 😊'''
        update.message.reply_text(mensaje)

def fuera_de_horario(update: Update, context: CallbackContext):
    # Verificamos si el mensaje fue enviado fuera del horario
    hora_actual = datetime.now().hour
    if hora_actual < 9 or hora_actual >= 18:
        mensaje = mensaje_ausencia()
        update.message.reply_text(mensaje)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("¡Hola! 👋 Soy el bot de P. Espejo. Si es tu primera vez escribiendo, recibirás un mensaje de bienvenida.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = upda
