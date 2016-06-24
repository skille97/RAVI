import csv

def listremove(l):
    if l is None:
        return [""]
    try:
        l.remove(">")
        return l
    except ValueError:
        return l

def listremovepro(l):
    if l is None:
        return [""]
    try:
        l.remove("%")
        return l
    except ValueError:
        return l


with open("Komponent oversigt 230616") as f:
    text = f.read()

text = text.split("\n")
text = list(map(str.split, text))
text = list(map(listremove, text))
text = list(map(listremovepro, text))

x = 0
while text[x][0] != "Component":
    x += 1

for i in text[x + 1:]:
    if not i:
        continue
    ind = text.index(i)
    i[-2] += "%"
    text[ind] = i

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(text)


