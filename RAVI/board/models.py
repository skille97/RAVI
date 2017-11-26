from django.db import models

        

        
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    komplet = models.BooleanField(default=False, verbose_name="Komplet")
    #Hvis dette navn ændres skal det også ændres i views.py i linje 90. Sååå kun gør det hvis det er nødvendigt
    projekt = models.CharField(default="", max_length=20)

    
    kunde = models.CharField(default="", max_length=20)
    antal = models.CharField(default="", max_length=20)
    data = models.CharField(default="", max_length=20)
    stencil = models.CharField(default="", max_length=20)
    program = models.CharField(default="", max_length=20)
    montage = models.CharField(default="", max_length=20)
    PCB = models.CharField(default="", max_length=20)
    komponenter = models.CharField(default="", max_length=20)
    kommentar = models.CharField(default="", max_length=20)

    
    def __str__(self):
        return str(self.id)


class Colours(models.Model):
    itemLinked = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)


    projekt = models.CharField(default="", max_length=20)
    kunde = models.CharField(default="", max_length=20)
    antal = models.CharField(default="", max_length=20)
    data = models.CharField(default="", max_length=20)
    stencil = models.CharField(default="", max_length=20)
    program = models.CharField(default="", max_length=20)
    montage = models.CharField(default="", max_length=20)
    PCB = models.CharField(default="", max_length=20)
    komponenter = models.CharField(default="", max_length=20)
    kommentar = models.CharField(default="", max_length=20)

    def __str__(self):
        return str(self.itemLinked.id)

        
    
# I know this is not pretty but i could not find another way
# Write the values you want to be displayed in order. 
# Note that ID, name must be present. Please use the names present in models.py
# komplet is added at de end automaticly

#        |DO NOT CHANGE |  CHANGE THESE
ORDER =     ["id"]  +     ["kunde", "antal", "data", "stencil", "program", "montage", "PCB", "komponenter", "kommentar"]


