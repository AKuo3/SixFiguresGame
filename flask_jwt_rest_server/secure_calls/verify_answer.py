from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from db_con import get_db_instance, get_db
import random
global_db_con = get_db()

from tools.logging import logger

def handle_request():
    #todo: implement
    logger.debug("Get Easy Question Handle Request")
    cur = global_db_con.cursor()
    used_questions = request.args.get("used_questions")
    cur.execute(f"select count(*) from easy_questions;")
    numRows = cur.fetchall()
    random_question = random.randrange(1,numRows)
    checkedDupe = False

    while(checkedDupe == False):
     for x in used_questions:
      if(x == random_question):
       random_question = random.randrange(1,numRows)
       break
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

    return json_response(question_info = {'question_id': question_id,'question_text':question_text,'question_answerA': question_answerA,'question_answerB':question_answerB,'question_answerC':question_answerC,'question_answerD':question_answerD,'question_correctAnswer':question_correctAnswer})