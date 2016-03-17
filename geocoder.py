# -*- coding: utf-8 -*-
from geopy.geocoders import Nominatim
import csv

geolocator=	Nominatim()

filename=	 "DataJournalismJobs_postingLocationsRaw.csv"
with open(filename, "rt") as csvFile:
	csvReader=	csv.DictReader(csvFile)
	for row in csvReader:
		jobLocation=	row["Location"]
		geoLocation=	geolocator.geocode(jobLocation)
		if(geoLocation==None):
			locationName=	None 
			latitude=		None 
			longitude=		None
		else:
			try:
				locationName=	geoLocation.address
				latitude=		geoLocation.latitude
				longitude=		geoLocation.longitude
				print(jobLocation)
				print(locationName)
				print(latitude)
				print(longitude)
				print("========")
			except Exception as e:
				print(e)
