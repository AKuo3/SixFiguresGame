from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from db_con import get_db_instance, get_db
import random
global_db_con = get_db()

from tools.logging import logger

def handle_request():
    logger.debug("Get Easy Question Handle Request")
    cur = global_db_con.cursor()
    used_questions = request.form.getlist('used_easy_questions')
    numRows = 16
    random_question = -1
    checkedDupe = False

    while(checkedDupe == False):
     random_question = random.randrange(1,numRows)
     for x in used_questions[0]:
      if(x == random_question): break
     else:
      checkedDupe = True

    cur.execute(f"select * from easy_questions where id = '{random_question}';")
    question = cur.fetchone()
    question_id = question[0]
    question_text = question[1]
    question_answerA = question[2]
    question_answerB = question[3]
    question_answerC = question[4]
    question_answerD = question[5]
    question_correctAnswer = question[6]
    print("Successfully got easy question.")

    return json_response(token = create_token(g.jwt_data), question_info = {'question_id': question_id,'question_text':question_text,'question_answerA': question_answerA,'question_answerB':question_answerB,'question_answerC':question_answerC,'question_answerD':question_answerD})