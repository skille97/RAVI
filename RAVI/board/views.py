from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


from board.models import *
from django.conf import settings

import json

def index(request, hidden=False):

    items = Item.objects.filter(komplet= not hidden).order_by("id")

    body = []
    colours = []
    hiddenStates = []
    link = "/"
    if not hidden:
        link = link + "hidden"

    for item in items:
        itemBody = []
        itemColours = []
        for name in ORDER:
            itemBody.append(getattr(item, name))
            colorModel = item.Colors
            itemColours.append(getattr(colorModel, name))
                        
        body.append(itemBody)
        colours.append(itemColours)
        if(hidden):
            hiddenStates.append(item.komplet)

    args = {
        "headers" : ORDER,
        "body" : body,
        "colours": colours,
        "hiddenStates" : hiddenStates,
        "link" : link,
        "isHidden" : hidden,
    }
    return render(request, "board/index.html", args)


def hidden(request):
    return index(request, True)


def updateRows(request):
    row = request.POST.get("id")
    column = request.POST.get("column")
    newValue = request.POST.get("newValue")


    item = get_object_or_404(Item, id=row)

    setattr(item, column, newValue)
    item.save()
    return HttpResponse('')

def hideRow(request):
    row = request.POST.get("id")

    item = Item.objects.get_object_or_404(Item, id=row)
    item.komplet = not (item.komplet)
    item.save()
    return HttpResponse('')

def addRow(request):
    print("Hej")
    name = request.POST.get("text", "test")
    print(name)
    item = Item(name=name)
    item.save()
    colors = Colors(name=name, item=item)
    colors.save()

    return HttpResponse('')












