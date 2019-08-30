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
			value1=form.cleaned_data['data1']
			value2=form.cleaned_data['data2']
	
			sensorsdata.recordata(value1, value2)
			return render(request, 'pages/show.html', {'value1': value1, 'value2': value2})	

	else:
		form=Fields()
		return render(request, 'pages/error.html')
