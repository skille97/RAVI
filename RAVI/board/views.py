from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


from board.models import *
from django.conf import settings

import json




def index(request, hidden=False):

    items = Item.objects.filter(komplet= hidden).order_by("id")

    body = []
    colours = []
    link = "/"
    if not hidden:
        link = link + "hidden"


    for item in items:
        itemBody = []
        itemColours = []
        for name in ORDER:
            itemBody.append(getattr(item, name))
            colorModel = item.colors
            if name in ["id", "name"]:
                itemColours.append(getattr(item, name))
            elif name is not "komplet":
                itemColours.append(getattr(colorModel, name))        
        body.append([itemBody, str(item.komplet)])
        colours.append(itemColours)


    args = {
        "headers" : ORDER,
        "body" : body,
        "colours": colours,
        "link" : link,
        "isHidden" : hidden,
    }

    return render(request, "board/index.html", args)


def hidden(request):
    return index(request, True)


def updateRows(request):
    # Lav sikkersheds check sådan at man ikke kan ændre id.
    data = json.loads(((request.body).decode('utf-8')))
    row = data["id"]
    column = int(data["column"])
    newValue = data["newValue"]


    print("Updating")
    print(row)
    print(ORDER[column])
    print(newValue)

    item = get_object_or_404(Item, id=row)



    setattr(item, ORDER[column], newValue)
    item.save()
    return HttpResponse('')

def hideRow(request):
    data = json.loads(((request.body).decode('utf-8')))
    print(data["id"])
    row = data["id"]
    print("hiding row " + str(row))
    item = get_object_or_404(Item, id=row)
    item.komplet = not (item.komplet)
    item.save()
    return HttpResponse('')

def addRow(request):
    data = json.loads(((request.body).decode('utf-8')))
    name = data["text"]
    print(name)
    item = Item(name=name)
    item.save()
    colors = Colors(itemLinked=item)
    colors.save()

    return HttpResponse('')












