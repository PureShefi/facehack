import wikipedia

def get_wiki(name):
    try:
        return {"success": True, "data":wikipedia.summary(params["name"])}
    except wikipedia.exceptions.PageError:
        return {"success": False}

    