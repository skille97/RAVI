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

def conveter(filename):
    with open(filename) as f:
        text = f.read()

    text = text.split("\n")
    text = list(map(str.split, text))
    text = list(map(listremove, text))
    text = list(map(listremovepro, text))
    x = 0
    while text[x][0] != "Component":
        x += 1

    text[x] = ["Component", "Comment", "Required", "Available", "Ratio of required", "Difference"]
    for i in text[x + 1:]:
        if not i:
            continue
        ind = text.index(i)
        i[-2] += "%"
        text[ind] = i
    text[:] = [y for y in text if y != []]


    remove = []
    for i in range(len(text)):
        if text[i][0] == "MYPlan":
            if text[i][2] == "Printed:":
                remove.append(i)
    o = 0
    for i in remove:
        del text[i - o]
        o += 1

    with open("output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(text)

if __name__ == "__main__":
    conveter("lang")