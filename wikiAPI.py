import wikipedia

def get_wiki(params):
    try:
        return {"success": True, "data":wikipedia.summary(params["name"]), "url": wikipedia.page(params["name"]).url}
    except:
        return {"success": False, "data": "", "url": ""}

    