from django.shortcuts import render
from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
	queryset=PageVisit.objects.all()
	page_queryset=PageVisit.objects.filter(path=request.path)
	PageVisit.objects.create(path=request.path)
	context = {
		"title": "My Django App", 
		"total_visits": queryset,
		"page_visits": page_queryset,
		"percentage": round((page_queryset.count()/queryset.count())*100, 2) if queryset.count() > 0 else 0
	}
	return render(request, 'home.html' , context)