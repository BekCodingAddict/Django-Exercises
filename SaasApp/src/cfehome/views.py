from django.shortcuts import render
from visits.models import PageVisit

def home_view(request, *args, **kwargs):
	return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
	queryset=PageVisit.objects.all()
	page_queryset=PageVisit.objects.filter(path=request.path)
	try:
		percentage = round((page_queryset.count()/queryset.count())*100, 2) if queryset.count() > 0 else 0
	except ZeroDivisionError:
		percentage = 0

	PageVisit.objects.create(path=request.path)
	context = {
		"title": "My Django App", 
		"total_visits": queryset,
		"page_visits": page_queryset,
		"percentage": percentage
	}

	return render(request, 'about.html' , context)