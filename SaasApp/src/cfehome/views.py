from django.shortcuts import render


def home_page_view(request, *args, **kwargs):
	context = {
		"title": "My Django App", 	
	}
	return render(request, 'home.html' , context)