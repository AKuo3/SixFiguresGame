from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from db_con import get_db_instance, get_db
import random
global_db_con = get_db()

from tools.logging import logger

def handle_request():
    logger.debug("Phone Friend Handle Request")
    cur = global_db_con.cursor()
    question_id = request.args.get("current_question_id")
    current_question_difficulty = request.args.get("current_question_difficulty")
    indexed_answer = None
    given_answer = None
    rng = None
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
        correct_answer = server_question[6] #a, b, c, d

    if current_question_difficulty == "easy": #90% chance of guaranteed success
        rng = random.randrange(1,101)
        if(rng <= 90):
            given_answer = "This is easy. The answer is " + correct_answer + ". Good luck!"
        else:
            given_answer = "Sheesh, I don't know. Maybe it's d. Sorry!"
    elif current_question_difficulty == "medium": #70% chance of guaranteed success
        rng = random.randrange(1,101)
        if(rng <= 70):
            given_answer = "Hmm, I think I learned this in school. I'm pretty sure it's " + correct_answer + "."
        else:
            given_answer = "I'm really not sure... I'll guess a?"
    elif current_question_difficulty == "hard": #30% chance of guaranteed success
        rng = random.randrange(1,101)
        if(rng <= 30):
            given_answer = "Hey, I was just looking that up! It should be " + correct_answer + "."
        else:
            given_answer = "I think my friend's brother's cousin once mentioned that it's c. I think."
    elif current_question_difficulty == "pinnacle": #5% chance of guaranteed success
        rng = random.randrange(1,101)
        if(rng <= 5):
            given_answer = "Umm... Hmm... I think I've seen this question before. Maybe it's " + correct_answer + "...?"
        else:
            given_answer = "I want to say it's a, but you should really go with your gut. Hope you win it all!"


    return json_response(friend_answer = given_answer)