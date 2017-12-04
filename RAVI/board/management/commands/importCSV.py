from django.core.management.base import BaseCommand
import os
import csv
from board.models import *

class Command(BaseCommand):
	help = "Imports the specified csv file and convertion data. Convertion data is just a csv file where column 0 is the database headers in the csv and column 1 is the headers in django"

	def add_arguments(self, parser):
		parser.add_argument("file", nargs="+", type=str)
		parser.add_argument("convFile", nargs="+", type=str)

	def handle(self, *args, **options):
		rawdata = []

		csvfile = os.path.abspath(options["file"][0])
		with open(csvfile, 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				rawdata.append(row)


		csvheader = rawdata[0]

		headerConverter = {}

		convFile = os.path.abspath(options["convFile"][0])

		with open(convFile, 'r') as convFile:
			reader = csv.reader(convFile)
			for row in reader:
				print(row)
				try:
					headerConverter[row[0].replace(" ", "")] = row[1].replace(" ", "")
				except IndexError:
					pass

		print(headerConverter)

		for i in range(1, len(rawdata)):
			dataRow = rawdata[i]
			item = Item()
			print("Converting row " + str(i))
			for column in csvheader:
				if column is not "" and column in csvheader and column in headerConverter:
					convertedHeader = headerConverter[column]
					value = dataRow[csvheader.index(column)]

					print("    " + convertedHeader + ": " + value)
					if convertedHeader is not headerConverter[csvheader[len(csvheader)-1]]:
						setattr(item, convertedHeader, value)
					else:
						setattr(item, headerConverter[column], value in "True")

			item.save()
		