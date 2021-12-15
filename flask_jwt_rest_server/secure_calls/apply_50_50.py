from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from db_con import get_db_instance, get_db
import random
global_db_con = get_db()

from tools.logging import logger

def handle_request():
    logger.debug("50/50 Handle Request")
    cur = global_db_con.cursor()
    question_id = request.args.get("current_question_id")
    current_question_difficulty = request.args.get("current_question_difficulty")
    disabled_answer_1 = None
    disabled_answer_2 = None
    indexed_answer = None
    error = False

    if current_question_difficulty == "easy":
        cur.execute(f"select * from easy_questions where id = '{question_id}';")
    elif current_question_difficulty == "medium":
        cur.execute(f"select * from medium_questions where id = '{question_id}';")
    elif current_question_difficulty == "hard":
        cur.execute(f"select * from hard_questions where id = '{question_id}';")
    elif current_question_difficulty == "pinnacle":
        cur.execute(f"select * from pinnacle_questions where id = '{question_id}';")
    else:
        error = True

    if error == True:
        print("Something bad happened!!")
    else:
        server_question = cur.fetchone()
        correct_answer = server_question[6] #1 = a, 2 = b, 3 = c, 4 = d
        if correct_answer == "a":
            indexed_answer = 1
        elif correct_answer == "b":
            indexed_answer = 2
        elif correct_answer == "c":
            indexed_answer = 3
        elif correct_answer == "d":
            indexed_answer = 4

        disabled_answer_1 = random.randrange(1,5)
        while disabled_answer_1 == indexed_answer:
            disabled_answer_1 = random.randrange(1,5)

        disabled_answer_2 = random.randrange(1,5)
        while disabled_answer_2 == indexed_answer or disabled_answer_2 == disabled_answer_1:
            disabled_answer_2 = random.randrange(1,5)


    return json_response(disabled_option_1 = disabled_answer_1,disabled_option_2 = disabled_answer_2)