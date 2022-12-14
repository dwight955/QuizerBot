class UserContext:
    save_event_game = [0, 0]

from main import *


from controller.answer.initBotCommandStart import start
from controller.answer.anyMessage import echo
from generalVariable.constant import CONSTANT

application = ApplicationBuilder().token(CONSTANT.MY_TOKEN_BOT).build()

from controller.answer.answer_poll import *
from controller.answer.answer_quiz import *
from controller.answer.answer_inline_keyboard import *

from game.poll import poll
from game.quiz import quiz
from game.credits import credits
# from game.quiz import button

application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('poll', poll))
application.add_handler(CommandHandler('quiz', quiz))
application.add_handler(CommandHandler('creditos', credits))
# application.add_handler(CallbackQueryHandler(button))
application.add_handler(PollHandler(receive_quiz_answer))

application.add_handler(PollAnswerHandler(receive_poll_answer))

application.add_handler(CallbackQueryHandler(receive_inline_keyboard))

echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

application.add_handler(echo_handler)

application.run_polling()

