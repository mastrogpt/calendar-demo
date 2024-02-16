# --web true
import json


def main(_):
    data = {
        "services": [

            {
                "name": "Calendar",
                "url": "openai/chat",
            }
        ]
    }
    return {"body": data}
