from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . models import Fields

def home(request):

	return render (request, "pages/home.html")

def post(request):

	return render (request, "pages/post.html")

def show(request):
	from . import sensorsdata

	if request.method == 'POST':
		form = Fields(request.POST)
		value1 = form.data1
		value2 = form.data2

	
		sensorsdata.recordata(value1, value2)
		return render(request, 'pages/show.html', {'form.data1': form.data1}, {'form.data2': form.data2})	

	else:
		form=Fields()
		return render(request, 'pages/error.html')
