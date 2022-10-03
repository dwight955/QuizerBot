from main import *
from game.database.dbReward import save_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id_user = update.message.chat.id
    if __name__ == "__main__":
        file_read_data = open("userData.txt", "rt")
    else:
        file_read_data = open("game/database/userData.txt", "rt")

    info_data = file_read_data.read()

    if str(id_user) not in info_data:
        await save_user(id_user)

    await context.bot.send_message(chat_id=id_user, text="Welcome to the Bot - con nuevo token")