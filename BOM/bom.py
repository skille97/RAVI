import pprint

def listremove(l):
    try:
        return l.remove(">")
    except ValueError:
        return l

with open("Komponent oversigt 230616") as f:
    text = f.read()

text = text.split("\n")
text = list(map(str.split, text))
text = list(map(listremove, text))
print(text)

