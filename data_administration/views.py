from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . forms import Fields

def home(request):

	return render (request, "pages/home.html")

def post(request):
	form = Fields(request.POST)

	return render (request, "pages/post.html", {'form':form})

def show(request):
	from . import sensorsdata

	if request.method == 'POST':
		form = Fields(request.POST)
		if form.is_valid():
			hum = form.cleaned_data['data1']
			temp = form.cleaned_data['data2']
	
			sensorsdata.recordata(hum, temp)
			return render(request, 'pages/print.html', {'value1': hum, 'value2': temp})	

	else:
		form=Fields()
		return render(request, 'pages/error.html')
