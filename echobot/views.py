from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import Name

def index(request):
	data=''
    # if this is a POST request we need to process the form data
  	if request.method == 'POST':
  	# create a form instance and populate it with data from the request:
  	# form = NameForm(request.POST)
  	# check whether it's valid:
  		data=request.POST.get('textfield','')
        obj=Name(input_text=data)
        obj.save()
        #     # process the data in form.cleaned_data as required
        #     # ...
        #     # redirect to a new URL:
        #     return HttpResponseRedirect()

    # if a GET (or any other method) we'll create a blank form
    
	return render(request, 'index.html', {'data': data})