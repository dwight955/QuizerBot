
#1822798056
from controller.handler.handler_command import UserContext
from main import *
from generalVariable.variable import Variable

async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a predefined poll"""
    print("===2=========")
    print(str(update))
    Variable.answer_complete["chat_id"] = update.effective_chat.id
    questions = ["JavaScript","REACT","CSS","HTML"]
    message = await context.bot.send_poll(
        update.effective_chat.id,
        "Cuales son las tecnologia que se utilizan para comenzar a crear una pagina web?",
        questions,
        is_anonymous=False,
        allows_multiple_answers=True,
    )
    # global save_event_game
    UserContext.save_event_game = [update, context]
