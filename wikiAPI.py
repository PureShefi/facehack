import wikipedia

def get_summary(name):
    try:
        return wikipedia.summary(name)
    except wikipedia.exceptions.PageError:
        return ""
    