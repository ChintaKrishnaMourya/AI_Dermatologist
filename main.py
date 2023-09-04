from textbase import bot, Message
from typing import List
from dermobuddy import *

@bot()
def on_message(message_history: List[Message], state: dict = None):
    print(message_history[-1]["content"][0]['value'])
    bot_response = derm_agent({"input" :message_history[-1]["content"][0]['value']})["output"]

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }