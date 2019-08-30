from django import forms

class Fields (forms.Form):
	
    data1 = forms.CharField(label='humidity', max_length=255)
    
    data2 = forms.CharField(label='temperature',max_length=255)


   