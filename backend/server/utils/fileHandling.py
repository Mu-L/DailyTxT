import json
import os
import logging

from fastapi import HTTPException
from .settings import settings

logger = logging.getLogger("dailytxtLogger")

def getUsers():
    try:
        f = open(os.path.join(settings.data_path, "users.json"), "r")
    except FileNotFoundError:
        logger.info("users.json - File not found")
        return {}
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error when trying to open users.json")
    else:
        with f:
            s = f.read()
            if s == "":
                return {}
            return json.loads(s)

def writeUsers(content):
    # print working directory
    try:
        f = open(os.path.join(settings.data_path, "users.json"), "w")
    except Exception as e:
        logger.exception(e)
        return e
    else:
        with f:
            f.write(json.dumps(content, indent=4))
            return True