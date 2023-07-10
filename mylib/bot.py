import wikipedia

def scrape(name='Microsoft', sentences=1):
    r = wikipedia.summary(name, sentences=sentences)
    return r



