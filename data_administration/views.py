from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . forms import Fields

def home(request):

	return render (request, "pages/home.html")

def post(request):
	
	from . import sensorsdata
		
	hum = request.GET['data1']
	tem = request.GET['data2']

	sensorsdata.recordata(hum, tem)
	
	return render (request, "pages/show.html", {'hum':hum}, {'tem':tem})
	