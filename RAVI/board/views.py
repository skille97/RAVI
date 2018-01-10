from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

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

def genHeader(verbose_names, order):
    header = []
    for i in order:
        if verbose_names:
            name = Item._meta.get_field(i).verbose_name
        else:
            name = i
        header.append(name)
    return header



def index(request, hidden=False):
    items = Item.objects.filter(komplet= hidden).order_by("id")

    body = genValueBody(items, True, True)
    link = "/"
    if not hidden:
        link = link + "hidden"


    


    args = {
        "headers" : genHeader(True, ORDER),
        "body" : body,
        "link" : link,
        "isHidden" : hidden,
    }

    return render(request, "board/index.html", args)


def hidden(request):
    return index(request, True)


def checkColumn(column):
    if (column not in range(0, len(ORDER))):
        print("User trying to change column out of range. Aborting")
        return False
    elif ORDER[column] in ["id"]:
        print("User trying to change illegal columns. Aborting")
        return False
    return True

@csrf_exempt
def updateRows(request):

    # Try parsing
    try:
        data = json.loads(((request.body).decode('utf-8')))
        row = data["id"]
        column = int(data["column"])
        newValue = data["newValue"]
    except Exception as e:
        print("Tried updating a cell with data")
        print(request.body)
        print("But encountered an error")
        return HttpResponseBadRequest("Missing data")


    if not checkColumn(column):
        return HttpResponseForbidden("Illegal column")

    item = get_object_or_404(Item, id=row)

    setattr(item, ORDER[column], newValue)




    item.save()
    return HttpResponse('')

@csrf_exempt
def hideRow(request):
    try:
        data = json.loads(((request.body).decode('utf-8')))
        row = data["id"]
    except Exception as e:
        print("Tried hiding row with data")
        print(request.body)
        print("But encountered an error")
        return HttpResponseBadRequest("Missing data")

    item = get_object_or_404(Item, id=row)
    item.komplet = not (item.komplet)
    item.save()
    return HttpResponse('')

@csrf_exempt
def addRow(request): 
    try:
        data = json.loads(((request.body).decode('utf-8')))
        name = data["text"]
    except Exception as e:
        print("Tried adding row with data")
        print(request.body)
        print("But encountered an error")
        return HttpResponseBadRequest("Missing data")

    item = Item(projekt=name)
    item.save()
    colours = Colours(itemLinked=item)
    colours.save()

    return HttpResponse('')

@csrf_exempt
def updateColour(request):
    try:
        data = json.loads(((request.body).decode('utf-8')))
        row = data["row"]
        column = int(data["column"])
        colour = data["colour"]
    except Exception as e:
        print("Tried updating colour with data")
        print(request.body)
        print("But encountered an error")
        return HttpResponseBadRequest("Missing data")

    
    if not checkColumn(column):
        return HttpResponseForbidden("Illegal column")

    item = get_object_or_404(Item, id=row)
    colourItem = item.colours
    setattr(colourItem, ORDER[column], colour)
    colourItem.save()

    return HttpResponse('')

@csrf_exempt
def toCsv(response):
    items = Item.objects.all().order_by("id")

    body = genValueBody(items, False, True)

    #Tell the browser to be ready for our csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv.csv"'

    #And write the data
    csv_writer = csv.writer(response)
    csv_writer.writerow(ORDER + ["komplet"]) # write headers
    for row in body:
        csv_writer.writerow(row[0] + [row[1]])

    return response









