from django.db import models

        

        
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Projekt", default="")
    komplet = models.BooleanField(default=False, verbose_name="Komplet")



    kunde = models.TextField(default="")
    antal = models.TextField(default="")
    data = models.TextField(default="")
    stencil = models.TextField(default="")
    program = models.TextField(default="")
    montage = models.TextField(default="")
    PCB = models.TextField(default="")
    komponenter = models.TextField(default="")
    kommentar = models.TextField(default="")

    


class Colors(models.Model):
    itemLinked = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)

    kunde = models.CharField(default="", max_length=20)
    antal = models.CharField(default="", max_length=20)
    data = models.CharField(default="", max_length=20)
    stencil = models.CharField(default="", max_length=20)
    program = models.CharField(default="", max_length=20)
    montage = models.CharField(default="", max_length=20)
    PCB = models.CharField(default="", max_length=20)
    komponenter = models.CharField(default="", max_length=20)
    kommentar = models.CharField(default="", max_length=20)


        
    
# I know this is not pretty but i could not find another way
# Write the values you want to be displayed in order. 
# Note that ID, name and komplet must be present. Please use the names present in models.py



ORDER = ["id","kunde", "name", "antal", "data", "komplet"]


