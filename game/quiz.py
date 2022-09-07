
from controller.handler.handler_command import UserContext
from main import *
from generalVariable.variable import Variable

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a predefined poll"""
    Variable.answer_complete["chat_id"] = update.effective_chat.id
    questions = ["24 DE ENERO DE 1844", "04 DE ENERO DE 1834", "27 DE MAYO DEL 1846", "27 DE FEBRERO DE 1844"]
    message = await update.effective_message.reply_poll(
        "¿Cuando se logró la independencia de Republica Dominicana?",
        questions, 
        type=Poll.QUIZ, 
        correct_option_id=3,
        explanation= "27 DE FEBRERO DE 1844"
    )
    # global save_event_game
    UserContext.save_event_game = [update, context]
    print("===1=========")
    print(str(UserContext.save_event_game))
