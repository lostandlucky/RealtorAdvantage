from django.shortcuts import render
from django.views import generic
from .models import Brokerage

class BrokerageTable(generic.ListView):
	template_name = 'BrokerageTable/BrokerageTable.html'
	context_object_name = 'Brokerage_List'
	
	def get_queryset(self):
		return Brokerage.objects.all()
