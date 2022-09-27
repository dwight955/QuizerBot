import time
from generalVariable.variable import Variable
from game import quiz
# Funcion que cuenta los segundos en que el quiz o poll estaran abiertos
# Si is_request esta en True el Thread muere
async def run_period_open_answer()->None:
    print("Se acabo el tiempo")
    await quiz.quiz(Variable.currentContext["update"], Variable.currentContext["context"])