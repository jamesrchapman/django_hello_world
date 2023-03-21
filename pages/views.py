from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def homePageView(request):
	return HttpResponse("What's good man")