from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token

from tools.logging import logger

def handle_request():
    logger.debug("Setup Handle Request")

    token_string = '89b15cd3a509488789b15cd3a5094887'

    return json_response(token = create_token(token_string))

