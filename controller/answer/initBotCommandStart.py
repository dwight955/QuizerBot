from main import *
from game.database.dbReward import save_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Se obtiene el Id del usuario
    id_user = update.message.chat.id
    # Se obtiene el firts_name del usuario
    name = update.message.chat.first_name
    # formato del mensaje de Inicio
    msg_welcome = (
        f"Bienvenido *{name}* al juego QuizerBot v.0.1\n\n ¿Listo para responder peguntas?\n\n"
        "¡Descuida! no son muy complicadas pero tampoco muy faciles \u1F60F\n\n"
        "*Modos de juegos*\n> /quiz : Solo preguntas con una sola respuesta\n> /poll : Solo preguntas"
        " con varias respuestas\n> /mixto : Te enviara de manera aleatoria un Quiz o Poll\n*Mas opciones*\n> /creditos : "
        "Conoce un poco mas a los desarrolladores"
    )

    if __name__ == "__main__":
        file_read_data = open("userData.txt", "rt")
    else:
        file_read_data = open("game/database/userData.txt", "rt")

    info_data = file_read_data.read()

    if str(id_user) not in info_data:
        await save_user(id_user)

    await context.bot.send_message(chat_id=id_user, text= msg_welcome, parse_mode="Markdown")