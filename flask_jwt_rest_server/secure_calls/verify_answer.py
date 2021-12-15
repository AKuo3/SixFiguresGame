from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from db_con import get_db_instance, get_db
import random
global_db_con = get_db()

from tools.logging import logger

def handle_request():
    logger.debug("Verify Answer Handle Request")
    cur = global_db_con.cursor()
    question_id = request.args.get("current_question_id")
    print(request.args.get("current_question_id"))
    print(question_id)
    user_answer = request.args.get("user_answer")
    print(request.args.get("user_answer"))
    print(user_answer)
    current_question_difficulty = request.args.get("current_question_difficulty")
    error = False
    user_right = None

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
        correct_answer = server_question[6]
        if correct_answer == user_answer:
            user_right = True
        else:
            user_right = False
        print("Successfully checked question.")


    return json_response(user_correct = user_right,right_answer = correct_answer)