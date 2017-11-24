from django.db import models

#These values make the ORDER setting easier. 
ID = "id"
Name = "name"
Komplet = "komplet"





class Item(models.Model):
	id = models.AutoField(primary_key=True)
	idColour = models.TextField()
	name = models.TextField(verbose_name="Projekt")
	nameColour = models.TextField()


	komplet = models.BooleanField(default=False, verbose_name="Komplet")
	kompletColour = models.BooleanField(default=False)


	def __str__(self):
		return self.name

class VærdiModel(models.Model):
	item = models.OneToOneField(Item, primary_key=True)
	colour = models.TextField()


	def __str__(self):
		return self.__class__.__name__

class Kunde(VærdiModel):
	value = models.TextField()

class Antal(VærdiModel):
	value = models.TextField()

class Data(VærdiModel):
	value = models.TextField()

class Stencil(VærdiModel):
	value = models.TextField()

class Program(VærdiModel):
	value = models.TextField()

class Montage(VærdiModel):
	value = models.TextField()

class Levering(VærdiModel):
	value = models.TextField()

class PCB(VærdiModel):
	value = models.TextField()

class Komponenter(VærdiModel):
	value = models.TextField()

class Kommentar(VærdiModel):
	value = models.TextField()

	
# I know this is not pretty but i could not find another way
# Write the values you want to be displayed in order. 
# Note that ID, name and komplet must be present. Please use the names present in models.py



ORDER = [ID, Kunde, Name, Antal, Data, Komplet]


