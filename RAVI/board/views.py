from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

import csv

from board.models import *
from django.conf import settings

import json


def genValueBody(items, withColour, withKompletStates):
    #This takes a database query from items and converts it into an array with the following structure.
    # body[item[value]]
    # If the two settings are set to true it will return this
    # body[item[value, colour], komplet]
    body = []

    for item in items:
        itemBody = []
        for name in ORDER:
            value = getattr(item, name)
            colour = ""
            if(withColour):
                colourModel = item.colours
                
                if name not in ["id", "komplet"]:
                    colour = getattr(colourModel, name) 
                itemBody.append([value, colour])   
            else:
                itemBody.append(value) 
        if withKompletStates:
            body.append([itemBody, str(item.komplet)])
        else:
            body.append(itemBody)

    return body


def index(request, hidden=False):

    items = Item.objects.filter(komplet= hidden).order_by("id")

    body = genValueBody(items, True, True)
    link = "/"
    if not hidden:
        link = link + "hidden"


    


    args = {
        "headers" : ORDER,
        "body" : body,
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
    item = Item(projekt=name)
    item.save()
    colours = Colours(itemLinked=item)
    colours.save()

    return HttpResponse('')


def updateColour(request):
    data = json.loads(((request.body).decode('utf-8')))


    row = data["row"]
    column = ORDER[int(data["column"])]
    colour = data["colour"]

    print(row)
    print(column)
    print(colour)

    item = get_object_or_404(Item, id=row)
    colourItem = item.colours
    setattr(colourItem, column, colour)
    colourItem.save()

    return HttpResponse('')


def toCsv(response):
    items = Item.objects.all().order_by("id")

    body = genValueBody(items, False, True)

    #Tell the browser to be ready for our csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    #And write the data
    csv_writer = csv.writer(response)
    csv_writer.writerow(ORDER + ["komplet"]) # write headers
    for row in body:
        csv_writer.writerow(row[0] + [row[1]])

    return response









