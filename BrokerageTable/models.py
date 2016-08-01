from django.db import models

class Brokerage(models.Model):
	BrokerageName = models.CharField(max_length=500)
	#To-Do Fix additional settings for ImagesFields/FileFields
	#BrokerageLogo = ImageField
	ReviewLink = models.CharField(max_length=1000)
	ContactLink = models.CharField(max_length=1000)
	TotalAgents = models.IntegerField()
	Location = models.CharField(max_length=500)
	Desks = models.IntegerField()
	YearlyCosts = models.DecimalField(max_digits=12, decimal_places=2)
	CommisionSplit = models.CharField (max_length=8)
	#To-Do set a getter for Cap that returns none
	Cap =  models.DecimalField(max_digits=12, decimal_places=2)
	TrainingPerWeek = models.IntegerField()
	Onboarding = models.BooleanField()
	Mentorship = models.BooleanField()
	Teams_Hiring = models.BooleanField()
	Marketing = models.CharField(max_length=500)
	TotalListings = models.IntegerField()
	ConferenceRooms = models.BooleanField()
	OfficeLeaders = models.CharField (max_length=500)
	#OfficeLeaderPhoto = models.ImageField

