from main import *
import json


async def credits(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id_user = update.message.chat.id
    # Variable que se encarga de almacenar todos los datos del usuario
    data_credits = open("game/credits_json.json", 'rt')  # Cargar el archivo en modo texto
    data_read = data_credits.read()  # Leer el archivo
    load_json = json.loads(data_read)  # Cargar el archivo a Json

    union_credits = ""  # Variable para obtener los aportadores del proyecto
    for credits in load_json:  # Cargar los créditos
        network = ''  # Variable para almacenar las redes sociales de cada develop
        for key, value in credits['network'].items():  # Obteniendo las redes sociales llave valor
            # Creando la estructura de las redes con enlace
            network += f"       *{str(key).capitalize()}:* [{str(key).capitalize()}]({value})\n"

        # Estructura de los creditos de cada develop
        union_credits += f"\n\**{credits['name']}*\n" \
                         f"{network}"

    # Mensaje a enviar al cliente sobre la información solicitada
    msg_credits = (
            f"Créditos".center(50, '-') +
            f"\n"
            f"{union_credits}"
    )

    await context.bot.send_message(chat_id=id_user, text=msg_credits, parse_mode="Markdown")
