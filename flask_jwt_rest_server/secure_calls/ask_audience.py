from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token
from db_con import get_db_instance, get_db
import random
global_db_con = get_db()

from tools.logging import logger

def handle_request():
    logger.debug("Ask Audience Handle Request")
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
            if(correct_answer == "a"):
                given_answer = "92% voted for a. 1% voted for b. 4% voted for c. 3% voted for d."
            elif(correct_answer == "b"):
                given_answer = "2% voted for a. 89% voted for b. 6% voted for c. 3% voted for d."
            elif(correct_answer == "c"):
                given_answer = "4% voted for a. 0% voted for b. 96% voted for c. 0% voted for d."
            elif(correct_answer == "d"):
                given_answer = "2% voted for a. 1% voted for b. 13% voted for c. 93% voted for d."
        else:
            given_answer = "20% voted for a. 39% voted for b. 13% voted for c. 28% voted for d."
    elif current_question_difficulty == "medium": #70% chance of guaranteed success
        rng = random.randrange(1,101)
        if(rng <= 70):
            if(correct_answer == "a"):
                given_answer = "76% voted for a. 11% voted for b. 6% voted for c. 7% voted for d."
            elif(correct_answer == "b"):
                given_answer = "6% voted for a. 81% voted for b. 9% voted for c. 4% voted for d."
            elif(correct_answer == "c"):
                given_answer = "0% voted for a. 10% voted for b. 79% voted for c. 11% voted for d."
            elif(correct_answer == "d"):
                given_answer = "4% voted for a. 0% voted for b. 13% voted for c. 83% voted for d."
        else:
            given_answer = "39% voted for a. 20% voted for b. 13% voted for c. 28% voted for d."
    elif current_question_difficulty == "hard": #30% chance of guaranteed success
        rng = random.randrange(1,101)
        if(rng <= 30):
            if(correct_answer == "a"):
                given_answer = "40% voted for a. 24% voted for b. 16% voted for c. 20% voted for d."
            elif(correct_answer == "b"):
                given_answer = "42% voted for a. 51% voted for b. 7% voted for c. 0% voted for d."
            elif(correct_answer == "c"):
                given_answer = "25% voted for a. 27% voted for b. 39% voted for c. 9% voted for d."
            elif(correct_answer == "d"):
                given_answer = "20% voted for a. 24% voted for b. 13% voted for c. 43% voted for d."
        else:
            given_answer = "12% voted for a. 1% voted for b. 40% voted for c. 48% voted for d."
    elif current_question_difficulty == "pinnacle": #5% chance of guaranteed success
        rng = random.randrange(1,101)
        if(rng <= 5):
            if(correct_answer == "a"):
                given_answer = "30% voted for a. 26% voted for b. 16% voted for c. 28% voted for d."
            elif(correct_answer == "b"):
                given_answer = "12% voted for a. 34% voted for b. 30% voted for c. 24% voted for d."
            elif(correct_answer == "c"):
                given_answer = "3% voted for a. 10% voted for b. 47% voted for c. 40% voted for d."
            elif(correct_answer == "d"):
                given_answer = "28% voted for a. 23% voted for b. 7% voted for c. 32% voted for d."
        else:
            given_answer = "28% voted for a. 32% voted for b. 25% voted for c. 15% voted for d."


    return json_response(audience_answer = given_answer)