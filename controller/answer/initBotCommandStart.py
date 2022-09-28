from main import *
from game.database.dbReward import save_user
from generalVariable.variable import Variable
from game.database.dbData import get_user_data

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id_user = update.message.chat.id
    if __name__ == "__main__":
        file_read_data = open("userData.txt", "rt")
    else:
        file_read_data = open("game/database/userData.txt", "rt")

    info_data = file_read_data.read()

    if str(id_user) not in info_data:
        await save_user(id_user)
        Variable.gameData["poll"] = get_user_data(id_user)["polls_answered"]
        Variable.gameData["quiz"] = get_user_data(id_user)["quizs_answered"]



    await context.bot.send_message(chat_id=id_user, text="Welcome to the Bot - con nuevo token")